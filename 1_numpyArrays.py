'''
Asunto: Exploración de los arreglos con la librería numpy

Un array de numpy es incluso 50 veces más rápido que una lista de python o c
El array de numpy solo puede tener un único tipo de dato
'''
import numpy as np

# Crear un array numpy desde una lista de python
lista = [1,2,3,4,5,6,7,8,9]
listaNp = np.array(lista)

# Crear una matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matNp = np.array(matriz)

# Indexado de array numpy
print(matNp[1]) # Devuelve la segunda fila de la matriz
print(matNp[0][1]) # Devuelve el elemento '2' ubicado en la fila 0, columna 1
print(listaNp[1:4]) # Devuelve los valores de la lista Np con índice 1 al 4
print(listaNp[::3]) # Devuelve todo el arreglo seleccionando valores de 3 en 3
print(listaNp[::-1]) # Invertir un arreglo
print(matNp[1:,0:2]) # Devuelve los valores de fila empezando por índice 1,
# y columnas del índice 0 a 2

# Tipos de datos numpy
print(listaNp.dtype) # Imprime el tipo de dato que contiene el array, en este caso int32

arrNp = np.array([1,2,3,4,5], dtype='float64') # Restringe un tipo de dato para el array
print(arrNp.dtype)

arrNp2 = np.array([0,1,2,3,4,5])
arrNp2 = arrNp2.astype(np.bool_) # Cambia el tipo de dato de un array y lo asigna a otra variable
print(arrNp2.dtype)
