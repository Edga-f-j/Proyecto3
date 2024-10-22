


import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3,4]
y = [1,3,9,16]


df = pd.read_csv("archivoss/poblacion.csv")

colombia = df["COL"]
arg = df["ARG"]
fecha = df["Date"]

print(arg)

# plt.plot(fecha,colombia, label='Colombia', color='blue', linestyle='--',linewidth=2)
# plt.plot(fecha,arg, label='Argentina', color='green', linestyle='-', linewidth=2)
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')

# plt.title('TITULO')
# plt.show()