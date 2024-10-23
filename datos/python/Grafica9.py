from flask import Flask, render_template
import io
import base64

import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("archivoss/tatakae.csv")

    ###########################3TROPONINA
df['Grupo_Troponin'] = df['Troponin'].apply(lambda x: 'Normal (<0.04 ng/mL)' if x < 0.04 else 'Alto (≥0.04 ng/mL)')


df_agrupacion_troponin = df.groupby(['Grupo_Troponin', 'Result']).size().unstack(fill_value=0)


ax = df_agrupacion_troponin.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])


plt.title('Relación entre Niveles de Troponina y Ataques Cardíacos (Infarto vs No Infarto)', fontsize=14)
plt.xlabel('Nivel de Troponina', fontsize=12)
plt.ylabel('Cantidad de Personas', fontsize=12)


for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10)


plt.xticks(rotation=0)


ax.legend(['No Infarto', 'Infarto'], title='Resultado', fontsize=10)


plt.show()


