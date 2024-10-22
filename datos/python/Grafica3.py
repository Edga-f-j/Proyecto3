import pandas as pd
import matplotlib.pyplot as plt



#################### CUANTAS MUJERES Y HOMBRES TUVIERON Y NO TUVIERON PAROS CARDIACOS #########
# Cargar los datos del archivo CSV
df = pd.read_csv("archivoss/tatakae.csv")

# Cambiar los valores de Gender a etiquetas más descriptivas
df['Gender'] = df['Gender'].apply(lambda x: 'Hombre' if x == 1 else 'Mujer')

# Agrupar por género y resultado (infarto o no)
df_agrupacion_genero = df.groupby(['Gender', 'Result']).size().unstack(fill_value=0)

# Crear la gráfica de barras
ax = df_agrupacion_genero.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])

# Título y etiquetas
plt.title('Comparación de hombres y mujeres que tuvieron o no infarto', fontsize=14)
plt.xlabel('Género', fontsize=12)
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
