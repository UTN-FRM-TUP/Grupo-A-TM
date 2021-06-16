""" Clase que genera objetos persona """

import random


class Persona():

    def __init__(self, ide, estado, x, y):
        self.ide = ide
        self.estado = estado
        self.x = x
        self.y = y
        self.direccion_anterior = 'a'
        self.muerto = False
        self.herido = False
        self.salvado = False

        # Variable bandera para controlar el ingreso a un camino de emergencia
        self.salida_emergencia = True

    def evalua_celda_vecina(self, nuevo_estado):
        celdas_vecinas = {}
        celdas_vecinas.update({'derecha': nuevo_estado[self.x, self.y+1]})
        if self.x+1 != 21:
            celdas_vecinas.update({'abajo': nuevo_estado[self.x+1, self.y]})
        celdas_vecinas.update({'izquierda': nuevo_estado[self.x, self.y-1]})
        celdas_vecinas.update({'arriba': nuevo_estado[self.x-1, self.y]})
        return celdas_vecinas

    def elegir_direccion(self, nuevo_estado, celdas_vecinas):

        celdas_validas = []
        camino = []        
        movimiento = False
        
        for direccion in celdas_vecinas:

            # Camino de salida de emergencia
            if celdas_vecinas[direccion] == 6:
                self.salvado = True
            elif celdas_vecinas[direccion] == 5:
                camino.append(direccion)
                if self.salida_emergencia:
                    movimiento = True
                    self.ingreso_camino_emergencia(
                        nuevo_estado, direccion)

            # Espacio vacio o puerta
            elif celdas_vecinas[direccion] == 0 or (
                    celdas_vecinas[direccion] == 2):
                celdas_validas.append(direccion)

            # Pared o personas
            elif celdas_vecinas[direccion] == 1 or (
                    celdas_vecinas[direccion] == 9):
                continue

        # Se ejecuta cuando está dentro de un camino de emergencia
        if len(camino) > 0 and movimiento == False:
            # Comprueba que no sea un final de camino
            if len(camino) > 1:
                camino.remove(self.volver())
            direccion_entre_ceros = random.choice(camino)

            self.guardar_dirección_anterior(direccion_entre_ceros)

            self.eleccion(direccion_entre_ceros, nuevo_estado)

            camino.clear()
        # Si no es un camino de emergencia
        else:
            if self.direccion_anterior == 'a':
                direccion_entre_ceros = random.choice(celdas_validas)
            else:
                celdas_validas.remove(self.volver())
                direccion_entre_ceros = random.choice(celdas_validas)

            self.guardar_dirección_anterior(direccion_entre_ceros)

            self.eleccion(direccion_entre_ceros, nuevo_estado)

            celdas_validas.clear()

    def ingreso_camino_emergencia(self, nuevo_estado, direccion):
        if direccion == "izquierda":
            print('EMERGENCIA izquierda')
            # Se mueve a la izquierda
            nuevo_estado[self.x, self.y] = 0
            nuevo_estado[self.x, self.y-1] = 9
            self.salida_emergencia = False
            self.actualizar_posicion(self.x, self.y-1)
            self.direccion_anterior = "izquierda"
        elif direccion == "derecha":
            print('EMERGENCIA derecha')
            # Se mueve a la derecha
            nuevo_estado[self.x, self.y] = 0
            nuevo_estado[self.x, self.y+1] = 9
            self.salida_emergencia = False
            self.actualizar_posicion(self.x, self.y+1)
            self.direccion_anterior = "derecha"
        elif direccion == "arriba":
            print('EMERGENCIA arriba')
            # Se mueve hacia arriba
            nuevo_estado[self.x, self.y] = 0
            nuevo_estado[self.x-1, self.y] = 9
            self.salida_emergencia = False
            self.actualizar_posicion(self.x-1, self.y)
            self.direccion_anterior = "arriba"
        elif direccion == "abajo":
            print("EMERGENCIA abajo")
            # Se mueve hacia abajo
            nuevo_estado[self.x, self.y] = 0
            nuevo_estado[self.x+1, self.y] = 9
            self.salida_emergencia = False
            self.actualizar_posicion(self.x+1, self.y)
            self.direccion_anterior = "abajo"

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
