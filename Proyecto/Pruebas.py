import numpy as np

a = np.array([
    [1,2,3,4], 
    [3,6,3,2], 
    [1,2,5,3]
])

for x,y in zip(*np.where(a==3)):
    
 
  x= x
  y= y
  print(x, y)


  


"""
celdas_vecinas = {
            'izquierda': 5,
            'derecha': 0 ,
            'arriba': 1 ,
            'abajo': 1
}
for clave  in celdas_vecinas:
  if celdas_vecinas[clave] == 5 :
    if clave == "izquierda":
        print("izquierda")
      
      """


    