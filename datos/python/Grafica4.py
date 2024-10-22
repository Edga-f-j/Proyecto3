

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
df = pd.read_csv("archivoss/tatakae.csv")

# Crear los grupos para la presión arterial sistólica (Systolic blood pressure)
df['Grupo_SystolicBP'] = df['Systolic blood pressure'].apply(lambda x: 'Bajo (<90)' if x < 90 else 'Normal (90-120)' if x <= 120 else 'Alto (>120)')

# Agrupar por niveles de presión sistólica y resultados (infarto o no)
df_agrupacion_systolic = df.groupby(['Grupo_SystolicBP', 'Result']).size().unstack(fill_value=0)

# Crear la gráfica de barras para la presión sistólica
ax = df_agrupacion_systolic.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])

# Título y etiquetas
plt.title('Comparación de personas según Presión Sistólica (Infarto vs No Infarto)', fontsize=14)
plt.xlabel('Rango de Presión Sistólica', fontsize=12)
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

