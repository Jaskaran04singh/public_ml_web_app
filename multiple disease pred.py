# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 11:17:02 2025

@author: Jaskaran Singh
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models with relative paths (upload these files to Streamlit Cloud)
loaded_model = pickle.load(open("diabetpro.sav",'rb'))
load_model2 = pickle.load(open("heart_disease.sav",'rb'))

def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_resphape = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_resphape)
    if prediction[0] == 0:
        return "not diabetic"
    else:
        return "diabetic"

def heart_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_resphape = input_data_as_numpy_array.reshape(1, -1)
    prediction = load_model2.predict(input_data_resphape)
    if prediction[0] == 0:
        return "no heart disease"
    else:
        return "heart disease"

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                          ['Diabetes Prediction', 'Heart Disease Prediction'],
                          icons=['activity', 'heart'],
                          default_index=0)

if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction Web App")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies", value="0")
    with col2:
        Glucose = st.text_input("Glucose level", value="0")
    with col3:
        BloodPressure = st.text_input("Blood Pressure value", value="0")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value", value="0")
    with col2:
        Insulin = st.text_input("Insulin Level", value="0")
    with col3:
        BMI = st.text_input("BMI value", value="0")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value", value="0")
    with col2:
        Age = st.text_input("Age value", value="0")
    
    diagnosis = " "
    
    if st.button("Diabetes Test Result"):
        try:
            input_data = (
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            )
            diagnosis = diabetes_prediction(input_data)
        except ValueError:
            diagnosis = "Please enter valid numeric values"
    
    st.success(diagnosis)

if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Web App")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age (in years)", value="0")
    with col2:    
        sex = st.text_input("Sex (0=female, 1=male)", value="0")
    with col3:
        cp = st.text_input("Chest Pain Type (0-3)", value="0")
    with col1:    
        trestbps = st.text_input("Resting Blood Pressure", value="0")
    with col2:
        chol = st.text_input("Serum Cholesterol", value="0")	
    with col3:
        fbs = st.text_input("Fasting Blood Sugar (>120: 1, else: 0)", value="0")	
    with col1:
        restecg = st.text_input("Resting ECG Results (0-2)", value="0")	
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved", value="0")	
    with col3:
        exang = st.text_input("Exercise Induced Angina (1=yes, 0=no)", value="0")	
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise", value="0")
    with col2:
        slope = st.text_input("Slope of Peak Exercise ST Segment (0-2)", value="0")	
    with col3:
        ca = st.text_input("Number of Major Vessels (0-3)", value="0")	
    with col1:
        thal = st.text_input("Thalassemia (0-3)", value="0")
    
    diagnosis = " "
    
    if st.button("Heart Disease Test Result"):
        try:
            input_data = [
                float(age), int(sex), int(cp), float(trestbps), float(chol),
                int(fbs), int(restecg), float(thalach), int(exang),
                float(oldpeak), int(slope), int(ca), int(thal)
            ]
            diagnosis = heart_prediction(input_data)
        except ValueError:
            diagnosis = "Please enter valid numeric values"
    
    st.success(diagnosis)

