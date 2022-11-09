'''
Explorar algunas de las funciones más importantes y útiles en la librería de numpy
'''

import numpy as np

arr = np.random.randint(1,20,10)
matriz = arr.reshape(2,5)
print(matriz)

print( 'Max: ',arr.max() ) # Trae el número más grande dentro de un array
print( 'Min: ',arr.min() ) # Trae el número más pequeño dentro de un array
print( 'Max eje 1: ',matriz.max(1) ) # Trae los valores máximos por eje, en este caso el eje 1,
# es decir, devuelve un array con los valores máximos de cada fila o columna
print( 'Argmax: ',matriz.argmax(1) ) # Devuelve el índice del valor máximo de un array
print( 'Ptp: ',arr.ptp() ) # Pick to pick devuelve la diferencia entre el valor más pequeño 
# y más alto de un arreglo mostrando la distancia de valores
arr.sort() # Ordena de mayor a menor los valores de un arreglo
print( 'Sort: ',arr ) 
print( 'Percentile: ',np.percentile(arr,50) ) # Especifica el percentil en el que estoy trabajando
# El percentil 0 sería el número más bajo, el percentil 100 el más alto y el 50 el del medio o la mediana
print( 'Mediana: ',np.median(arr) ) # Mediana de un arreglo
print( 'Std: ', np.std(arr)) # Desviación estándar de un arreglo
print( 'Var: ', np.var(arr)) # Variancia de un arreglo
print( 'Media: ', np.mean(arr)) # Media o promedio de un arreglo
a = np.array([[1,2],[3,4]])
b = np.array([5,6])
b = np.expand_dims(b, axis=0)
print( 'Concatenate: ', np.concatenate((a,b),axis = 0))
print( 'Concatenate Transpose: ', np.concatenate((a,b.T),axis=1)) 