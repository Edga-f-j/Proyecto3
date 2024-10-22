import pandas as pd
import matplotlib.pyplot as plt


# import os
# print(os.getcwd())

# import os
# print(os.getcwd())


# lista = [1,2,3,4,5,6,7,8,9]

# print(lista)
# #crear una serie
# mi_serie = pd.Series(lista)
df = pd.read_csv("archivoss/poblacion.csv")

# # Mostrar el DataFrame
# print(df.head())
# print(df[["Date","COL","ARG"]].mean)

colombia = df["COL"]
#print(colombia.mean()) # para colcoar la media de toda la columna

# filtra que la poblacion sea mayor a 30 millones
# filtrar = df[colombia>30000000]
# print(filtrar["ARG"])



#eliminar columnas
# ElmFra = df.drop(columns=['FRA'])
# print(ElmFra)
df.plot(x='Date', y='CHN', figsize=(10, 6))
plt.show()