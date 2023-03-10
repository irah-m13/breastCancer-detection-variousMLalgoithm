# -*- coding: utf-8 -*-
"""BreastCancerDetection_variousMLAlgo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GXo0589iXW46rc837MrKRgnoxtqLOl0y

Import libraries
"""

import pandas as pd #useful for loading dataset
import numpy as np # used to perform array
import matplotlib as pyplot

"""Load dataset from local directory"""

from google.colab import files
uploaded = files.upload()

"""Load and Summarize data"""

dataset= pd.read_csv('data.csv')

print(dataset.shape)
print(dataset.head(5))

"""Map class string value to numbers"""

dataset['diagnosis'] = dataset['diagnosis'].map({'B' : 0, 'M' : 1}).astype(int)
print(dataset.head(5))

"""Segregate Dataset into X(input) and Y(output)"""

x = dataset.iloc[:, 2:32].values
print(x)
y = dataset.iloc[:, 1].values
print(y)

"""Split into train and test"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =0.25, random_state = 0)

"""Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

"""Validating some Ml algorithm by accuracy"""

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

models = []
models.append(('LR', LogisticRegression(solver = 'liblinear', multi_class = 'ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier(n_neighbors = 6, p=2, metric ="minkowski", n_jobs=-1)))
models.append(('CART', DecisionTreeClassifier(max_depth = 600, criterion="gini")))
models.append(('NB', GaussianNB()))
models.append(('SVM',  SVC(kernel= "rbf", gamma = 'auto')))
models.append(('RF', RandomForestClassifier(n_estimators=22, criterion='entropy', bootstrap=False, random_state=0)))

result = []
names = []
res = []

for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=None)
    cv_result = cross_val_score(model, x_train, y_train, cv=kfold, scoring='accuracy')
    result.append(cv_result)
    names.append(name)
    res.append(cv_result.mean())
    print('%s: %f' % (name, cv_result.mean()))

pyplot.ylim((.900, .999))
pyplot.bar(names, res, color ='maroon', width = 0.6)

pyplot.title('Algorithm Comparison')
pyplot.show()

"""Training and prediction using algorithm with high accuracy"""

from sklearn.svm import SVC
model.fit(x_train , y_train)
y_pred = model.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test),1)),1))

