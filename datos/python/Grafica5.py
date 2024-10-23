
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archivoss/tatakae.csv")

df['Grupo_DiastolicBP'] = df['Diastolic blood pressure'].apply(lambda x: 'Bajo (<60)' if x < 60 else 'Normal (60-80)' if x <= 80 else 'Alto (>80)')


df_agrupacion_diastolic = df.groupby(['Grupo_DiastolicBP', 'Result']).size().unstack(fill_value=0)


ax = df_agrupacion_diastolic.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])




plt.title('Comparación de personas según Presión Diastólica (Infarto vs No Infarto)', fontsize=14)
plt.xlabel('Rango de Presión Diastólica', fontsize=12)
plt.ylabel('Cantidad de Personas', fontsize=12)


for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10)


plt.xticks(rotation=0)


ax.legend(['No Infarto', 'Infarto'], title='Resultado', fontsize=10)


plt.show()
