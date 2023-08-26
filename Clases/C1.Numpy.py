#Ir a Settings, Proyect, Python Interpreter, Click en simbolo de anaconda, Ir al "+", Instalar "numpy" y "pandas".

import numpy as np

#LISTA DE UNA DIMENSION
l = [1,2,3,4,5]

#TRANSFORMAR CUALQUIER LISTA A UNA LISTA NP.ARRAY
n1 = np.array(l)
print(n1)

#Verificar el tipo de dato de n1 que sea np.array.
print(type(n1))


#PRINCIPALES ATRIBUTOS/FUNCIONES DE LAS LISTAS NP.ARRAY
#Imprime las dimensiones del arreglo.
print(n1.ndim)
#Devuelve la cantidad de datos y la dimensiones que tiene en forma de tupla.
print(n1.shape)
#Devuelve la cantidad de elementos TOTAL que hay dentro.
print(n1.size)
#Devuelve el tipo de dato que hay dentro.
print(n1.dtype)

#LISTA CON DOS DIMENSIONES
#Las listas de dos dimensiones o mas deben de contener la misma cantidad de datos.
m = [[1,2,3,4,5], [6,7,8,9,10]]
n2 = np.array(m)
print(type(n2))

#PRINCIPALES FUNCIONES
print(n2.ndim)
print(n2.shape)
print(n2.size)
print(n2.dtype)


#ACCESO A LOS ELEMENTOS EN UNA LISTA BIDIMENSIONAL.
#Primero va la fila o el renglon y luego la columna. Y se empieza desde le 0.
print(n2[1,2])

#ALGUNAS OPERACIONES MATEMATICAS QUE SE PUEDEN HACER.
#Multiplicacion
print(n2 * 2)
#Sacar el promedio de los datos.
print(n2.mean())
#Sacar el promedio de la fila "x" con todos los datos de la columna.
print(n2[0, :].mean())
#Sacar el promedio de la columna "x" con todos los datos de la fila.
print(n2[:, 2].mean())
#Ejemplo de una operacion de algebra lineal.
print(np.linalg.norm(n2))
#Transpuesta: Convertir la fila a columna y la columna  a fila.
print(n2.transpose())

#Resolver Ecuaciones

"""
Ecuacion: 
X + 2y = 1
3x + 5y = 2

"""
#Pasar cada linea de ecuacion a una lista cada una.
ecuaciones = [[1, 2], [3, 5]]
#Covertir a lista np.array
np_ecuaciones = np.array(ecuaciones)

resultado = np.array([1, 2])
print(np.linalg.solve(np_ecuaciones, resultado))


