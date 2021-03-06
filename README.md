## 馃 BIENVENIDO AL GRUPO A 馃

# Proyecto de investigaci贸n

## Integrantes

**Bustos Nahuel**

**Espinoza Maria Julia**

**Maya Pablo**

## Tema

**Simulaci贸n de fuego en edificio**

En base a esto se ha desarrollado un software escrito en python que considera distintas entidades como personas, paredes, espacios libres, zonas con fuego, salidas de emergencia y salidas.

Esperamos que esta aplicaci贸n sirva como punto de partida y complemento para el an谩lisis de planes de evacuaci贸n ,dise帽o de espacios en edificios y salidas de emergencia. 

## Marco te贸rico

El proyecto trata de una simulaci贸n de evacuaci贸n en un edificio mientras el mismo se incendia, esto sirve para obtener una visi贸n m谩s cercana a la realidad sobre el desempe帽o de la infraestructura del edificio y de los elementos de seguridad que contiene para su plan de evacuaci贸n. A partir de esta simulaci贸n se obtienen datos sobre los posibles muertos, heridos y salvados. Con lo cual podemos tomar en cuenta si el edificio necesitar谩 alg煤n tipo de modificaci贸n, para volverlo m谩s seguro.


Nuestro marco est谩 definido por las siguientes normativas:

[Evacuaci贸n de edificios](https://www.insst.es/documents/94886/326853/ntp_046.pdf/b9d7dd31-9758-42a1-8c8c-55daa88295f2)

[C谩lculo estimativo de v铆as y tiempos de evacuaci贸n](https://www.cso.go.cr/legislacion/notas_tecnicas_preventivas_insht/NTP%20436%20-%20Calculo%20estimativo%20de%20vias%20y%20tiempos%20de%20evacuacion.pdf)

## Tecnolog铆as


El proyecto fue desarrollado 铆ntegramente en el lenguaje Python haciendo uso de VSCode como entorno de desarrollo. Tambi茅n se utiliz贸 herramientas en el entorno de desarrollo como live share, esta herramienta se utiliza para realizar modificaciones en el c贸digo de manera colaborativa. Una persona comparte un archivo de c贸digo y el resto, con el permiso del anfitri贸n, puede hacer modificaciones.
Otra de las herramientas utilizadas es PyQt designer, con la que se cre贸 la interfaz gr谩fica en la que el usuario busca la reqweuta del escenario a probar en la simulaci贸n y dem谩s botones que se muestran en el ap茅ndice.  


## Requerimientos previos

Para poder ejecutar el programa se debe contar con el siguiente software y librer铆as instaladas en el sistema:

- Python 3
- numpy
- PyQt5
- pygame

## Funcionamiento

Al momento de ejecutar el programa, el usuario tendr谩 la oportunidad de elegir d贸nde correr la simulaci贸n entre una serie de escenarios comunes como lo son casas, oficinas o escuelas. Pudiendo tambi茅n ingresar su propio escenario.  Tambi茅n tendr谩 control sobre la cantidad de personas dentro del edificio al momento del incendio ya que podr谩 cargar previamente a cada persona en su escenario.
Al final de la ejecuci贸n se presenta un resultado indicando cu谩ntas de las personas que se encontraban en el edificio pudieron salvarse ilesas, terminaron salvadas heridas o muertas.


## Creaci贸n de escenario

Este archivo debe ser extensi贸n .txt (Para que luego pueda abrirse en la interfaz gr谩fica).

Para crear una escenario se debe utilizar una matriz de n煤meros en la que cada n煤mero es la representaci贸n de una pared, una persona, el fuego, la l铆nea se帽alizada de salida de emergencia y la salida del edificio.
Significado para cada n煤mero:
        0 = Espacio vac铆o
        1 = Pared 
        5 = L铆nea se帽alizada de salida de emergencia 
        6 = Salida
        7 = Fuego Activo  
        9 = Persona

Cuando cree su matriz debe incorporar a las personas que desee que est茅n en el edificio y en donde considera que se inicia el fuego.
Como as铆 tambi茅n que debe dibujarse todo el borde de la matriz con 2 que implica el contorno de la matriz de n煤meros, no olvide que debe dibujar cada pared del edificio tanto interna como externa.

				Ejemplo de escenario:
                            (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,1,1),
                            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,0,0,0,9,0,0,1,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1),
                            (1,1,1,1,1,1,0,5,5,5,5,5,5,5,5,5,0,1,1,1,1,1,1),
                            (1,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,0,0,1),
                            (1,0,0,0,9,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,0,0,1),
                            (1,1,1,1,1,1,0,0,0,0,0,5,0,0,0,0,0,1,1,1,1,1,1),
                            (1,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,5,0,0,9,0,0,1,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,0,0,1),
                            (1,1,1,1,1,1,0,0,0,0,0,5,0,0,0,0,0,1,1,1,1,1,1),
                            (1,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,0,0,1),
                            (1,0,0,0,0,1,0,0,0,0,0,5,0,0,0,0,0,1,0,0,0,0,1),
                            (1,1,1,1,1,1,1,1,1,1,6,6,6,1,1,1,1,1,1,1,1,1,1),

Tambi茅n debe tenerse en cuenta que solo admite matrices cuadradas o rectangulares.
Matriz cuadrada implica que tiene la misma cantidad de columnas y la misma cantidad de filas. 

                Ejemplo: Matriz cuadrada de 4X4 (4 Filas x 4 Columnas)
                
                                    (1,1,1,1),
                                    (1,0,0,0),
                                    (1,0,0,1),
                                    (1,1,1,1),

Matriz rectangular implica que tiene cierta cantidad de filas y cierta cantidad de columnas, pero esto es as铆 en toda la matriz.

                Ejemplo: Matriz Rectangular de 4X6 (4 Filas X 6 Columnas)

                                    (1,1,1,1,1,1),
                                    (1,0,0,0,0,0),
                                    (1,0,0,1,0,0),
                                    (1,1,1,1,0,0),

Las matrices que var铆an la cantidad de filas o columnas no son v谩lidas.

				Ejemplo:
						(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
						(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
						(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),

