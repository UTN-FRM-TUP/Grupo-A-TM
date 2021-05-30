def mover(estado, x, y):
    estado = elegir_direccion(evalua_celda_vecina(estado, x, y), estado, x, y)
    return estado


def evalua_celda_vecina(estado, x, y):
    celdas_vecinas = {}
    if not len(estado[x]) or not len(estado):
        celdas_vecinas.update({"abajo": estado[x+1, y]})
        celdas_vecinas.update({"arriba": estado[x-1, y]})
        celdas_vecinas.update({"izquierda": estado[x, y-1]})
        celdas_vecinas.update({"derecha": estado[x, y+1]})
    return celdas_vecinas


def elegir_direccion(celdas_vecinas, estado, x, y):
    direccion_anterior = 'izquierda'

    for direccion in celdas_vecinas:
        if celdas_vecinas[direccion] == 6:  # salida
            continue
        elif celdas_vecinas[direccion] == 5:  # salida de emergencia
            estado = eleccion(direccion, estado, x, y)
            direccion_anterior = direccion
        elif celdas_vecinas[direccion] == 0:  # espacio vacio
            estado = eleccion(direccion, estado, x, y)
            direccion_anterior = direccion
        elif celdas_vecinas[direccion] == 2:    # Puerta abierta
            estado = eleccion(direccion, estado, x, y)
            direccion_anterior = direccion
        elif celdas_vecinas[direccion] == 8:    # fuego apagado
            estado = eleccion(direccion, estado, x, y)
            direccion_anterior = direccion
        elif celdas_vecinas[direccion] == 7:    # Fuego activo
            # condicion = 'herido'
            estado = volver(direccion_anterior, estado, x, y)
        else:
            estado = volver(direccion_anterior, estado, x, y)
    return estado


def volver(direccion, estado, x, y):
    if direccion == "izquierda":
        estado = derecha(estado, x, y)
    if direccion == "derecha":
        estado = izquierda(estado, x, y)
    if direccion == "arriba":
        estado = arriba(estado, x, y)
    if direccion == "abajo":
        estado = arriba(estado, x, y)
    return estado


def eleccion(direccion, estado, x, y):
    if direccion == "izquierda":
        estado = izquierda(estado, x, y)
    if direccion == "derecha":
        estado = derecha(estado, x, y)
    if direccion == "arriba":
        estado = arriba(estado, x, y)
    if direccion == "abajo":
        estado = abajo(estado, x, y)
    return estado


def izquierda(estado, x, y):
    estado[x, y] = estado[x, y-1]
    estado[x, y-1] = 9
    return estado


def derecha(estado, x, y):
    estado[x, y] = estado[x, y+1]
    estado[x, y+1] = 9
    return estado


def arriba(estado, x, y):
    estado[x, y] = estado[x-1, y]
    estado[x-1, y] = 9
    return estado


def abajo(estado, x, y):
    estado[x, y] = estado[x+1, y]
    estado[x+1, y] = 9
    return estado


def izquierda(estado, x, y):
    actual = estado[x, y]
    proxima = estado[x, y-1]
    estado[x, y] = proxima
    estado[x, y-1] = actual
    # return estado


def derecha(estado, x, y):
    actual = estado[x, y]
    proximo = estado[x, y+1]
    estado[x, y] = proximo
    estado[x, y+1] = actual
    # return estado


def arriba(estado, x, y):
    actual = estado[x, y]
    proximo = estado[x-1, y]
    estado[x-1, y] = actual
    estado[x, y] = proximo
    # return estado


def abajo(estado, x, y):
    actual = estado[x, y]
    proximo = estado[x+1, y]
    estado[x+1, y] = actual
    estado[x, y] = proximo
    # return estado