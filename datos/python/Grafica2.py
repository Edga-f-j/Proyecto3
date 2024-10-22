import pandas as pd
import matplotlib.pyplot as plt



################################3 GRAFICA CUANTOS TUVIERON PAROS CARDIACOS  CON PRESIO BAJA, ALTA Y NORMAL

# Cargar los datos del archivo CSV
df = pd.read_csv("archivoss/tatakae.csv")

# Crear el grupo por niveles de ritmo cardíaco (Heart rate)
# Se pueden crear grupos de rango, por ejemplo, bajo < 60, normal 60-100, alto > 100
df['Grupo_HeartRate'] = df['Heart rate'].apply(lambda x: "Bajo (<60)" if x < 60 else "Normal (60-100)" if x <= 100 else "Alto (>100)")

# Agrupar por niveles de Heart rate y resultados (infarto o no)
df_agrupacion_hr = df.groupby(['Grupo_HeartRate', 'Result']).size().unstack(fill_value=0)

# Crear la gráfica de barras
ax = df_agrupacion_hr.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])

# Título y etiquetas
plt.title('Comparación de personas según el ritmo cardíaco (Infarto vs No Infarto)', fontsize=14)
plt.xlabel('Rango de Ritmo Cardíaco', fontsize=12)
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
