import streamlit as st
import joblib

model=joblib.load('HeightWeightAIModel.joblib')

st.set_page_config(page_title="Weight Predictor",page_icon=":chart_with_downwards_trend:")
st.title('Welcome to Weight Predictor!')
st.header('How we predict ?')
st.write('We use the Decision Tree Regression Algorithms to learn from data collected from over 10,000 individuals of various ethinicities, religions, income levels, quality of life and between the the age group of 20 to 50 years to create a complex and accurate model to predict the Weight of an individual.')
st.write('---')
st.header('Select from Options below')

gender = st.radio('Select your Gender',['Male','Female'])
if gender == 'Male':
    g=0
else:
    g=1

a=st.slider('Select Age', 20,50)
h=st.slider('Select Height (in m)', 1.30,2.00)
p=model.predict([[g,h,a]])
w=p[0]
w1=round(w,2)

st.metric(label='Predicted Weight', value=f"{w1} kg")
st.success("The weight of a %d year old %s of %.2f m is most likely going to be %.2f kg "%(a,gender,h,p[0]))
st.caption("Made by Rohit")