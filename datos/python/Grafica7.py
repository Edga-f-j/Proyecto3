import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


####################################################GRAFICA ESPECIAL #####
# Cargar los datos del archivo CSV
df = pd.read_csv("archivoss/tatakae.csv")

# Crear los grupos para el nivel de azúcar en sangre (Blood sugar)
df['Grupo_BloodSugar'] = df['Blood sugar'].apply(lambda x: 'Normal (<100)' if x < 100 else 'Prediabetes (100-125)' if x <= 125 else 'Diabetes (>126)')

# Crear los grupos para el ritmo cardíaco (Heart rate)
df['Grupo_HeartRate'] = df['Heart rate'].apply(lambda x: "Bajo" if x < 60 else "Normal" if x <= 100 else "Alto")

# Crear una tabla cruzada para ver la distribución de infartos según azúcar y ritmo cardíaco
tabla_cruzada = pd.crosstab([df['Grupo_BloodSugar'], df['Grupo_HeartRate']], df['Result'])

# Crear la gráfica tipo heatmap para visualizar la relación
plt.figure(figsize=(12, 8))
sns.heatmap(tabla_cruzada, annot=True, cmap="YlGnBu", fmt="d")

# Título y etiquetas
plt.title('Relación entre Nivel de Azúcar y Ritmo Cardíaco con el Resultado (Infarto vs No Infarto)', fontsize=16)
plt.xlabel('Resultado', fontsize=12)
plt.ylabel('Nivel de Azúcar y Ritmo Cardíaco', fontsize=12)

# Mostrar la gráfica
plt.show()
