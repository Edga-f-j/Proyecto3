import pandas as pd
import matplotlib.pyplot as plt



######################################### NIVEL DE CK-MB
# Cargar los datos del archivo CSV
df = pd.read_csv("archivoss/tatakae.csv")

# Crear un grupo basado en los niveles de CK-MB y género
def clasificar_ckmb(row):
    if row['Gender'] == 1:  # Hombre
        return 'Normal (<7 ng/L)' if row['CK-MB'] < 7 else 'Alto (≥7 ng/L)'
    else:  # Mujer
        return 'Normal (<4 ng/L)' if row['CK-MB'] < 4 else 'Alto (≥4 ng/L)'

df['Grupo_CKMB'] = df.apply(clasificar_ckmb, axis=1)

# Agrupar por niveles de CK-MB y resultados (infarto o no)
df_agrupacion_ckmb = df.groupby(['Grupo_CKMB', 'Result']).size().unstack(fill_value=0)

# Crear la gráfica de barras
ax = df_agrupacion_ckmb.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])

# Título y etiquetas
plt.title('Relación entre Niveles de CK-MB y Ataques Cardíacos (Infarto vs No Infarto)', fontsize=14)
plt.xlabel('Nivel de CK-MB', fontsize=12)
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
