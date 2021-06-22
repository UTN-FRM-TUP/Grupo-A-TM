#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Este modulo gestiona el comportamiento del fuego """

import time
from celdas import evalua_celda_vecina
from main_app import extintores

class Fuego():

    def __init__(self):
        self.contra_incendios = extintores
        self.propagacion = 0.5

    def propagacion_fuego(self, x, y, celdasy, celdasx, celdas_vecinas_fuego, nuevo_estado):
        if y > 1 and y < celdasy: 
            if x > 0 and y < celdasx:         
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
                        