'''
Asunto: Explorar distintas formas de generar un arreglo numpy

'''

import numpy as np

print(list(range(0,10))) # lista de python
print(np.arange(0,20,2)) # numpy array con valores enlistados de 2 en 2
print(np.zeros( (3,3) ) ) # array compuesto por 0
print(np.ones(5)) # array compuesto por 1
print(np.linspace(0,10,20)) # Crea un array con un valor de inicio, un valor final y
# cuántos datos se quieren generar que vayan del número inicial al final por medio
# de una distribución
print(np.eye(4)) # Crea una matriz diagonal de 4x4
print(np.random.rand(2,4)) # valor aleatorio entre 0 y 1
print(np.random.randint(1,200,(10,10))) # una matriz de 10x10 con número aleatorios del 1 al 200
