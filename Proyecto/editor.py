import pygame
from pygame.locals import QUIT
import numpy as np
import sys

pygame.init()

altura, ancho = 100, 100

bg = 25, 25, 25

screen = pygame.display.set_mode((ancho, altura))
screen.fill(bg)

# Tamaño de la matriz
nxC, nyC = 5, 5

# Estado de las celdas. Pared = 1 / Espacio = 0
# Genera una matriz inicial con todas las celdas en 0
gameState = np.zeros((nxC,  nyC), dtype=int)

# Dimensiones de cada celda individual
dimensionCeldaAncho = 20
dimensionCeldaAlto = 20


while True: 

    newGameState = np.copy(gameState)

    # Cada vez que identificamos un evento lo procesamos
    ev = pygame.event.get()

    for event in ev:

        # Identifica la celda presionada con el mouse
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.trunc(posX / dimensionCeldaAncho)), int(
                np.trunc(posY / dimensionCeldaAlto))
            newGameState[celX, celY] = 1

        # Cierra el editor
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for y in range(0, nxC):
        for x in range(0, nyC):

            # Calcula el polígono (cuadrado) que forma la celda.
            poly = [((x) * dimensionCeldaAncho, y * dimensionCeldaAlto),
                    ((x+1) * dimensionCeldaAncho, y * dimensionCeldaAlto),
                    ((x+1) * dimensionCeldaAncho, (y+1) * dimensionCeldaAlto),
                    ((x) * dimensionCeldaAncho, (y+1) * dimensionCeldaAlto)]

            # Si es espacio pinta un recuadro con borde gris
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)

            # Si es pared pinta un recuadro relleno de color
            else:
                pygame.draw.polygon(screen, (200, 100, 100), poly, 0)

    # Actualiza el estado del juego.
    gameState = np.copy(newGameState)

    # Muestra el resultado
    pygame.display.flip()

    np.savetxt('escenario.txt', gameState)

    """ # Escribe los cambios realizados en un archivo
    archivo = 'escenario.txt'
    with open(archivo, 'w') as f:
        f.write(str(gameState)) """
