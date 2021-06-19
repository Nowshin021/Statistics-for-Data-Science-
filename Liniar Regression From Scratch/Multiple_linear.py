# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:16:02 2021

@author: nowshin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

#%%
def transpose_Nazia(X):
    return  X.T

#%%
def MatrixMultiply_Nazia(a,b):
    return a.dot(b)

#%%
def Inverse_Nazia(a):
    return np.linalg.inv(a)
#%%

def find_prediction_Nazia(X, Y , W):
    
    y_prediction=[]
    for i in range(len(Y)):
        a=W[0]
        for j in range(1,len(W)):
            a = a+ W[j] * X.values[i][j]
        y_prediction.append(a)
    
    y_prediction_val = np.array(y_prediction)
    
    return y_prediction_val

#%%
def findMSE_Nazia(y_prediction_val , Y):
    y_test =np.array(Y)

    y_cap=[]
    for i,j in zip(y_prediction_val , y_test):
        y_cap.append((i-j)**2)
    
    y_cap=np.array(y_cap)
    msc = sum(y_cap)/float(len(y_cap))
    return msc
    
#%%
def findRMSC_Nazia(msc):
    return math.sqrt(msc)

#%%
def findMAE_Nazia(y_prediction_val,Y):
    
    y_cap_2=[]
    y_test=np.array(Y)
    for i , j in zip(y_prediction_val,y_test):
        y_cap_2.append(abs(i-j))

    mae= sum(y_cap_2)/ float(len(y_cap_2))
    return mae

#%%
def findRsquare_Nazia(y_prediction_val,Y):
#R square 
    numerator=[]
    y_test=np.array(Y)
    y_test_mean =sum(y_test)/float(len(y_test))
    for i , j in zip(y_test ,y_prediction_val):
        numerator.append(((i - j)**2))
    
    numerator=np.array(numerator)
    denominator=[((i - y_test_mean)**2) for i in y_test]
    denominator=np.array(denominator)

    r_square =(1-(sum(numerator)/sum(denominator))) 

    return r_square


#%%    
def plot_graph_Nazia(X,y_prediction_val,Y):

    plt.figure (figsize=(20,10), dpi = 80)
    
    plt.subplot(2,2,1)
    
    plt.grid(color='grey')
    plt.scatter(X['Length'], Y, color='#5094d9', marker='+', label='Test values')
    plt.scatter(X['Length'],y_prediction_val,  marker='>',color='navy', label = 'predicted values')
    plt.xlabel('Length', size=12)
    plt.ylabel("Number of rings", size =12)
    plt.legend(fontsize=15,loc="upper left")
    
    plt.subplot(2,2,2)
    
    plt.grid(color='grey')
    plt.scatter(X['Height'], Y, color='#5094d9', marker='+', label='Test values')
    plt.scatter(X['Height'],y_prediction_val, marker='>',color='firebrick', label = 'predicted values')
    plt.xlabel('Height', size=12)
    plt.ylabel("Number of rings", size =12)
    plt.legend(fontsize=15,loc="upper left")

    plt.subplot(2,2,3)
    
    plt.grid(color='grey')
    plt.scatter(X['Diameter'], Y, color='#5094d9', marker='+', label='Test values')
    plt.scatter(X['Diameter'],y_prediction_val, marker='>', color='forestgreen', label = 'predicted values')
    plt.xlabel('Diameter', size=12)
    plt.ylabel("Number of rings", size =12)
    plt.legend(fontsize=15,loc="upper left")
    

    plt.subplot(2,2,4)
    
    plt.grid(color='grey')
    plt.scatter(X['Whole Weight'], Y, color='#5094d9', marker='+', label='Test values')
    plt.scatter(X['Whole Weight'],y_prediction_val, marker='>', color='indigo', label = 'predicted values')
    plt.xlabel('Whole Weight', size=12)
    plt.ylabel("Number of rings", size =12)
    plt.legend(fontsize=15,loc="upper left")
    
    plt.show()
