import pygame
from pygame.locals import QUIT
import sys
from Escenario import escenario, cantidad_celdas, nombre_archivo

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

pygame.display.set_caption(nombre_archivo())


def main():
    # Inicia todos los módulos importados
    pygame.init()

    # Crea el estado del juego a partir del archivo provisto por el usuario
    gameState = escenario()

    # -------- Loop principal -----------
    while True:

        # Maneja los eventos
        ev = pygame.event.get()

        for event in ev:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

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
                if gameState[x, y] == 0:
                    pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
                elif gameState[x, y] == 2:
                    pygame.draw.polygon(screen, (AZUL), poly, 0)
                elif gameState[x, y] == 5:
                    pygame.draw.polygon(screen, (VERDE), poly, 0)
                elif gameState[x, y] == 6:
                    pygame.draw.polygon(screen, (NEGRO), poly, 0)
                else:
                    pygame.draw.polygon(screen, (BLANCO), poly, 0)

        # Recarga la pantalla
        pygame.display.flip()


if __name__ == '__main__':
    main()
