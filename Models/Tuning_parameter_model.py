# -*- coding: utf-8 -*-
"""
Created on Wed May 19 16:54:51 2021

@author: nowshin
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import ElasticNetCV
from sklearn.metrics import *
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report, confusion_matrix
#%%

xls = pd.ExcelFile('dataset.xlsx')
X = pd.read_excel(xls, 'X', header=None)
y = pd.read_excel(xls, 'y', header=None)
y= np.ravel(y)

#%%
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=42)

#%%
logreg = LogisticRegression(solver = "saga", penalty='elasticnet', C=1, max_iter=1000, 
                            class_weight='balanced', multi_class='auto', l1_ratio=0.1)
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)
print("Accuracy: ( Logictic regression : )",metrics.accuracy_score(y_test, y_pred)*100)
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)

#plotting the confusion matrix 
plt.figure(figsize=(12,12))
sns.heatmap(cnf_matrix, annot=True, annot_kws={"size": 16},cmap='Blues', fmt='g')
plt.ylabel("Predicted class")
plt.xlabel("Actucal class")
plt.show()

#%%
from sklearn import svm
clf = svm.SVC(kernel='rbf', C=10.0, gamma='scale' , decision_function_shape='ovr',class_weight='balanced')

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy: SVM : ",metrics.accuracy_score(y_test, y_pred)*100)
from sklearn import metrics
cnf_matrix_svc = metrics.confusion_matrix(y_test, y_pred)
print("Confusion matrix using SVM")

#plotting the confusion matrix 
plt.figure(figsize=(12,12))
sns.heatmap(cnf_matrix_svc, annot=True, annot_kws={"size": 16},cmap='Greens', fmt='g')
plt.ylabel("Predicted class")
plt.xlabel("Actucal class")
plt.show()

#%%



