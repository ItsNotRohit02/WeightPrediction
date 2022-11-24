import streamlit as st
import joblib

model=joblib.load('HeightWeightAIModel.joblib')

st.title('Welcome to Weight Predictor!')
st.header('How we predict ?')
st.write('We use the Decision Tree Regression Algorithms to learn from data collected from over 10,000 individuals of various ethinicities, religions, income levels, quality of life and between the the age group of 20 to 50 years to create a complex and accurate model to predict the Weight of an individual.')
st.header('Select from Options below')

gender = st.radio('Select your Gender',['Male','Female'])
if gender == 'Male':
    g=0
else:
    g=1

a=st.slider('Select Age', 20,50)

h=st.slider('Select Height (in m)', 1.30,2.00)


p=model.predict([[g,h,a]])

st.success("The weight of a %d year old %s of %f m is most likely going to be %.2f kg "%(a,gender,h,p[0]))