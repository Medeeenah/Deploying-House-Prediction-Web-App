# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 19:16:56 2023

@author: USER
"""


import numpy as np
import pickle
import pandas as pd
import streamlit as st

loaded_model = pickle.load(open("C:/Users/USER/Desktop/ML/models/house_model.pkl", "rb"))

def make_prediction(area, lat, lon, borough):
    data = {
        "Surface_covered_in_m2": area,
        "lat": lat,
        "lon": lon,
        "borough": borough
    }
    df = pd.DataFrame(data, index=[0])
    prediction = loaded_model.predict(df).round(2)[0]
    return f"${prediction}"


def main():
    
    #Title
    st.title("Mexico Houses Prediction Web App")
    
    #Get input from the user
    
    Surface_covered_in_m2 = st.text_input("Surface_covered_in_m2")
    lat = st.text_input("Latitude")
    lon = st.text_input("Longitude")
    borough = st.text_input("Borough")
    
    #code for prediction
    House_price = ""
    #Creating button for prediction
    if st.button("Predict House Price"):
        House_price = make_prediction(Surface_covered_in_m2, lat, lon, borough)
        
    st.success(House_price)
    

if __name__ == "__main__":
        main()
    
    