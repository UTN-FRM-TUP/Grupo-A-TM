""" Este modulo gestiona el comportamiento del fuego """

import time
from celdas import evalua_celda_vecina

class Fuego():

    def __init__(self):
        extintores = False
        self.propagacion = 0.5

    def propagacion_fuego(self, x, y, celdasy, celdas_vecinas_fuego, nuevo_estado):

       # time.sleep(self.propagacion) 
        if y != 0 or y != celdasy:
           for direccion in celdas_vecinas_fuego:
                if celdas_vecinas_fuego[direccion] == 7 or (
                    celdas_vecinas_fuego[direccion] == 6 or celdas_vecinas_fuego[direccion] == 8):
                    continue
                elif celdas_vecinas_fuego[direccion] == 1:
                    nuevo_estado[x, y] = 8
                else: 
                    if direccion == "derecha":                  
                            nuevo_estado[x, y+1] = 7
                            nuevo_estado[x, y] = 8
                    elif direccion == "arriba":                  
                            nuevo_estado[x-1, y] = 7
                            nuevo_estado[x, y] = 8
                    elif direccion == "abajo":                 
                            nuevo_estado[x+1, y] = 7
                            nuevo_estado[x, y] = 8
                    elif direccion == "izquierda":                                    
                            nuevo_estado[x, y-1] = 7
                            nuevo_estado[x, y] = 8     
                        