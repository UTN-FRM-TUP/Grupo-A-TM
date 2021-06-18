import pygame
from pygame.locals import QUIT
import numpy as np
import sys
from escenario import escenario, cantidad_celdas, nombre_archivo
import time
from persona import Persona
from celdas import evalua_celda_vecina


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
ancho_pantalla = nxC * DIMENSION_CELDA
alto_pantalla = nyC * DIMENSION_CELDA

screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

screen.fill(COLOR_FONDO)

pygame.display.set_caption(nombre_archivo())


def main():
    # Inicia todos los módulos importados
    pygame.init()

    # Variable bandera para pausar la simulacion
    pauseExect = False

    # Crea el estado del juego a partir del archivo provisto por el usuario
    estado_juego = escenario()

    # Contadores de estado de las personas
    muertos = 0
    heridos = 0
    salvados = 0

    # Crea una lista con las posicines de las personas
    personas = []

    # Recorre la matriz y crea una persona en la posición corespondiente
    ide = 0
    for y in range(0, nxC):
        for x in range(0, nyC):
            if estado_juego[x, y] == 9:
                personas.append(Persona(ide, estado_juego, x, y))
                ide += 1

    # -------- Loop principal -----------
    while True:

        # Disminuye velocidad
        time.sleep(0.3)

        # Crea un nuevo estado sobre el que se producen las modificaciones
        nuevo_estado = np.copy(estado_juego)

        screen.fill(COLOR_FONDO)

        # Maneja los eventos
        ev = pygame.event.get()

        for event in ev:

            # Detectamos si se presiona una tecla pra controlar la pausa
            if event.type == pygame.KEYDOWN:
                pauseExect = not pauseExect

            # Cierrra la simulacion si se cierra la ventana
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        mover = True

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

                # Dibuja cada elemento
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

                # Movimiento de las personas
                celdas_vecinas = {}

                if not pauseExect:

                    if estado_juego[x, y] == 9:
                        if len(personas) > 0:
                            if mover:
                                for person in personas:
                                    celdas_vecinas = evalua_celda_vecina(person.x, person.y, nuevo_estado)
                                    person.elegir_direccion(
                                        nuevo_estado, celdas_vecinas)
                                    print(person.ide, person.x, person.y)
                                    if person.muerto == True:
                                        print("muerto")
                                        personas.remove(person)
                                        muertos += 1
                                    elif person.salvado == True:
                                        print("salvado")
                                        personas.remove(person)
                                        salvados += 1
                                    elif person.herido == True:
                                        print("herido")
                                        heridos += 1

                            mover = False
                        else:
                            break

        estado_juego = np.copy(nuevo_estado)

        # Recarga la pantalla
        pygame.display.flip()


if __name__ == '__main__':
    main()
