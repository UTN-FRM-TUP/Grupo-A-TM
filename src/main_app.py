#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
from PyQt5.QtWidgets import QApplication
import numpy as np
from vista import Vista
from escenario import Escenario

# Inicia las instancias necesarias
app = QApplication(sys.argv)
vista = Vista()
escenario = Escenario()

cantidad_muertos = 0
cantidad_salvados = 0
cantidad_heridos = 0
extintores = False

# Establece rutas para archivos de persistencia
archivo_ruta = 'Grupo-A-TM/src/path.txt'
archivo_extintores = 'Grupo-A-TM/src/extintores.txt'
archivo_informe = 'Grupo-A-TM/src/informe.txt'


def abrirSimulacion():
    """ Inicia la simulacion llamando a pygame """
    borrar_informe(archivo_informe)
    subprocess.call("Grupo-A-TM/src/main_pygame.py")

def contraIncendios(archivo):
    """ Guarda el valor True cuando está activo el sistema contra incendios """
    with open(archivo, "w") as extintores:
        extintores.write('True')

def manejar_ruta(escenario, archivo):
    """ Realiza las acciones sobre la ruta: obtiene, coloca en GUI, guarda """
    escenario.buscarRutaArchivo()
    vista.rutaArchivo.setText(escenario.archivo)
    guardar_ruta(archivo, escenario.archivo)

def guardar_ruta(archivo, texto):
    """ Guarda la ruta provista en un archivo """
    with open(archivo, "w") as ruta:
        ruta.write(f'{texto}')

def borrar_informe(archivo):
    """ Borra el archivo """
    with open(archivo, "w") as informe:
        informe.write('')

def mostrar_informe(archivo):
    """ Muestra en informe de estado en la interfaz """
    with open(archivo, 'r') as informe:
        vista.informeResultados.setText(informe.read())
    
# Checkbox que indica si existe sistema contra incendios
vista.contraIncendios.stateChanged.connect(lambda: contraIncendios(archivo_extintores))

# Botón para buscar el archivo de forma local
vista.buscarRuta.clicked.connect(lambda: manejar_ruta(escenario, archivo_ruta))

# Botón para iniciar la simulación
vista.botonIniciar.clicked.connect(lambda: abrirSimulacion())

# Botón para visualizar los resultados
vista.mostrarResultados.clicked.connect(lambda: mostrar_informe(archivo_informe))

if __name__ == "__main__":

    vista.show()
    sys.exit(app.exec())