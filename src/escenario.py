#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Modulo de funciones para el manejo del escenario """

import numpy as np
import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog

# Esta ruta de archivo se obtiene desde la GUI y la ingresa el usuario

class Escenario(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.archivo = '1234'

    def buscarRutaArchivo(self):
        archivo = QFileDialog.getOpenFileName(self, 'Abrir archivo', '/home')
        self.archivo = archivo[0]
        print('ruta de objeto escenario:', self.archivo)

    def crear_matriz_desde_archivo(self):
        try:
            matriz = np.genfromtxt(self.archivo, delimiter=',')
        except OSError:
            print('La ruta especificada no existe')
            print('Por favor cambie la ruta a un archivo válido')
            sys.exit()
        else:
            return matriz


    def nombre_archivo(self):
        auxlist = list(self.archivo.split('/'))
        nombre = auxlist[len(auxlist)-1]
        return nombre


    def cantidad_celdas(self):
        grid = self.crear_matriz_desde_archivo()
        return len(grid[0])-1, len(grid)


    def escenario(self):
        grid = self.crear_matriz_desde_archivo()
        return grid
