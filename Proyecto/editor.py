import pygame
from pygame.locals import QUIT
import numpy as np
import sys

pygame.init()

altura, ancho = 100, 100

bg = 25, 25, 25

screen = pygame.display.set_mode((ancho, altura))
screen.fill(bg)

# Tamaño de nuestra matriz
nxC, nyC = 5, 5

# Estado de las celdas. Pared = 1 / Espacio = 0
gameState = np.zeros((nxC,  nyC), dtype=int)

# dimensiones de cada celda individual
dimensionAltoCelda = 30
dimensionAnchoCelda = 30


while True: 

    newGameState = np.copy(gameState)

    ev = pygame.event.get()

    # Cada vez que identificamos un evento lo procesamos
    for event in ev:

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.trunc(posX / dimensionAnchoCelda)), int(
                np.trunc(posY / dimensionAltoCelda))
            newGameState[celX, celY] = 1

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for y in range(0, nxC):
        for x in range(0, nyC):

            # Calculamos el polígono que forma la celda.
            poly = [((x) * dimensionAnchoCelda, y * dimensionAltoCelda),
                    ((x+1) * dimensionAnchoCelda, y * dimensionAltoCelda),
                    ((x+1) * dimensionAnchoCelda, (y+1) * dimensionAltoCelda),
                    ((x) * dimensionAnchoCelda, (y+1) * dimensionAltoCelda)]

            # Si es espacio pintamos un recuadro con borde gris
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
            # Si es pared pintamos un recuadro relleno de color
            else:
                pygame.draw.polygon(screen, (200, 100, 100), poly, 0)

    # Actualizamos el estado del juego.
    gameState = np.copy(newGameState)

    # Mostramos el resultado
    pygame.display.flip()

    # np.savetxt('escenario.txt', gameState, delimiter=',')

    archivo = 'escenario.txt'
    with open(archivo, 'w') as f:
        f.write(str(gameState))
        

