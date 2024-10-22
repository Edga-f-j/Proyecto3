
import pandas as pd

######### BIBLIOTECAS NECESARIAS PARA LA IA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


############### ESTA ES PARA MOSTRAR LOS RESULTADOS LA MATRIZ DE RESULTADOS Y GRAFICAR COMO QUEDO 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv("archivoss/tatakae.csv")

######### esto es pa convertir los string en valores numericos, infarto es 1, y el paro es 0####
df['Result'] = df['Result'].map({'positive': 1, 'negative': 0})  


X = df[['Age', 'Heart rate', 'Systolic blood pressure', 'Diastolic blood pressure', 'Blood sugar', 'CK-MB', 'Troponin']]
y = df['Result'].astype(int)  #que sea de tipo entero


###################  CODIGO DE ENTRENAMIENTO PA LA IA, ES EL 80% 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

################### CON ESTO SE CREA UN ARCHIVO NUEVO QUE ES LA IA
with open('modelo_entrenado.pkl', 'wb') as file:
    pickle.dump(model, file)





################### IMPORTENTE PA CONVERTIR LAS PRUEBAS A ENTEROS 
y_pred = model.predict(X_test).astype(int)  




################## CODIGO PA GRAFICAR Y EVALUAR LOS RESULTADOS DE LA IA
# # Evaluar el modelo con métricas de clasificación
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Precisión del modelo: {accuracy:.2f}')

# # Mostrar la matriz de confusión
# print('Matriz de confusión:')
# print(confusion_matrix(y_test, y_pred))

# # Mostrar un reporte de clasificación detallado
# print('Reporte de clasificación:')
# print(classification_report(y_test, y_pred))



# # Visualización de comparación entre valores reales y predichos
# real_counts = np.bincount(y_test)  # Contar los valores reales de infarto/no infarto
# pred_counts = np.bincount(y_pred)  # Contar los valores predichos por el modelo



# # Crear la gráfica de barras comparando real vs predicho
# labels = ['No Infarto', 'Infarto']
# x = np.arange(len(labels))  # Posición de las etiquetas

# width = 0.35  # Ancho de las barras

# plt.figure(figsize=(8, 6))
# plt.bar(x - width/2, real_counts, width, label='Real')
# plt.bar(x + width/2, pred_counts, width, label='Predicho')

# plt.xlabel('Resultado')
# plt.ylabel('Cantidad de personas')
# plt.title('Comparación de Infartos Reales vs Predichos')
# plt.xticks(x, labels)
# plt.legend()

# plt.show()











# Seleccionar las columnas que vamos a usar como características (X) y la columna target (y)
# X = df[['Age', 'Heart rate', 'Systolic blood pressure', 'Diastolic blood pressure', 'Blood sugar', 'CK-MB', 'Troponin']]
# y = df['Result']  # Suponiendo que esta columna tiene 0 o 1 para representar infarto/no infarto

# # Dividir los datos en conjunto de entrenamiento (80%) y prueba (20%)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# #####  ESCALAR DATOS #####
# scaler = StandardScaler()

# # Escalar las características
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)




# # Crear el modelo
# model = LogisticRegression()

# # Entrenar el modelo con los datos de entrenamiento
# model.fit(X_train, y_train)



# # Hacer predicciones con el conjunto de prueba
# y_pred = model.predict(X_test)

# # Calcular la precisión del modelo
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Precisión del modelo: {accuracy:.2f}')

# # Mostrar la matriz de confusión
# print('Matriz de confusión:')
# print(confusion_matrix(y_test, y_pred))

# # Mostrar un reporte de clasificación detallado
# print('Reporte de clasificación:')
# print(classification_report(y_test, y_pred))

# plt.figure(figsize=(10, 6))
# plt.plot(range(len(y_test)), y_test, label="Precio Real", marker='o')
# plt.plot(range(len(y_pred)), y_pred, label="Precio Predicho", marker='x')
# plt.xlabel("Ejemplos")
# plt.ylabel("Precio")
# plt.title("Comparación de Precios Reales vs Predichos")
# plt.legend()
# plt.show()


