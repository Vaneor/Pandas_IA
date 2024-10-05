import pandas as pd
datos = {'Nombre': ['Alice', 'Bob', 'Charlie'],
         'Edad': [25, 30, 35],
         'Ciudad': ['A', 'B', 'C']}
df = pd.DataFrame(datos, index=['a', 'b', 'c'])
print(df)
#Seleccionar datos con loc[] # multiples valores    
seleccion_loc = df.loc['b', 'Edad'] 
print(seleccion_loc)
#Seleccionar datos con iloc[]
seleccionar_iloc = df.iloc[1, 1]
print(seleccionar_iloc)
#Seleccionar datos con at[] #si solo necesitaramos un valor
seleccion_at = df.at['b', 'Edad']
print(seleccion_at)
#Seleccionar datos con iat[]
seleccion_iat = df.iat[1, 1]
print(seleccion_iat)