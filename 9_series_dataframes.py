'''
Asunto: Explorar las series y dataframes que ofrece la librería de pandas
'''
import pandas as pd

# Crea una estructura de datos conocida como serie de pandas la cual se le
# pueden colocar los índices deseados a cada valor
serie = pd.Series(["Navas",'Messi','Neymar','Bicho'], index= [1,7,10,30])
print(serie)

# Se puede crear una serie a partir de un diccionario
myDict = {1:'Navas', 2:'Messi', 3:'Neymar', 4:'Bicho'}
mySerie = pd.Series(myDict)
print(mySerie)
# Aquí no hay posición 0, ya que se empieza por el índice 1 o el colocado

# En caso de tener más de una dimensión, es decir más que solo un array
# se utilizan los dataframe de pandas
# El dataframe es la estructura principal de pandas
otherDict = {'Jugador':["Navas",'Messi','Neymar','Bicho'],
'Altura':[183.0, 170.0, 170.0, 165.0],
'Goles': [2, 200, 200, 200]}

df = pd.DataFrame(otherDict)
print('.'*30)
print(df)
print(df.columns)
print(df.index)