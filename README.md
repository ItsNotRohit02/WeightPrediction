# Weight Predictor

## How it Works
This Python program uses the streamlit, pandas and sklearn libraries to train a decision tree regression model on a dataset of 
Height, Weight and Age data. The dataset is read in using the pandas library and stored in a DataFrame called rawdata. 
The features (or independent variables) for the model are stored in the DataFrame X, while the target (or dependent variable) 
is stored in the variable y.

The sklearn library is then used to create a decision tree regression model and train it on the data stored in X and y. 
The trained model is then saved to a file called HeightWeightMLModel.joblib using the joblib library.

The streamlit library is used to create a user interface for the program. The user is able to select their Gender, Height 
and Age. The program then gives a predicted weight as an output.
The Program learns from over 10,000 data entries.

## Click Link Below 
[Click Here to see the Program in action](https://itsnotrohit02-weightprediction-heightweightapp-paqq34.streamlit.app/)

## How to Use the Program
* Download the Height Data.csv file.
* Download the required libraries as mentioned in the requirements.txt file.
* Run Height Weight.py . This creates the HeightWeightMLModel.joblib (ML Model)
* Run the HeightWeightApp.py using "streamlit run HeightWeightApp.py" command in the command prompt while in the program directory.
* This should open a webpage that looks like [this](https://itsnotrohit02-weightprediction-heightweightapp-paqq34.streamlit.app/).

## Extra
* The Accuracy Score of the ML Model is 80%.