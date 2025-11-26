# Write your code here
from sklearn.pipeline import Pipeline
import pandas as pd
import streamlit

## Create funtion to predict output of  species
def predict_species(model : Pipeline, 
                    sep_len : int|float ,
                    sep_wid : int|float ,
                    petal_len : int|float ,
                    petal_wid : int|float ):
    
    x_new = pd.DataFrame([{'sepal_length' : sep_len ,
                           "sepal_width" : sep_wid ,
                           "petal_length" : petal_len ,
                           "petal_width" : petal_wid}])
    

    pred = model.predict(x_new)
    prob = model.predict_proba(x_new)
    probs = pd.DataFrame(prob , columns=model.classes_)
    return pred[0] , probs