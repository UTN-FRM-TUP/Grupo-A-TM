""" Clase que genera objetos persona """

import random


class Persona():

    def __init__(self, ide, estado, x, y):
        self.ide = ide
        self.estado = estado
        self.x = x
        self.y = y
        self.direccion_anterior = 'a'
        self.salida_emergencia = False

    def evalua_celda_vecina(self, nuevo_estado):
        celdas_vecinas = {}
        celdas_vecinas.update({'derecha': nuevo_estado[self.x, self.y+1]})
        if self.x+1 != 21:
            celdas_vecinas.update({'abajo': nuevo_estado[self.x+1, self.y]})
        celdas_vecinas.update({'izquierda': nuevo_estado[self.x, self.y-1]})
        celdas_vecinas.update({'arriba': nuevo_estado[self.x-1, self.y]})
        return celdas_vecinas

    def elegir_direccion(self, nuevo_estado, celdas_vecinas):

        espacios_vacios = []
        # direcciones_validas = []
        
        if nuevo_estado[self.x, self.y] != 6:
            for direccion in celdas_vecinas:
                if celdas_vecinas[direccion] == 5:
                    if not self.salida_emergencia:
                        if direccion == "izquierda":
                            print('EMERGENCIA izquierda')
                            self.salida_emergencia = True
                            nuevo_estado[self.x, self.y] = 0
                            nuevo_estado[self.x, self.y-1] = 9
                            self.actualizar_posicion(self.x, self.y-1)
                        elif direccion == "derecha":
                            print('EMERGENCIA derecha')
                            self.salida_emergencia = True
                            nuevo_estado[self.x, self.y] = 0
                            nuevo_estado[self.x, self.y+1] = 9
                            self.actualizar_posicion(self.x, self.y+1)
                        elif direccion == "arriba":
                            print('EMERGENCIA izquierda')
                            self.salida_emergencia = True
                            nuevo_estado[self.x, self.y] = 0
                            nuevo_estado[self.x-1, self.y] = 9
                            self.actualizar_posicion(self.x-1, self.y)
                            self.arriba(nuevo_estado)
                        elif direccion == "abajo":
                            print("EMERGENCIA abajo")
                            self.salida_emergencia = True
                            nuevo_estado[self.x, self.y] = 0
                            nuevo_estado[self.x+1, self.y] = 9
                            self.actualizar_posicion(self.x+1, self.y)
                            self.abajo(nuevo_estado)
                    else:
                        self.eleccion(direccion, nuevo_estado)

                elif celdas_vecinas[direccion] == 0: #or celdas_vecinas[direccion] == 2:  # espacio vacio o puerta
                    espacios_vacios.append(direccion)
                elif celdas_vecinas[direccion] == 1: #or celdas_vecinas[direccion] == 9:  # Pared o personas
                    continue

        if self.direccion_anterior == 'a':
            direccion_entre_ceros = random.choice(espacios_vacios)
        else:
            espacios_vacios.remove(self.volver())
            direccion_entre_ceros = random.choice(espacios_vacios)

        self.guardar_dirección_anterior(direccion_entre_ceros)

        self.eleccion(direccion_entre_ceros, nuevo_estado)

        espacios_vacios.clear()

    def volver(self):
        if self.direccion_anterior == 'izquierda':
            return 'derecha'
        elif self.direccion_anterior == 'derecha':
            return 'izquierda'
        elif self.direccion_anterior == 'arriba':
            return 'abajo'
        elif self.direccion_anterior == 'abajo':
            return 'arriba'

    def guardar_dirección_anterior(self, direccion):
        self.direccion_anterior = direccion

    # LLama al método que realiza el movimiento de acuerdo a la dirección
    def eleccion(self, direccion, nuevo_estado):
        if direccion == "izquierda":
            self.izquierda(nuevo_estado)
        elif direccion == "derecha":
            self.derecha(nuevo_estado)
        elif direccion == "arriba":
            self.arriba(nuevo_estado)
        elif direccion == "abajo":
            self.abajo(nuevo_estado)

    # Métodos de movimiento
    def izquierda(self, nuevo_estado):
        actual = nuevo_estado[self.x, self.y]
        proximo = nuevo_estado[self.x, self.y-1]
        nuevo_estado[self.x, self.y] = proximo
        nuevo_estado[self.x, self.y-1] = actual
        self.actualizar_posicion(self.x, self.y-1)

    def derecha(self, nuevo_estado):
        actual = nuevo_estado[self.x, self.y]
        proximo = nuevo_estado[self.x, self.y+1]
        nuevo_estado[self.x, self.y] = proximo
        nuevo_estado[self.x, self.y+1] = actual
        self.actualizar_posicion(self.x, self.y+1)

    def arriba(self, nuevo_estado):
        actual = nuevo_estado[self.x, self.y]
        proximo = nuevo_estado[self.x-1, self.y]
        nuevo_estado[self.x, self.y] = proximo
        nuevo_estado[self.x-1, self.y] = actual
        self.actualizar_posicion(self.x-1, self.y)

    def abajo(self, nuevo_estado):
        actual = nuevo_estado[self.x, self.y]
        proximo = nuevo_estado[self.x+1, self.y]
        nuevo_estado[self.x, self.y] = proximo
        nuevo_estado[self.x+1, self.y] = actual
        self.actualizar_posicion(self.x+1, self.y)

    def actualizar_posicion(self, x, y):
        self.x = x
        self.y = y
