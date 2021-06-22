#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Este módulo contiene la clase que crea la ventana"""

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from GUI_simulador import Ui_Simulador


class Vista(QMainWindow, Ui_Simulador):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        """ self.ruta = '2222'


    def buscarRutaArchivo(self):
        archivo = QFileDialog.getOpenFileName(self, 'Abrir archivo', '/home')
        self.ruta = archivo[0]
        print('ruta de objeto vista:', self.ruta) """
        
    