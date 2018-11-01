import os
import numpy as np # Your spreadsheet manipulator tools.
import pandas as pd #Your Spreadsheet importer tools.
from sklearn.neural_network import MLPClassifier #Your neural network tools.
from sklearn.svm import SVR
import matplotlib.pyplot as plt #To plot graphs and items.
from sklearn.externals import joblib
from pandas.tools.plotting import scatter_matrix #To Make a scatter matrix
from sklearn.model_selection import train_test_split # This will help as randomize the data
from sklearn.metrics import accuracy_score #The way to determine how accurate we are.
from sklearn.metrics import confusion_matrix #The Matrix to show the what was correctly predicted and what wasn't.

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
Y = arrayRawData[:,128]
print("This is X\n")
print(X)

print("This is Y\n")
print(Y)
validation_size = 0.20
seed = 7

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = validation_size, random_state = seed)

clf = SVR(C=1.0, epsilon = 0.2)
clf.fit(X,Y)
testData = pd.read_csv("testData.csv")
print("Test Data Acquired")
del testData['imgname']
del testData['picid']
#print(testData)

#print(testimg)
print("Test timg052 = ")
numValue = clf.predict(testData)
print(numValue[0])
fileName= str(email) + '.joblib'
joblib.dump(clf, fileName)
#s = pickle.dumps(clf)
#GET Test Data
