import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

rawdata=pd.read_csv("Height Data.csv")
X=rawdata.drop(columns=['Weight'])
y=rawdata['Weight']

model=DecisionTreeRegressor()
model.fit(X,y)

joblib.dump(model,'HeightWeightMLModel.joblib')