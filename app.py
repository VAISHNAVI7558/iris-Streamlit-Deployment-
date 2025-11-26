# Write your code here
import streamlit as st
import pandas as pd
from utils import predict_species
import joblib

model = joblib.load('/workspaces/iris-Streamlit-Deployment-/notebook/iris_model.joblib')

# Design page

st.set_page_config(page_title = 'Iris end to end deploymebt')

# Give title
st.title("Iris Deployment for end user")

# Give Name
st.subheader('By Vaishnavi Rayphale')