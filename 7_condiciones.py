'''
Asunto: Explorar condicionales dentro de arreglos de numpy
'''
import numpy as np

arr = np.linspace(1,10,10, dtype='int8')

# Se aplica la condicional a cada elemento de la lista devolviendo una lista
# booleana
index_cond = arr > 5
print(index_cond)

# Si utilizamos el arreglo condicional como entrada de un arreglo, solo
# devolverá los valores que cumplan con la condición: True
print(arr[index_cond])

# Podemos crear acciones con estos condicionales
arr[arr>5] = 99 # Todos los elementos mayores a 5 cambialos por 99
print(arr)


