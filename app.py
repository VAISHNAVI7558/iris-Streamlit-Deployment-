# Write your code here
import streamlit as st
import pandas as pd
from utils import predict_species
import joblib

model = joblib.load('notebook/iris_model.joblib')

# Design page

st.set_page_config(page_title = 'Iris end to end deploymebt')

# Give title
st.title("Iris Deployment for end user")

# Give Name
st.subheader('By Vaishnavi Rayphale')

# Tack input from user
sep_len = st.number_input("sepal_lenght" , min_value= 0.00)
sep_wid = st.number_input("sepal_widht" , min_value= 0.00)
petal_len = st.number_input("petal_lenght" , min_value= 0.01)
petal_wid = st.number_input("petal_widht" , min_value= 0.00)



## Add button

predict = st.button("Predition" , type = 'primary')

if predict:
    pred = predict_species(model , sep_len , sep_wid , petal_len , petal_wid)

st.subheader(pred)
probs  =  st.dataframe(pred)
st.subheader(probs)