# plt.plot(Attack, yougn, label='Jovenes', color='blue', linestyle='--',linewidth=2)
# plt.plot(Attack, old, label='Adultos', color='green', linestyle='-', linewidth=2)
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')

# plt.title('TITULO')
# plt.show()
















# Attack = df["Troponin"]

# Adultos = df[(df['Age'] >= 41) & (df['Age'] <= 70)]
# Jovenes = df[(df['Age'] >= 26) & (df['Age'] <= 40)]



#########################################################
######################### EDAD  #########################

# Clasificación de personas jóvenes (<= 40 años) y mayores (> 40 años)
# Clasificar personas como jóvenes (<= 40) o mayores (> 40)
# df['grupo_edad'] = df['Age'].apply(lambda x: 'Joven' if x <= 40 else 'Mayor')


# # Agrupar por grupo de edad y resultado (infarto)
# df_agrupado = df.groupby(['grupo_edad', 'Result']).size().unstack(fill_value=0)

# # Crear gráfica de barras
# df_agrupado.plot(kind='barh')

# # Añadir etiquetas y título
# plt.title('Cantidad de Personas Jóvenes vs Mayores con Infartos')
# plt.xlabel('Grupo de Edad')
# plt.ylabel('Cantidad de Personas')

# # Mostrar gráfica
# plt.show()


###########################################################
######################### GENERO  #########################



# df['Grupo_genero'] = df['Gender'].apply(lambda x: "Men" if x ==1 else "Woman")

# df_agrupacion2 = df.groupby(['Grupo_genero','Result']).size().unstack(fill_value=0)

# df_agrupacion2.plot(kind='bar')

# plt.title('Cantidad de Hombres vs Mujeres con Infartos')
# plt.xlabel('Grupo de Edad')
# plt.ylabel('Cantidad de Personas')

# # Mostrar gráfica
# plt.show()


###########################################################
######################### Troponin  #########################

# # Crear el grupo por niveles de troponina y resultado
# df['Grupo_Troponin'] = df['Troponin'].apply(lambda x: "Bajo" if x <= 0.01 else "Alto")

# # Agrupar por niveles de Troponina y resultados (infarto o no)
# df_agrupacion2 = df.groupby(['Grupo_Troponin', 'Result']).size().unstack(fill_value=0)

# # Crear la gráfica de barras con mejoras visuales
# ax = df_agrupacion2.plot(kind='bar', figsize=(10, 6), width=0.4, color=['#1f77b4', '#ff7f0e'])

# # Título y etiquetas
# plt.title('Comparación de personas con Troponin Bajo y Alto (Infarto vs No Infarto)', fontsize=14)
# plt.xlabel('Nivel de Troponina', fontsize=12)
# plt.ylabel('Cantidad de Personas', fontsize=12)

# # Añadir etiquetas de conteo encima de las barras
# for container in ax.containers:
#     ax.bar_label(container, label_type='edge', fontsize=10)


# # Rotar las etiquetas del eje X para mayor legibilidad
# plt.xticks(rotation=0)

# # Ajustar la leyenda para indicar 'No Infarto' y 'Infarto'
# ax.legend(['No Infarto', 'Infarto'], title='Resultado', fontsize=10)

# # Mostrar la gráfica
# plt.show()






# Attack = df["Troponin"]
# yougn = Jovenes["Age"]
# old = Adultos["Age"]

# #convenciones
# #Muestra los datos en consola
# # print(Attack)




# plt.plot(Attack, yougn, label='Jovenes', color='blue', linestyle='--',linewidth=2)
# plt.plot(Attack, old, label='Adultos', color='green', linestyle='-', linewidth=2)
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')

# plt.title('TITULO')
# plt.show()