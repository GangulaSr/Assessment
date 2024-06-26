# -*- coding: utf-8 -*-
"""LVADSUSR85_Sravanthi_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MXa1pdr_q5SdyiBCZfR1gMcCQCvq_Pmg
"""

#1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.metrics import stats

df = pd.read_csv('/content/booking.csv')

print(df.describe(),end='\n\n')
print(df.info(),end='\n\n')
print(df.isnull().sum(),end='\n\n')


plt.boxplot(df['lead time'])
plt.show()


Q1 = df['lead time'].quantile(0.25)
Q3 = df['lead time'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - (1.5*IQR)
upper_limit = Q3 + (1.5*IQR)
df = df[~(df['lead time'] < lower_limit) | (df['lead time'] > upper_limit)]

#2

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['room type'] = le.fit_transform(df['room type'])
df['type of meal'] = le.fit_transform(df['type of meal'])
df['booking status'] = le.fit_transform(df['booking status'])
df['market segment type'] = le.fit_transform(df['market segment type'])

print(df.head(20))

#3

features = df[['number of adults',	'number of children',	'number of weekend nights',
               'number of week nights',	'type of meal',	'car parking space',	'room type',
               'lead time',	'market segment type',	'repeated',	'P-C',	'P-not-C',	'average price',
               'special requests']]
labels = df['booking status']

df.duplicated().sum()
df.drop_duplicates()

import seaborn as sns

sns.heatmap(df.corr(),annot=True)

#4

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(features,labels,test_size=0.3)

#5

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf = clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)

#6

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix


acc = accuracy_score(y_test,y_pred)
print("accuracy: ",acc)

precision = precision_score(y_test, y_pred)
print("precision: ",precision)

recall = recall_score(y_test, y_pred)
print("recall: ",recall)

f1 = f1_score(y_test, y_pred)
print("f1: ",f1)

conf_matrix = confusion_matrix(y_test, y_pred)
print("conf_matrix: ",conf_matrix)