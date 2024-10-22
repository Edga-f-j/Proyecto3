

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archivoss/tatakae.csv")


# Crear el grupo por niveles de troponina y resultado
df['Grupo_Troponin'] = df['Troponin'].apply(lambda x: "Bajo" if x <= 0.01 else "Alto")

# Agrupar por niveles de Troponina y resultados (infarto o no)
df_agrupacion2 = df.groupby(['Grupo_Troponin', 'Result']).size().unstack(fill_value=0)

# Crear la gráfica de barras con mejoras visuales
ax = df_agrupacion2.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])

# Título y etiquetas
plt.title('Comparación de personas con Troponin Bajo y Alto (Infarto vs No Infarto)', fontsize=14)
plt.xlabel('Nivel de Troponina', fontsize=12)
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