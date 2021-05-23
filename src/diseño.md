# Diseño 13/05/2021
Archivo = input(ruta/al/archivo)

with open(archivo, 'r') as f:
    f.readlines()

    . = Espacio vacio
    # = Pared 
    2 = Puerta abierta 
    3 = Puerta cerrada
    4 = Mata fuego
    - = Linea de salida de emergencia 
    6 = Salida
    7 = Fuego Activo
    8 = Fuego apagado
    9 = Persona

     
## Clase Persona -> 
solo se mueve de (Izq,Der,Arr,Aba), si llega al "-" sigue esa linea hasta la salida (6), ver el tema del movimiento??
        tiene que evaluar si es "." o "-" y elige "-" SIEMPRE.
        Si tiene fuego al lado no se mueve en esa posición. 
        Si tiene una persona en esa posición se mueve a otro lado.
        Si la puerta esta cerrada no puede pasarla.

      cantidad_personas = input()


   ### Metodos
   mover():
      evaluar_Celda_vecinas()
      movimiento
      posicion = 9
      posicion_ant = . o -


   evaluar_posicion():
      si es 6 
      cantidad_personas --
      cantidad_personas == 0
         pygem.quit()
         sys.exit()
        
   - Clase Niño (Hereda de persona) "panico"
   - Clase Adulto (Hereda de persona) "panico"

## Clase Fuego -> 
posicion aleatoria (Iz,Der,Arr,Aba),se tiene que propagar - Ver el tema del time? o como propagar?
si tiene fuego al lado no se mueve en esa posición.

aspersores boolean = True
intensidad int 0 - 100
 si intensidad == 0  7 => 8

   ### Metodos
   propagar():
      evaluar_Celda_vecinas()
      propaga
      posicion = 7
       
   evaluar_intensidad()

import time
tm_sec: segundos 

### Ejemplo matriz
[  
 (1, 1, 1, 1, 1, 1, 1, 1),
 (1, 5, 2, 0, 0, 1, 0, 1),
 (1, 5, 1, 0, 0, 1, 0, 2),
 (1, 5, 1, 1, 1, 1, 0, 1),
 (1, 5, 5, 0, 0, 0, 0, 1),
 (1, 1, 6, 1, 1, 1, 1, 1),
]

si panico <= 80 
   evalua movimiento
sino
   movimiento = random
