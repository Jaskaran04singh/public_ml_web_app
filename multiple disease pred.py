# -*- coding: utf-8 -*-
"""
Multiple Disease Prediction Web App

@author: Jaskaran Singh
"""
import numpy as np
import pickle
import streamlit as st

# Load models with error handling
try:
    diabetes_model = pickle.load(open("diabetpro.sav", 'rb'))
    heart_model = pickle.load(open("heart_disease.sav", 'rb'))
except:
    st.error("Model files not found. Please make sure 'diabetpro.sav' and 'heart_disease.sav' are in the same directory.")
    st.stop()

def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = diabetes_model.predict(input_data_reshaped)
    return "diabetic" if prediction[0] == 1 else "not diabetic"

def heart_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = heart_model.predict(input_data_reshaped)
    return "heart disease" if prediction[0] == 1 else "no heart disease"

# Custom sidebar navigation (replacement for streamlit_option_menu)
st.sidebar.title("Multiple Disease Prediction System")
selected = st.sidebar.radio("Select Prediction Type", 
                           ['Diabetes Prediction', 'Heart Disease Prediction'],
                           index=0)

st.sidebar.markdown("---")
st.sidebar.info("This app predicts the likelihood of diabetes or heart disease based on input parameters.")

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction Web App")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pregnancies = st.text_input("Number of Pregnancies", value="0")
    with col2:
        glucose = st.text_input("Glucose level", value="0")
    with col3:
        blood_pressure = st.text_input("Blood Pressure value", value="0")
    with col1:
        skin_thickness = st.text_input("Skin Thickness value", value="0")
    with col2:
        insulin = st.text_input("Insulin Level", value="0")
    with col3:
        bmi = st.text_input("BMI value", value="0")
    with col1:
        diabetes_pedigree = st.text_input("Diabetes Pedigree Function value", value="0")
    with col2:
        age = st.text_input("Age", value="0")
    
    diagnosis = ""
    
    if st.button("Diabetes Test Result"):
        try:
            input_data = (pregnancies, glucose, blood_pressure, skin_thickness, 
                         insulin, bmi, diabetes_pedigree, age)
            diagnosis = diabetes_prediction(input_data)
            if diagnosis == "diabetic":
                st.error(f"Result: The patient is {diagnosis}")
            else:
                st.success(f"Result: The patient is {diagnosis}")
        except:
            st.error("Please enter valid numerical values for all fields.")

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Web App")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age (in years)", value="0")
    with col2:    
        sex = st.selectbox("Sex", ["Select", "Male (1)", "Female (0)"])
    with col3:
        cp = st.selectbox("Chest Pain Type", ["Select", "Typical angina (0)", "Atypical angina (1)", 
                                            "Non-anginal pain (2)", "Asymptomatic (3)"])
    with col1:    
        trestbps = st.text_input("Resting Blood Pressure (mm Hg)", value="0")
    with col2:
        chol = st.text_input("Serum Cholesterol (mg/dl)", value="0")	
    with col3:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Select", "Yes (1)", "No (0)"])	
    with col1:
        restecg = st.selectbox("Resting ECG Results", ["Select", "Normal (0)", 
                                                     "ST-T wave abnormality (1)", 
                                                     "Left ventricular hypertrophy (2)"])	
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved", value="0")	
    with col3:
        exang = st.selectbox("Exercise Induced Angina", ["Select", "Yes (1)", "No (0)"])	
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise", value="0")
    with col2:
        slope = st.selectbox("Slope of Peak Exercise ST Segment", ["Select", "Upsloping (0)", 
                                                                 "Flat (1)", "Downsloping (2)"])	
    with col3:
        ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", 
                         ["Select", "0", "1", "2", "3"])	
    with col1:
        thal = st.selectbox("Thalassemia", ["Select", "Normal (1)", "Fixed defect (2)", 
                                          "Reversible defect (3)"])
    
    # Convert categorical inputs to numerical values
    sex_val = 1 if sex == "Male (1)" else 0 if sex == "Female (0)" else 0
    cp_val = 0 if "Typical angina" in cp else 1 if "Atypical angina" in cp else 2 if "Non-anginal" in cp else 3 if "Asymptomatic" in cp else 0
    fbs_val = 1 if fbs == "Yes (1)" else 0
    restecg_val = 0 if "Normal" in restecg else 1 if "ST-T wave" in restecg else 2
    exang_val = 1 if exang == "Yes (1)" else 0
    slope_val = 0 if "Upsloping" in slope else 1 if "Flat" in slope else 2
    ca_val = 0 if ca == "Select" else int(ca)
    thal_val = 1 if "Normal" in thal else 2 if "Fixed defect" in thal else 3
    
    diagnosis = ""
    
    if st.button("Heart Disease Test Result"):
        try:
            input_data = [float(age), sex_val, cp_val, float(trestbps), float(chol), 
                         fbs_val, restecg_val, float(thalach), exang_val, 
                         float(oldpeak), slope_val, ca_val, thal_val]
            diagnosis = heart_prediction(input_data)
            if diagnosis == "heart disease":
                st.error(f"Result: The patient has {diagnosis}")
            else:
                st.success(f"Result: The patient has {diagnosis}")
        except Exception as e:
            st.error(f"Please enter valid numerical values for all fields. Error: {str(e)}")

# Add some styling
st.markdown("""
<style>
    .main-header {
        font-size: 24px;
        color: #1f77b4;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    .stSelectbox, .stTextInput {
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)
