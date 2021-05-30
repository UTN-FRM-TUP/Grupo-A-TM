import pygame
from pygame.locals import QUIT
import numpy as np
import sys
from escenario import escenario, cantidad_celdas, nombre_archivo
import time
import random


# Configuración de valores iniciales
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

COLOR_FONDO = 25, 25, 25

DIMENSION_CELDA = 20

# Tamaño de la matriz
nxC, nyC = cantidad_celdas()

# Establece el ancho y alto de la pantalla
screen = pygame.display.set_mode((
    nxC * DIMENSION_CELDA, nyC * DIMENSION_CELDA))

screen.fill(COLOR_FONDO)

contador = 0

pygame.display.set_caption(nombre_archivo())


def evalua_celda_vecina(estado, x, y):
    celdas_vecinas = {}
    celdas_vecinas.update({'derecha': estado[x, y+1]})
    celdas_vecinas.update({'abajo': estado[x+1, y]})
    celdas_vecinas.update({'izquierda': estado[x, y-1]})
    celdas_vecinas.update({'arriba': estado[x-1, y]})
    return celdas_vecinas


def elegir_direccion(celdas_vecinas, estado, x, y):

    espacios_vacios = []

    if not estado[x, y] == 6:
        for direccion in celdas_vecinas:
            if celdas_vecinas[direccion] == 6:  # salida
                eleccion(direccion, estado, x, y)
                # continue
                """ elif celdas_vecinas[direccion] == 5:  # salida de emergencia
                eleccion(direccion, estado, x, y)
                direccion_anterior = direccion
                # continue """
            elif celdas_vecinas[direccion] == 0:  # espacio vacio
                espacios_vacios.append(direccion)
                
                """ elif celdas_vecinas[direccion] == 2:    # Puerta abierta
                eleccion(direccion, estado, x, y)
                direccion_anterior = direccion
                # continue
         
             elif celdas_vecinas[direccion] == 8:    # fuego apagado
                eleccion(direccion, estado, x, y)
                direccion_anterior = direccion
                # continue
                elif celdas_vecinas[direccion] == 7:    # Fuego activo
                # condicion = 'herido'
                volver(direccion_anterior, estado, x, y)
                # continue """
            elif celdas_vecinas[direccion] == 1:    # Pared
                continue
 
    """ if bandera is True:
        print("hola")
        print(espacios_vacios)
        if direccion_anterior == 'izquierda':
            if 'derecha' in espacios_vacios:
                espacios_vacios.remove('derecha')
        elif direccion_anterior == 'derecha':
            if 'izquierda' in espacios_vacios:
                espacios_vacios.remove('izquierda')
        elif direccion_anterior == 'arriba':
            if 'abajo' in espacios_vacios:
                espacios_vacios.remove('abajo')
        elif direccion_anterior == 'abajo':
            if 'arriba' in espacios_vacios:
                espacios_vacios.remove('arriba') """

    print("espacio con eliminacion", espacios_vacios)
    direccion_entre_ceros = random.choice(espacios_vacios)
    direccion_anterior = direccion_entre_ceros

    print(direccion_anterior)

    eleccion(direccion_entre_ceros, estado, x, y)

    espacios_vacios.clear()


""" def guardar_direccion(celdas_vecinas):
    espacios_vacios = []
    for direccion in celdas_vecinas:
        if celdas_vecinas[direccion] == 0:  # espacio vacio
            espacios_vacios.append(direccion)

    return random.choice(espacios_vacios) """
    

def volver(direccion, estado, x, y):
    if direccion == "izquierda":
        derecha(estado, x, y)
    if direccion == "derecha":
        izquierda(estado, x, y)
    if direccion == "arriba":
        arriba(estado, x, y)
    if direccion == "abajo":
        arriba(estado, x, y)


def eleccion(direccion, estado, x, y):
    if direccion == "izquierda":
        izquierda(estado, x, y)
    if direccion == "derecha":
        derecha(estado, x, y)
    if direccion == "arriba":
        arriba(estado, x, y)
    if direccion == "abajo":
        abajo(estado, x, y)


def izquierda(estado, x, y):
    actual = estado[x, y]
    proximo = estado[x, y-1]
    estado[x, y] = proximo
    estado[x, y-1] = actual


def derecha(estado, x, y):
    actual = estado[x, y]
    proximo = estado[x, y+1]
    estado[x, y] = proximo
    estado[x, y+1] = actual


def arriba(estado, x, y):
    actual = estado[x, y]
    proximo = estado[x-1, y]
    estado[x-1, y] = actual
    estado[x, y] = proximo


def abajo(estado, x, y):
    actual = estado[x, y]
    proximo = estado[x+1, y]
    estado[x+1, y] = actual
    estado[x, y] = proximo


def main():
    # Inicia todos los módulos importados

    pygame.init()

    # Crea el estado del juego a partir del archivo provisto por el usuario
    estado_juego = escenario()


    """ for x, y in zip(*np.where(estado_juego == 9)):
        cant_per += cant_per """

    # bandera = False
    
    # -------- Loop principal -----------
    while True:

        # Disminuye velocidad
        time.sleep(2)

        nuevo_estado = np.copy(estado_juego)

        screen.fill(COLOR_FONDO)

        # Maneja los eventos
        ev = pygame.event.get()

        for event in ev:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # Recorre la matriz
        for y in range(0, nxC):
            for x in range(0, nyC):

                # Calcula el polígono (cuadrado) que forma la celda.
                poly = [(y * DIMENSION_CELDA, (x) * DIMENSION_CELDA),
                        (y * DIMENSION_CELDA, (x+1) * DIMENSION_CELDA),
                        ((y+1) * DIMENSION_CELDA, (
                            (x+1) * DIMENSION_CELDA)),
                        ((y+1) * DIMENSION_CELDA, (
                            (x) * DIMENSION_CELDA))]

                # Define como se dibuja cada elemento
                if estado_juego[x, y] == 0:
                    pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
                elif estado_juego[x, y] == 2:
                    pygame.draw.polygon(screen, (AZUL), poly, 0)
                elif estado_juego[x, y] == 5:
                    pygame.draw.polygon(screen, (VERDE), poly, 0)
                elif estado_juego[x, y] == 6:
                    pygame.draw.polygon(screen, (NEGRO), poly, 0)
                elif estado_juego[x, y] == 7:
                    pygame.draw.polygon(screen, (ROJO), poly, 0)
                elif estado_juego[x, y] == 9:
                    pygame.draw.polygon(screen, (0, 255, 255), poly, 0)
                else:
                    pygame.draw.polygon(screen, (BLANCO), poly, 0)

                # Modifica el escenario según el comportamiento de las personas

                celdas_vecinas = {}

                if estado_juego[x, y] == 9:
                    celdas_vecinas = evalua_celda_vecina(nuevo_estado, x, y)
                    elegir_direccion(celdas_vecinas, estado_juego, x, y)
                    # bandera = True
                   
        estado_juego = np.copy(nuevo_estado)

        # Recarga la pantalla
        pygame.display.flip()


if __name__ == '__main__':
    main()