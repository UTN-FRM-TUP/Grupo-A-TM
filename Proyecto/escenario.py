import numpy as np
import sys

# Esta ruta de archivo se obtiene desde la GUI y la ingresa el usuario
archivo = 'A:\cubo.txt'


def crear_matriz_desde_archivo():
    try:
        matriz = np.genfromtxt(archivo, delimiter=',', dtype=int)
    except OSError:
        print('La ruta especificada no existe')
        print('Por favor cambie la ruta a un archivo válido')
        sys.exit()
    else:
        return matriz


def nombre_archivo():
    auxlist = list(archivo.split('/'))
    nombre = auxlist[len(auxlist)-1]
    return nombre


def cantidad_celdas():
    grid = crear_matriz_desde_archivo()
    return len(grid[0])-1, len(grid)


def escenario():
    grid = crear_matriz_desde_archivo()
    return grid