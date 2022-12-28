import streamlit as st
import joblib

model = joblib.load('HeightWeightMLModel.joblib')
st.set_page_config(page_title="Weight Predictor",page_icon=":chart_with_downwards_trend:")


st.title('Welcome to Weight Predictor!')
st.header('How we predict ?')
st.write('We use the Decision Tree Regression Algorithms to learn from data collected from over 10,000 individuals of '
         'various religions and income levels between the the age group of 20 to 50 '
         "years to create a complex and accurate model to predict the Weight of an individual. P.S if you aren't "
         "american the prediction might not be accurate as the training data is based on american individuals.")
st.write('---')
st.header('Select from Options below')


gender = st.radio('Select your Gender',['Male','Female'])
if gender == 'Male':
    g=0
else:
    g=1
a=st.slider('Select Age', min_value= 20, max_value=50 ,value=35)
h=st.slider('Select Height (in m)', min_value=1.30, max_value=2.00, value=1.65)
p=model.predict([[g,h,a]])
w=p[0]
w1=round(w,2)
w2=round(w*2.20462,2)


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label='Predicted Weight', value=f"{w1} kg")
with col2:
    st.metric(label='', value=f"{w2} lbs")


st.success("The weight of a %d year old %s of %.2f m is most likely going to be %.2f kg "%(a,gender,h,p[0]))
st.caption("Made by Rohit")
st.markdown("[![Foo](https://cdn-icons-png.flaticon.com/24/25/25231.png)](https://github.com/ItsNotRohit02)")