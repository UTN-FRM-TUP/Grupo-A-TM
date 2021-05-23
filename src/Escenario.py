import numpy as np

# Esta ruta de archivo se obtiene desde la GUI y la ingresa el usuario
archivo = '/home/nahuel/Descargas/plano.txt'


def crear_matriz_desde_archivo():
    matriz = np.genfromtxt(archivo, delimiter=',')
    return matriz


def cantidad_celdas():
    grid = crear_matriz_desde_archivo()
    return len(grid[0])-1, len(grid)


def escenario():
    grid = crear_matriz_desde_archivo()
    return grid
