from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado
with open('modelo_entrenado.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def home():
    ###########  ENTRA AL HTML
    return render_template('index.html')

    ###########  ENTRA AL FORMULARIO
@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.get_json()  ######## CONVIERTE LOS DATOS COMO SI FUERAN OBJETOS ##########

##### --------------------------

    edad = float(data['age'])
    heart_rate = float(data['heartRate'])
    systolic_bp = float(data['systolicBP'])
    diastolic_bp = float(data['diastolicBP'])
    blood_sugar = float(data['bloodSugar'])
    ckmb = float(data['ckmb'])
    troponin = float(data['troponin'])


    ########## CON LOS DATOS DE ARRIBA AHORA GUARDA TODOOO ESO EN UN NUEV VECTOR O ARREGLO QUE SE ENVIA A LA IA ######
    input_data = np.array([[edad, heart_rate, systolic_bp, diastolic_bp, blood_sugar, ckmb, troponin]])

    ########## CON ESTO YA SE ENCARGA DE HACER LA PREDICCION CON LOS DATOS QUE SE LE PASARON
    prediccion = model.predict(input_data)
    

    if (prediccion[0] == 1):
        resultado = 'Riesgo de infarto'
    else:
        resultado = 'Sin riesgo de infarto'


# resultado = 'Riesgo de infarto' if prediccion[0] == 1 else 'Sin riesgo de infarto'


    return jsonify(prediccion=resultado)

if __name__ == "__main__":
    app.run(debug=True)

