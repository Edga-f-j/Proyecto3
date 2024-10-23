import pandas as pd
import matplotlib.pyplot as plt



######################################### NIVEL DE CK-MB

df = pd.read_csv("archivoss/tatakae.csv")


def clasificar_ckmb(row):
    if row['Gender'] == 1:  # Hombre
        return 'Normal (<7 ng/L)' if row['CK-MB'] < 7 else 'Alto (≥7 ng/L)'
    else:  # Mujer
        return 'Normal (<4 ng/L)' if row['CK-MB'] < 4 else 'Alto (≥4 ng/L)'

df['Grupo_CKMB'] = df.apply(clasificar_ckmb, axis=1)


df_agrupacion_ckmb = df.groupby(['Grupo_CKMB', 'Result']).size().unstack(fill_value=0)


ax = df_agrupacion_ckmb.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])


plt.title('Relación entre Niveles de CK-MB y Ataques Cardíacos (Infarto vs No Infarto)', fontsize=14)
plt.xlabel('Nivel de CK-MB', fontsize=12)
plt.ylabel('Cantidad de Personas', fontsize=12)


for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10)


plt.xticks(rotation=0)


ax.legend(['No Infarto', 'Infarto'], title='Resultado', fontsize=10)


plt.show()
