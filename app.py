import numpy as np
import pandas as pd
import pickle 
import streamlit as st

pickle_master=open("linear.pkl","rb")
regressor=pickle.load(pickle_master) # our model

def predict_chance(GREScore,TOEFLScore,UniversityRating,CGPA):
    prediction=regressor.predict([[GREScore,TOEFLScore,UniversityRating,CGPA]])
    return prediction

def main():
    st.title("Admission prediction Using Linear Regression") 
    html_temp="""
        <div style="background-color:tomato;padding:10px">
        <h2 style ="color:black;text-align:center;">Admission Predictor</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)
    GREScore=st.text_input("GRE (0-340)")
    TOEFLScore=st.text_input("TOEFL (0-120)")
    UniversityRating=st.text_input("University Score(1-5)")
    CGPA=st.text_input("CGPA(1-10)")
    result=""
    if st.button("Predict"):
        result=predict_chance(GREScore, TOEFLScore, UniversityRating, CGPA)
    st.success("The admission chance in that university is{}".format(result))
        
if __name__=='__main__':
    main()
