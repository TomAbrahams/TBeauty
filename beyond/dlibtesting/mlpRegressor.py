import os
import numpy as np # Your spreadsheet manipulator tools.
import pandas as pd #Your Spreadsheet importer tools.
from sklearn.neural_network import MLPClassifier #Your neural network tools.
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
import matplotlib.pyplot as plt #To plot graphs and items.
from pandas.tools.plotting import scatter_matrix #To Make a scatter matrix
from sklearn.model_selection import train_test_split # This will help as randomize the data
from sklearn.metrics import accuracy_score #The way to determine how accurate we are.
from sklearn.metrics import confusion_matrix #The Matrix to show the what was correctly predicted and what wasn't.
from sklearn.externals import joblib
# Lets get the names of each of the columns.
email = input("What user email do you wish to analyze.\n")
email = email.replace("@","_")
saveFileName = email + '-' + 'resultsfile.csv'
direct = os.getcwd()
path = os.path.join(direct+"/fileRecords/", saveFileName)
rawData = pd.read_csv(path)
#Cleaned up the dataset
del rawData['picid']
del rawData['imgname']
del rawData['email']

arrayRawData = rawData.values
X = arrayRawData[:,0:128]
X= (X+1)*10
Y = arrayRawData[:,128]

print("This is X\n")
print(X)

print("This is Y\n")
print(Y)
validation_size = 0.20
seed = 7

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = validation_size, random_state = seed)

NeuralModel = MLPClassifier(hidden_layer_sizes=(30,),activation='relu',solver='lbfgs',
learning_rate_init=0.00000000000000000001, verbose=True,max_iter=5000, learning_rate='constant',tol = 0.0000000001,
early_stopping=False)

print("X is = ")
print(X)
NeuralModel.fit(X,Y)
Y_pred = NeuralModel.predict(X_test)
print(confusion_matrix(Y_test,Y_pred))
testData = pd.read_csv("testData.csv")
print("Test Data Acquired")
del testData['imgname']
del testData['picid']
#print(testData)
testData = testData*10
#print(testimg)
print("Test timg052 = ")
numValue = NeuralModel.predict(testData)
print(numValue)
#GET Test Data
numVal2 = NeuralModel.predict(X_test)
print("NumVal2")
print(numVal2)
print("Y_test")
print(Y_test)
fileName= str(email) + '.joblib'
joblib.dump(NeuralModel, fileName)
