'''
Asunto: Explorar la lectura de archivos csv y json con pandas
'''
import pandas as pd

# Leer archivo csv devolviendo un dataframe
csvFile = pd.read_csv('./bestsellers with categories.csv', sep=',', header = 0)
print(csvFile)
print(csvFile.columns)

# Leer archivo csv devolviendo un dataframe
jsonFile = pd.read_json('./HPCharactersDataRaw.json')
print(jsonFile)
print(jsonFile.columns)

# Leer archivo csv devolviendo una serie
jsonSerie = pd.read_json('./HPCharactersDataRaw.json', typ='Series')
print(jsonSerie)