
# Acá va la función que lee la matriz desde el archivo provisto por el usuario
# Por ahora es un ejemplo para chekear funcionamiento
# TODO Modificar por caracteres

import numpy as np

# Esta ruta de archivo se obtiene desde la GUI y la ingresa el usuario
archivo = '/home/nahuel/MEGA/Tecnicatura en programación/Primer Año/Metodología de investigación/Proyecto/Proyecto MDI/Grupo-A-TM/Proyecto/matriz.txt'
# archivo = '/home/nahuel/Descargas/plano.txt'

matriz = np.genfromtxt(archivo, delimiter=',')


def escenario():

    grid = matriz

    return grid
