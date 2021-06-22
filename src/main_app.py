#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
from PyQt5.QtWidgets import QApplication
import numpy as np
from vista import Vista
from escenario import Escenario


# ruta = '/home/nahuel/Descargas/escuelaCuadrado5.txt'

app = QApplication(sys.argv)
vista = Vista()
escenario = Escenario()
cantidad_muertos = 0
cantidad_salvados = 0
cantidad_heridos = 0
extintores = False
archivo = 'Grupo-A-TM/src/path.txt'


def abrirSimulacion(escenario):
    print('ruta antes de simulacion', escenario.archivo)
    subprocess.call("Grupo-A-TM/src/main_pygame.py")

def contraIncendios(extintores):
    extintores = True

def manejar_ruta(escenario, archivo):
    escenario.buscarRutaArchivo()
    vista.rutaArchivo.setText(escenario.archivo)
    guardar_ruta(archivo, escenario.archivo)

def guardar_ruta(archivo, texto):
    archivo = open(archivo, "w")
    archivo.write(f'{texto}')
    archivo.close()
    
vista.contraIncendios.stateChanged.connect(lambda: contraIncendios(extintores))

vista.buscarRuta.clicked.connect(lambda: manejar_ruta(escenario, archivo))

vista.botonIniciar.clicked.connect(lambda: abrirSimulacion(escenario))

if __name__ == "__main__":

    vista.show()
    sys.exit(app.exec())