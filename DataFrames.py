import pandas as pd

datos = {"nombre": ["Alice", "Bob", "Charlie"],
         "edad": [25, 30, 35],
         "Ciudad": ["A", "B", "C"]}

df = pd.DataFrame(datos)
print(df)