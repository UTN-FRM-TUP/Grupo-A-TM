#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
from PyQt5.QtWidgets import QApplication
from vista import Vista

app = QApplication(sys.argv)
vista = Vista()

# Código

vista.botonIniciar.clicked.connect(lambda: abrirSimulacion())

def abrirSimulacion():
    subprocess.call("Grupo-A-TM/src/main_pygame.py")

if __name__ == "__main__":

    vista.show()
    sys.exit(app.exec())