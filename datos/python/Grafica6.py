import pandas as pd
import matplotlib.pyplot as plt



########################################## AZUCAR

df = pd.read_csv("archivoss/tatakae.csv")


df['Grupo_BloodSugar'] = df['Blood sugar'].apply(lambda x: 'Normal (<100)' if x < 100 else 'Prediabetes (100-125)' if x <= 125 else 'Diabetes (>126)')


df_agrupacion_azucar = df.groupby(['Grupo_BloodSugar', 'Result']).size().unstack(fill_value=0)


ax = df_agrupacion_azucar.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])


plt.title('Comparación de personas según el nivel de azúcar en sangre (Infarto vs No Infarto)', fontsize=14)
plt.xlabel('Nivel de Azúcar en Sangre', fontsize=12)
plt.ylabel('Cantidad de Personas', fontsize=12)


for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10)


plt.xticks(rotation=0)


ax.legend(['No Infarto', 'Infarto'], title='Resultado', fontsize=10)


plt.show()
