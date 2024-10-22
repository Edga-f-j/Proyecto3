
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archivoss/tatakae.csv")
# Crear los grupos para la presión arterial diastólica (Diastolic blood pressure)
df['Grupo_DiastolicBP'] = df['Diastolic blood pressure'].apply(lambda x: 'Bajo (<60)' if x < 60 else 'Normal (60-80)' if x <= 80 else 'Alto (>80)')

# Agrupar por niveles de presión diastólica y resultados (infarto o no)
df_agrupacion_diastolic = df.groupby(['Grupo_DiastolicBP', 'Result']).size().unstack(fill_value=0)

# Crear la gráfica de barras para la presión diastólica
ax = df_agrupacion_diastolic.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])
#color=['#2ca02c', '#d62728']


# Título y etiquetas
plt.title('Comparación de personas según Presión Diastólica (Infarto vs No Infarto)', fontsize=14)
plt.xlabel('Rango de Presión Diastólica', fontsize=12)
plt.ylabel('Cantidad de Personas', fontsize=12)

# Añadir etiquetas de conteo encima de las barras
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10)

# Rotar las etiquetas del eje X para mayor legibilidad
plt.xticks(rotation=0)

# Ajustar la leyenda para indicar 'No Infarto' y 'Infarto'
ax.legend(['No Infarto', 'Infarto'], title='Resultado', fontsize=10)

# Mostrar la gráfica
plt.show()
