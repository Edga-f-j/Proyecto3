
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




