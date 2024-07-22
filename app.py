import streamlit as st
import pandas as pd
import pickle

# Cargar el modelo preentrenado (asegúrate de tener el archivo .sav)
with open('tree_classifier_crit_diabetes.sav', 'rb') as file:
    model = pickle.load(file)

# Definir las dos páginas
def pagina_datos():
    st.title('Explicación de los Datos')
    
    st.write("""
    ## Variables del Dataset de Diabetes
    Este dataset contiene las siguientes variables:
    - **Pregnancies**: Número de veces que una mujer ha estado embarazada.
    - **Glucose**: Nivel de glucosa en la sangre.
    - **BloodPressure**: Presión arterial diastólica (mm Hg).
    - **SkinThickness**: Espesor del pliegue cutáneo del tríceps (mm). (Esta variable no se usará para la predicción)
    - **Insulin**: Nivel de insulina en la sangre (mu U/ml).
    - **BMI**: Índice de Masa Corporal (peso en kg / (altura en m)^2).
    - **DiabetesPedigreeFunction**: Función de pedigrí de diabetes (una medida de la heredabilidad).
    - **Age**: Edad de la persona (años).
    - **Outcome**: Resultado de la prueba de diabetes (1 si tiene diabetes, 0 si no).
    """)
    
    st.write("""
    ## Descripción del Dataset
    Este dataset se ha utilizado para entrenar un modelo de árbol de decisión con el fin de predecir la presencia de diabetes en individuos basándose en las características mencionadas anteriormente, excepto `SkinThickness`.
    """)

def pagina_prediccion():
    st.title('Predicción de Diabetes')

    st.write("Ingrese los datos del paciente para realizar una predicción:")

    # Crear campos para ingresar los datos usando deslizadores
    pregnancies = st.slider('Número de Embarazos', min_value=0, max_value=20, value=0)
    glucose = st.slider('Nivel de Glucosa', min_value=0, max_value=200, value=0)
    blood_pressure = st.slider('Presión Arterial', min_value=0, max_value=150, value=0)
    insulin = st.slider('Nivel de Insulina', min_value=0, max_value=900, value=0)
    bmi = st.slider('Índice de Masa Corporal', min_value=0.0, max_value=70.0, value=0.0)
    dpf = st.slider('Función de Pedigrí de Diabetes', min_value=0.0, max_value=3.0, value=0.0)
    age = st.slider('Edad', min_value=0, max_value=120, value=0)

    # Realizar la predicción cuando el usuario presione el botón
    if st.button('Predecir'):
        # Crear el dataframe con los datos ingresados, sin 'SkinThickness'
        data = pd.DataFrame({
            'Pregnancies': [pregnancies],
            'Glucose': [glucose],
            'BloodPressure': [blood_pressure],
            'Insulin': [insulin],
            'BMI': [bmi],
            'DiabetesPedigreeFunction': [dpf],
            'Age': [age]
        })

        # Realizar la predicción
        prediction = model.predict(data)

        # Mostrar el resultado
        if prediction[0] == 1:
            st.write("El modelo predice que el paciente tiene diabetes.")
        else:
            st.write("El modelo predice que el paciente NO tiene diabetes.")

# Definir el menú de navegación
st.sidebar.title('Menú')
opcion = st.sidebar.selectbox('Seleccione una página', ['Explicación de los Datos', 'Predicción de Diabetes'])

if opcion == 'Explicación de los Datos':
    pagina_datos()
else:
    pagina_prediccion()
