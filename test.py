import numpy as np
import pickle
import streamlit as st
import pandas as pd
import numpy as np

model = pickle.load(open('finalized_model.sav', 'rb')) 
def predict(Distance,Days,AcresBurned):
    values=[Distance,Days,AcresBurned]
    features = [float(i) for i in values]
    array_features = [np.array(features)]
    prediction = model.predict(array_features)
    if(prediction == 3):
        st.text("You are safe,there are very low chances of the wildfire reaching your city ")
    elif(prediction == 2):
        st.text("You might be in danger as the wilfire is expected to reach you in 7-10 days, you must prepare to evacuate")
    elif(prediction == 1):
        st.text("You are in danger, the wildfire is expected to reach within 3-7 days,you must evacuate")
    else:
        st.text("Immediate Danger, wildfire might reach your city within 1-3 days, evacuate now!")

def main():
    Distance = st.number_input('Enter the distance of the wildfire from Los Angeles')
    AcresBurned = st.number_input('Enter approximate size of the acres burned in the wildfire')
    Day = st.number_input('Enter the number of days since the fire started')
    if st.button("Predict"):
            predict(Distance,Day,AcresBurned)

if __name__ == '__main__':
#Run the application
    main()