'''
Asunto: Se exploran las funciones de shape y reshape para cambiar la forma
de un array con numpy
'''
import numpy as np

arr = np.random.randint(1,10,(3,2))
print(arr)
print('Shape: ',arr.shape) # Me devuelve las dimensiones filasxcolumnas de un array
print(arr.reshape(1,6), '.'*10) # Transforma el shape de un array adecuandolo a una forma

arr2 = np.random.randint(1,10,(3,2))
print(arr2,'.'*20)
# Si queremos que haga un reshape como se hace en lenguaje C, es decir tomando filas
print(np.reshape(arr2,(2,3),'C'))
# Si queremos que haga un reshape como se hace en lenguaje Fortran, es decir tomando columnas
print(np.reshape(arr2,(2,3),'F'))
# Si queremos que haga un reshape cuidando la optimización de la computadora
print(np.reshape(arr2,(2,3),'A'))
