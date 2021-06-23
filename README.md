## 🤓 BIENVENIDO AL GRUPO A 🤓

# Proyecto de investigación

## Integrantes

**Bustos Nahuel**

**Espinoza Maria Julia**

**Maya Pablo**

## Tema

**Simulación de fuego en edificio**

En base a esto se ha desarrollado un software escrito en python que considera distintas entidades como personas, paredes, espacios libres, zonas con fuego, salidas de emergencia y salidas.

Esperamos que esta aplicación sirva como punto de partida y complemento para el análisis de planes de evacuación ,diseño de espacios en edificios y salidas de emergencia. 

## Marco teórico

El proyecto trata de una simulación de evacuación en un edificio mientras el mismo se incendia, esto sirve para obtener una visión más cercana a la realidad sobre el desempeño de la infraestructura del edificio y de los elementos de seguridad que contiene para su plan de evacuación. A partir de esta simulación se obtienen datos sobre los posibles muertos, heridos y salvados. Con lo cual podemos tomar en cuenta si el edificio necesitará algún tipo de modificación, para volverlo más seguro.


Nuestro marco está definido por las siguientes normativas:

[Evacuación de edificios](https://www.insst.es/documents/94886/326853/ntp_046.pdf/b9d7dd31-9758-42a1-8c8c-55daa88295f2)

[Cálculo estimativo de vías y tiempos de evacuación](https://www.cso.go.cr/legislacion/notas_tecnicas_preventivas_insht/NTP%20436%20-%20Calculo%20estimativo%20de%20vias%20y%20tiempos%20de%20evacuacion.pdf)

## Tecnologías


El proyecto fue desarrollado íntegramente en el lenguaje Python haciendo uso de VSCode como entorno de desarrollo. También se utilizó herramientas en el entorno de desarrollo como live share, esta herramienta se utiliza para realizar modificaciones en el código de manera colaborativa. Una persona comparte un archivo de código y el resto, con el permiso del anfitrión, puede hacer modificaciones.
Otra de las herramientas utilizadas es PyQt designer, con la que se creó la interfaz gráfica en la que el usuario busca la reqweuta del escenario a probar en la simulación y demás botones que se muestran en el apéndice.  


## Requerimientos previos

Para poder ejecutar el programa se debe contar con el siguiente software y librerías instaladas en el sistema:

- Python 3
- numpy
- PyQt5
- pygame

## Funcionamiento

Al momento de ejecutar el programa, el usuario tendrá la oportunidad de elegir dónde correr la simulación entre una serie de escenarios comunes como lo son casas, oficinas o escuelas. Pudiendo también ingresar su propio escenario.  También tendrá control sobre la cantidad de personas dentro del edificio al momento del incendio ya que podrá cargar previamente a cada persona en su escenario.
Al final de la ejecución se presenta un resultado indicando cuántas de las personas que se encontraban en el edificio pudieron salvarse ilesas, terminaron salvadas heridas o muertas.


## Creación de escenario

Este archivo debe ser extensión .txt (Para que luego pueda abrirse en la interfaz gráfica).

Para crear una escenario se debe utilizar una matriz de números en la que cada número es la representación de una pared, una persona, el fuego, la línea señalizada de salida de emergencia y la salida del edificio.
Significado para cada número:
        0 = Espacio vacío
        1 = Pared 
        5 = Línea señalizada de salida de emergencia 
        6 = Salida
        7 = Fuego Activo  
        9 = Persona

Cuando cree su matriz debe incorporar a las personas que desee que estén en el edificio y en donde considera que se inicia el fuego.
Como así también que debe dibujarse todo el borde de la matriz con 2 que implica el contorno de la matriz de números, no olvide que debe dibujar cada pared del edificio tanto interna como externa.

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

También debe tenerse en cuenta que solo admite matrices cuadradas o rectangulares.
Matriz cuadrada implica que tiene la misma cantidad de columnas y la misma cantidad de filas. 

                Ejemplo: Matriz cuadrada de 4X4 (4 Filas x 4 Columnas)
                
                                    (1,1,1,1),
                                    (1,0,0,0),
                                    (1,0,0,1),
                                    (1,1,1,1),

Matriz rectangular implica que tiene cierta cantidad de filas y cierta cantidad de columnas, pero esto es así en toda la matriz.

                Ejemplo: Matriz Rectangular de 4X6 (4 Filas X 6 Columnas)

                                    (1,1,1,1,1,1),
                                    (1,0,0,0,0,0),
                                    (1,0,0,1,0,0),
                                    (1,1,1,1,0,0),

Las matrices que varían la cantidad de filas o columnas no son válidas.

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

