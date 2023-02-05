# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:22:33 2023

@author: USER
"""

import numpy as np
import pandas as pd
import pickle


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
    return f"Predicted apartment price: ${prediction}"