#%%
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
def plot_graph_3d_Nazia(X,Y):
    

    
    fig = plt.figure(figsize = (20, 10))
   
    ax = plt.axes(projection ="3d")
    x1=X['Diameter']
    x2=X['Height']
    x3=Y
    plt3d=ax.scatter3D(x1, x2, x3, c=x3,  marker='^', cmap='coolwarm')
    ax.set_xlabel('$Diameter$', fontsize=12)
    ax.set_ylabel('$Height$', fontsize=12)
    ax.set_zlabel('$Rings$', fontsize=12)
    ax.set_title("3D plot of influential independent variable Diameter, Height with dependent variable Rings")
    cbar = fig.colorbar(plt3d,ax=ax)
    cbar.set_label("Number of rings")
    
    
    plt.show()

#%%  
import matplotlib.cm as cm
def plot_utility_Nazia(X,Y):
    plt.figure (figsize=(30,15))
    plt.subplot(2,2,1)
    plt.title("Scatter co relation (Length vs Rings)",fontsize=25)
    t=X['Length']
    plt.scatter(X['Length'], Y, marker='>', c=t, cmap='inferno')
    plt.grid(color='grey')
    plt.xlabel("Length",size=18)
    plt.ylabel("Rings" , size=18)
    
    
    plt.subplot(2,2,2)
    plt.title("Scatter co relation (Height vs Rings)",fontsize=25)
    u=X['Height']
    plt.scatter(X['Height'], Y, c=u ,cmap='magma', marker='_')
    plt.grid(color='grey')
    plt.ylabel("Rings" , size=18)
    plt.xlabel("Length",size=18)
    
    
    plt.subplot(2,2,3)
    plt.title("Scatter co relation (Diameter vs rings)",fontsize=25)
    v=X['Diameter']
    plt.scatter(X['Diameter'], Y, c=v, marker='*',cmap='viridis' )
    plt.grid(color='grey')
    plt.ylabel("Rings" , size=18)
    plt.xlabel("Diameter",size=18)
    
    
    plt.subplot(2,2,4)
    plt.title("Scatter co relation (Whole Weight vs Rings)", fontsize=25)
    w=X['Whole Weight']
    plt.scatter(X['Whole Weight'], Y,c=w,cmap='plasma', marker='^')
    plt.grid(color='grey')
    plt.ylabel("Rings" , size=18)
    plt.xlabel("Whole Weight",size=18)
    plt.show()
    
    
#%%

def multivariate_liniar_model_Nazia():
    #multivariant regression 
    abalone=pd.read_csv('abalone.csv')
    abalone.columns=['Sex','Length','Diameter','Height', 'Whole Weight', 'Shucked Weight', 
                     'Viscera Weight', 'Shell Weight', 'Rings']
    bias_list=[1 for i in range(len(abalone.index))]
    abalone['bias_value'] = bias_list
    abalone_X=abalone[['bias_value', 'Length','Diameter', 'Height' , 'Whole Weight']]
    abalone_Y = abalone[['Rings']]
    X=abalone_X.iloc[:2000]
    Y=abalone_Y.iloc[:2000]


    #Calculating prediction
    trans_x = transpose_Nazia(X)
    xT_dot_x = MatrixMultiply_Nazia(trans_x,X)
    inverse = Inverse_Nazia(xT_dot_x)
    xT_dot_y = MatrixMultiply_Nazia(trans_x,Y)
    W = MatrixMultiply_Nazia(inverse,xT_dot_y)

    #prediction values
    y_prediction_val=find_prediction_Nazia(X,Y,W)

    #Model Evaluation
    msc = findMSE_Nazia(y_prediction_val, Y)
    rmsc = findRMSC_Nazia(msc)
    mae=findMAE_Nazia(y_prediction_val,Y)
    R_sqr = findRsquare_Nazia(y_prediction_val, Y)

    print("Model evaluation : ")
    print("MSC : ", msc)
    print("RMSC : ", rmsc)
    print("MAE : ", mae)
    print("R square : ", R_sqr)
   
    

    plot_graph_Nazia(X,y_prediction_val,Y)
    plot_graph_3d_Nazia(X,Y)
    plot_utility_Nazia(X,Y)

    
#%%
multivariate_liniar_model_Nazia()


