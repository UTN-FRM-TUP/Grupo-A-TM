""" Este módulo contiene todas las funciones que realizan el movimiento """

# Devuelve la direccion que no debe volver a tomar
def volver(direccion_anterior):
        if direccion_anterior == 'izquierda':
            return 'derecha'
        elif direccion_anterior == 'derecha':
            return 'izquierda'
        elif direccion_anterior == 'arriba':
            return 'abajo'
        elif direccion_anterior == 'abajo':
            return 'arriba'

# Métodos que realizan el movimiento
def izquierda(x, y, nuevo_estado, valor_anterior):
        actual = nuevo_estado[x, y]
        proximo = nuevo_estado[x, y-1]
        if proximo != 6:
            valor_anterior = proximo
        nuevo_estado[x, y] = proximo
        nuevo_estado[x, y-1] = actual
        return(x, y-1)


def derecha(x, y, nuevo_estado, valor_anterior):
        actual = nuevo_estado[x, y]
        proximo = nuevo_estado[x, y+1]
        if proximo != 6:
            valor_anterior = proximo
        nuevo_estado[x, y] = proximo
        nuevo_estado[x, y+1] = actual
        return(x, y+1)

def arriba(x, y, nuevo_estado, valor_anterior):
        actual = nuevo_estado[x, y]
        proximo = nuevo_estado[x-1, y]
        if proximo != 6:
            valor_anterior = proximo
        nuevo_estado[x, y] = proximo
        nuevo_estado[x-1, y] = actual
        return(x-1, y)

def abajo(x, y, nuevo_estado, valor_anterior):
        actual = nuevo_estado[x, y]
        proximo = nuevo_estado[x+1, y]
        if proximo != 6:
            valor_anterior = proximo
        nuevo_estado[x, y] = proximo
        nuevo_estado[x+1, y] = actual
        return(x+1, y)
        

        
