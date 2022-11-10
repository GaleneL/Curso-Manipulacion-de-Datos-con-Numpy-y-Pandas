'''
Asunto: Explorar la funcionalidad de loc e iloc dentro de pandas, los cuales son utilizados para
hacer consultas más especializadas
'''
import pandas as pd

# Leer archivo csv devolviendo un dataframe
csvFile = pd.read_csv('./bestsellers with categories.csv', sep=',', header = 0)
print(csvFile.columns)

print('.'*25+'\n', csvFile[0:4]) # Las operaciones de slicing son válidas
print('.'*25+'\n', csvFile['Name']) # Muestra una serie de la columna Name
print('.'*25+'\n', csvFile[['Name','Author']]) # Puedo obtener un sub dataframe
print('.'*25+'\n', csvFile.loc[0:4,['Name','Author']]) # Otra forma de hacer slicing con opciones especializadas
print('.'*25+'\n', csvFile.loc[:,['Reviews']]*-1) # Otro ejemplo donde consulto todos los datos de la columna
# Reviews y a cada dato lo multiplico por -1
print('.'*25+'\n', csvFile.loc[:,['Author']]=='JJ Smith') # Condicionales devolviendo una serie booleana de True o False


# Iloc hace consultas con los índices, en este caso solicitamos todas las filas pero con las columnas
# de la 0 a la 2
print('.'*25+'\n',csvFile.iloc[:, 0:3])
print('.'*25+'\n', csvFile.iloc[1,3])