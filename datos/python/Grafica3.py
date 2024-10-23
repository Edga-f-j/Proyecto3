import pandas as pd
import matplotlib.pyplot as plt



#################### CUANTAS MUJERES Y HOMBRES TUVIERON Y NO TUVIERON PAROS CARDIACOS #########

df = pd.read_csv("archivoss/tatakae.csv")


df['Gender'] = df['Gender'].apply(lambda x: 'Hombre' if x == 1 else 'Mujer')

df_agrupacion_genero = df.groupby(['Gender', 'Result']).size().unstack(fill_value=0)

ax = df_agrupacion_genero.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])

plt.title('Comparación de hombres y mujeres que tuvieron o no infarto', fontsize=14)
plt.xlabel('Género', fontsize=12)
plt.ylabel('Cantidad de Personas', fontsize=12)


for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10)


plt.xticks(rotation=0)


ax.legend(['No Infarto', 'Infarto'], title='Resultado', fontsize=10)


plt.show()
