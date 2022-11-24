import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

rawdata=pd.read_csv("Height Data.csv")
x=rawdata.drop(columns=['Weight'])
y=rawdata['Weight']

model=DecisionTreeRegressor()
model.fit(x,y)
g=int(input("Enter Gender of the person (0=Male,1=Female) "))
a=int(input("Enter Age of the person "))
h=float(input("Enter Height of person (in meters) "))
p=model.predict([[g,h,a]])
print("The weight of the person is most likely going to be %.2f kg "%p[0])

joblib.dump(model,'HeightWeightAIModel.joblib')