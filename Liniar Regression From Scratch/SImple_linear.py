# -*- coding: utf-8 -*-
"""
Created on Sat May  1 00:25:17 2021

@author: nowshin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

#%%
print("Reg plot on Y=a+bx : \n")
df=pd.read_csv('power_usage.csv')
prod = df['Production']
usage = df['Electricity usage']

#%%
def find_mean_Nazia(a):
     mean = sum(a)/float(len(a))
     return mean
    
#%%
def find_var_Nazia(x):
    n=len(x)
    mean_x = sum(x)/float(len(x))
    sub_x = [ (i - mean_x) for i in x]
    
    var=0
    for i in range(len(x)):
        var = var + (x[i]-mean_x)**2
    var_x=var/(len(x)-1)
    
    return var_x

#%%

def find_covar_Nazia(x,y):
    
    n=len(x)
    mean_x =find_mean_Nazia(x) 
    mean_y = find_mean_Nazia(y)
    sub_x = [ (i - mean_x) for i in x]
    sub_y = [ (i - mean_y) for i in y]

    #Covariance X Y :
    s = 0
    n = len(x)
    for i in range(0, n):
        s += (x[i] - mean_x) * (y[i] - mean_y)
     
    covar =  s / (n - 1)
    
    return covar

#%%
def show_eqn_Nazia(x , y):
    covar = find_covar_Nazia(x,y)
    
    var_x = find_var_Nazia(x)
    mean_y=find_mean_Nazia(y)
    mean_x=find_mean_Nazia(x)
    
    b=covar/var_x
    a= mean_y - b * mean_x
    return a,b
    

#%%
def find_msc_Nazia(x,y):
    
    Y=show_eqn_Nazia(x,y)
    a=Y[0]
    b=Y[1]
    
    #MSC
    y_cap =[(a + (b*i)) for i in x]
    y_minus_y_cap=[]
    for i, j in zip(y , y_cap):
        y_minus_y_cap.append((i-j))
    
    numerator = [(i**2) for i in y_minus_y_cap]
   
    msc = sum(numerator) / len(y)
    return msc
#%%
def find_rmsc_Nazia(msc):
    return math.sqrt(msc)

#%%
def find_mae_Nazia(x,y):
    Y=show_eqn_Nazia(x,y)
    a=Y[0]
    b=Y[1]
    
    #MAE
    y_cap =[(a + (b*i)) for i in x]
    y_minus_y_cap=[]
    for i, j in zip(y , y_cap):
        y_minus_y_cap.append(abs(i-j))
    
    
    mae = sum(y_minus_y_cap) / len(y)
    return mae 


#%%
def find_r_sqr_Nazia(x,y):
    Y=show_eqn_Nazia(x,y)
    a=Y[0]
    b=Y[1]
    mean_y=find_mean_Nazia(y)
    
    #MSC
    y_cap =[(a + (b*i)) for i in x]
    y_minus_y_cap=[]
    for i, j in zip(y , y_cap):
        y_minus_y_cap.append((i-j))
    
    numerator = [(i**2) for i in y_minus_y_cap]
    denominator = [((i-mean_y)**2) for i in y]
    
    
    R=(1-(sum(numerator)/sum(denominator)))
    
    return R

#%%
        
def Simple_Liniar_regression_Nazia(x,y):
    #Y=a+bx
    Y=show_eqn_Nazia(x,y)
    a=Y[0]
    b=Y[1]
    
    #msc, rmsc, mae, R_square
    msc  = find_msc_Nazia(x,y)
    rmsc = find_rmsc_Nazia(msc)
    mae  = find_mae_Nazia(x,y)
    R    = find_r_sqr_Nazia(x,y)
    
    #covariance and variance
    cov =find_covar_Nazia(x,y)
    v   =find_var_Nazia(x)  
    
    
    print("Some sttistical measures : ")
    print()
    
        
    print("Covariance : X and Y : ",cov)
    print("Variance of x : ", v)
    print()
    
    print("Coefficiants  a and b ", )
    print('b ==' , b)
    print('a == ', a)
   
    print()
    print("MSC : " , msc)
    print("RMSC : ", rmsc)
    print("MAE : ",   mae)
    
    print()
    print("R square --> ", R)
    prediction=[a + (b*i) for i in x]
    plot_graph(x,y , prediction)
    
    
#%%
def plot_graph(x,y,prediction):
    plt.figure(figsize=(15,8))
    #graph ploting :
    plt.subplot(1,2,1)
    plt.title("Regression : Test dataset")
    plt.scatter(x,y, marker='*', label ="Test values ")
    plt.plot(x,prediction, color='r', label="Predicted values")
    plt.xlabel("Production of electricity ", size = 12)
    plt.ylabel("Electricity usage ", size = 12)
    plt.grid()
    plt.legend(loc='upper left', fontsize=15)
    
    plt.subplot(1,2,2)
    
    plt.title("Regression : Trained dataset")
    plt.scatter(x,prediction, marker='o',color='g', label ="Trained values ")
    plt.plot(x,prediction, color='orange', label="Predicted values")
    plt.xlabel("Production of electricity ", size = 12)
    plt.ylabel("Electricity usage ", size = 12)
    plt.grid()
    plt.legend(loc='upper left', fontsize=15)
    
    

    
    plt.show()
  
    
#%%
#main function calling :
x=prod
y=usage
Simple_Liniar_regression_Nazia(x,y)


