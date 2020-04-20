#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 2: Python code for approximating solution of a initial value problem using Euler's method and 
compute the absolute and relative error in the solution using Euler's method. 
Created on Wed Apr  1 16:28:05 2020

@author: krishnendu
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt
from scipy.integrate import *
def fun(y,t):                      #defining the function for derivative 
    return y/t-(y/t)**2
a=1                               #starting point
b=2                               #ending point
h=0.1                              #step size
N=int((b-a)/h +1 )                 #calculating the number of mesh point
t=np.linspace(a,b,N)              #creating mesh point
w=np.zeros(N)
w[0]=1                           #putting the initial condition
for i in range(N-1):              #iteration
    w[i+1]=w[i]+h*fun(w[i],t[i])
true=t/(1+np.log(t))     #true solution
err=abs(w-true)          #calculating the relative error
abs_err=abs(err/true)     #calculating the absolute error
print("the relative errors are :",err)    #printing the relative error
print("the absolute errors are :",abs_err)   #printing the absolute error
plt.plot(t,w,label=" Euler method")
plt.plot(t,true,label="actual")
plt.legend(loc="best")
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 2",size=18)
plt.grid()

plt.show()