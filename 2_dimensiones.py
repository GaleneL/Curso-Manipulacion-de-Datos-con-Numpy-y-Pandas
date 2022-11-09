'''
Asunto: Explorar las distintas dimensiones que pueden tener las variables de
numpy
'''
import numpy as np

# valor con dimensión 0
scalar = np.array(42)
print(scalar)
print(scalar.ndim)
print('.'*20)

# valor con 1 dimensión
vector = np.array([1,2,3,4])
print(vector)
print(vector.ndim)
print('.'*20)

# valor con 2 dimensiones
matriz = np.array([[1,2,3,4],[5,4,6,7],[4,8,6,1]])
print(matriz)
print(matriz.ndim)
print('.'*20)

# valor con 3 dimensiones
tensor = np.array([ [[1,2,3,4],[5,4,6,7],[4,8,6,1]],[[1,2,3,4],[5,4,6,7],[4,8,6,1]] ])
print(tensor)
print(tensor.ndim)
print('.'*20)

# Agregando dimensiones
tensor10 = np.array([1,2,3], ndmin=10)
print(tensor10)
print(tensor10.ndim)
print('.'*20)

# Expandir las dimensiones de un objeto
expand = np.expand_dims(np.array([1,2,3]), axis = 0) # Expandir una dimensión en las filas:0
print(expand)
print(expand.ndim)
print('.'*20)

# Eliminar dimensiones que no estoy usando
dismish = np.squeeze(tensor10)
print(dismish)
print(dismish.ndim)