# import numpy as np
import pygame
from pygame.locals import QUIT
import sys
from Escenario import escenario

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

bg = 25, 25, 25


def main():
    # Inicia todos los módulos importados
    pygame.init()

    # Estado de las celdas. Pared = 1 / Espacio = 0
    # Genera una matriz inicial a partir del archivo provisto por el usuario
    # gameState = np.array(enviroment())
    gameState = escenario()

    # Tamaño de la matriz (Estos datos los debería ingresar el usuario)
    nxC, nyC = 25, 18

    # Dimensiones de cada celda individual
    dimensionCeldaAncho = 20
    dimensionCeldaAlto = 20

    # Establece el ancho y alto de la pantalla
    screen = pygame.display.set_mode((
        nxC * dimensionCeldaAncho, nyC * dimensionCeldaAlto))
    screen.fill(bg)

    # -------- Loop principal -----------
    while True:
        ev = pygame.event.get()

        for event in ev:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for y in range(0, nxC):
            for x in range(0, nyC):

                # Calcula el polígono (cuadrado) que forma la celda.
                poly = [(y * dimensionCeldaAlto, (x) * dimensionCeldaAncho),
                        (y * dimensionCeldaAlto, (x+1) * dimensionCeldaAncho),
                        ((y+1) * dimensionCeldaAlto, (
                            (x+1) * dimensionCeldaAncho)),
                        ((y+1) * dimensionCeldaAlto, (
                            (x) * dimensionCeldaAncho))]

                # Si es espacio pinta un recuadro con borde gris
                if gameState[x, y] == 0:
                    pygame.draw.polygon(screen, (40, 40, 40), poly, 1)

                elif gameState[x, y] == 2:
                    pygame.draw.polygon(screen, (BLUE), poly, 0)

                elif gameState[x, y] == 5:
                    pygame.draw.polygon(screen, (GREEN), poly, 0)

                elif gameState[x, y] == 6:
                    pygame.draw.polygon(screen, (BLACK), poly, 0)

                # Si es pared pinta un recuadro relleno de color
                else:
                    pygame.draw.polygon(screen, (WHITE), poly, 0)

        pygame.display.flip()


if __name__ == '__main__':
    main()
