# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 11:17:02 2025

@author: Jaskaran Singh
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

loaded_model=pickle.load(open("C:/Users/Jaskaran Singh/OneDrive/Documents/Desktop/New folder/diabetpro.sav",'rb'))
load_model2= pickle.load(open("C:/Users/Jaskaran Singh/OneDrive/Documents/Desktop/New folder/heart_disease.sav",'rb'))

def diabetes_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_resphape=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_resphape)
    if(prediction[0]==0):
        return "not diabetic"
    else:
        return "diabetic" 
def heart_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_resphape=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model2.predict(input_data_resphape)
    if(prediction[0]==0):
        return "not heart disease"
    else:
        return "heart disease"
with st.sidebar:
    selected=option_menu("Multiple Disease Prediction System",
                        
                         ['Diabetes Prediction','Heart Disease Prediction'],
                         
                         icons=['activity','heart'],
                        
                         default_index=0)

if(selected=='Diabetes Prediction'):
    st.title("Diaetes Prediction web App")
    col1,col2,col3=st.columns(3)
    with col1:
      Pregnancies=st.text_input("Number of Pregnancies")
    with col2:
      Glucose=st.text_input("Glucose level")
    with col3:
      BloodPressure=st.text_input("Blood Pressure value")
    with col1:
        SkinThickness=st.text_input("Skin Thickness value")
    with col2:
         Insulin=st.text_input("Insulin Level")
    with col3:
      BMI=st.text_input("BMI value")
    with col1:
         DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function value")
    with col2:
         Age=st.text_input("Age value")
    #code for prediction
    diagnosis=" "
     # crating a button of prediction
    input_data=(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
     
    if st.button("Diabetes Test result"):
        diagnosis=diabetes_prediction(input_data)
    
    st.success(diagnosis)
    
    
if(selected=='Heart Disease Prediction'):
    st.title("Heart Disease Prediction web App")
      
    col1,col2,col3=st.columns(3)
      
    with col1:
         age = st.text_input("Age (in years)")
    with col2:    
        sex = st.text_input("Sex ")
    with col3:
        cp = st.text_input("Chest Pain Type ")
    with col1:    
        trestbps = st.text_input("Resting Blood Pressure )")
    with col2:
        chol = st.text_input("Serum Cholesterol ")	
    with col3:
        fbs = st.text_input("Fasting Blood Sugar  ")	
    with col1:
        restecg = st.text_input("Resting ECG Results ")	
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved") 	
    with col3:
        exang = st.text_input("Exercise Induced Angina (1 = yes, 0 = no)")	
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise")
    with col2:
        slope = st.text_input("Slope of Peak Exercise ST Segment ")	
    with col3:
        ca = st.text_input("Number of Major Vessels Colored by Fluoroscopy")	
    with col1:
        thal = st.text_input("Thalassemia ")
      
    diagnosis=" "
      # crating a button of prediction
    
      
    if st.button("Diabetes Test result"):
         diagnosis=diabetes_prediction( input_data = [
            float(age),
            int(sex),
            int(cp),
            float(trestbps),
            float(chol),
            int(fbs),
            int(restecg),
            float(thalach),
            int(exang),
            float(oldpeak),
            int(slope),
            int(ca),
            int(thal)
        ])
     
    st.success(diagnosis)      
         