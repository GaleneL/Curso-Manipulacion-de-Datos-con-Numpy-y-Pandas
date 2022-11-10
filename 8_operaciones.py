'''
Asunto: Explorar distintas operaciones matemáticas realizadas entre
arreglos y matrices de numpy
'''
import numpy as np

lista = [1,2]
print(lista*2) # En este caso la lista de python interpreta que quiero
# duplicar los valores de la lista

arr = np.array([1,2,3])
arr2 = np.array([4,5,6])
mat = np.array([[1,2,3],[4,5,6]])

print(arr*2) # El array de numpy interpreta que multiplica cada valor
# por 2 lo cual es más eficiente
print(arr+2)
print(1/arr)
print(arr**2)
print(arr+arr2) # elemento con elemento
print(mat*arr.T, '.'*20) # no sigue la regla del producto entre matrices necesariamente
print(mat.shape)
print(arr.shape)
new_array = np.matmul(mat, arr) # producto matricial
# mat @ arr tiene el mismo resultado
print(new_array)
print(new_array.shape)