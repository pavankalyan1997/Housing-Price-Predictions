# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:28:24 2018

@author: purandur
"""

import pandas as pd
import os
os.chdir('D:\Machine_Learning_Projects_by_Me\Housing Price Prediction')
HOUSING_PATH = os.path.join("datasets", "housing")

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path=os.path.join(housing_path,"housing.csv")
    return pd.read_csv(csv_path)

housing=load_housing_data()
housing.head()