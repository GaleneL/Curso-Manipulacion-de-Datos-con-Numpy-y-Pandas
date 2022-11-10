'''
Asunto: Exploración de la función copy para arreglos en numpy
'''
import numpy as np

arr = np.arange(0,11)
arr_piece = arr[0:6] # Se crea un array a partir de otro

arr_piece[:] = 0 # Al modificar la pieza de arreglo se modifica también el arreglo
# original, este es un problema a tener mucho en cuenta ya que hace referencia al
# objeto en memoria, no crea un nuevo objeto
print(arr_piece)
print(arr)

arr2 = np.arange(0,11)
arr_piece2 = arr2.copy() # Se crea un array a partir de otro pero con la función copy
arr_piece2[:] = 100
print(arr_piece2)
print(arr2) # La lista original es respetada ya que son objetos totalmente
# diferentes
