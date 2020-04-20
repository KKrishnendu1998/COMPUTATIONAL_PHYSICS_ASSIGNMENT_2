#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 1:Python code for solving initial value problem using backward integration with Euler's method
Created on Wed Apr  1 13:28:50 2020

@author: krishnendu
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt
from scipy.integrate import *
#Problem 1: 
def fun1(y):                          #defining the function for derivative 
    return -9*y

def func1(x,y):                        #defining the function for doing the implicit Euler's method
    return x-y-h1*fun1(x)

a1=0             #starting point                         
b1=1              #ending point
N1=100         #number of mesh points
x1=np.linspace(a1,b1,N1)                  #creating mesh point
h1=(b1-a1)/(N1-1)   #step size
w1=np.zeros(N1)
f1=np.zeros(N1)
w1[0]=np.exp(1)                  #putting the initial condition
f1[0]=np.exp(1 )                    #putting the initial condition
for i in range(N1-1):                  #iteration 
    f1[i+1]=f1[i]+h1*fun1(w1[i])   #finding the guess value for implicit Euler's method using explicit Euler's method
    
    w1[i+1]=newton(func1,f1[i+1],args=(w1[i],))   #finding the value of y

plt.plot(x1,w1,label="Implicit Euler's method")    
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 1-(a)",size=18)
plt.legend()
plt.grid()
plt.show()

#Problem 2:                     #defining the function for derivative 

a2=0             #starting point                         
b2=1              #ending point
N2=100         #number of mesh points
x2=np.linspace(a2,b2,N2)                  #creating mesh point
h2=(b2-a2)/(N2-1)   #step size

def fun2(y,x):                      #defining the function for derivative 
    return -20*(y-x)**2+2*x

def func2(x,y,z):                       #defining the function for doing the implicit Euler's method
    return x-y-h2*fun2(x,z)

w2=np.zeros(N2)
f2=np.zeros(N2)
w2[0]=1/3                              #putting the initial value
f2[0]=1/3                                #putting the initial value
for i in range(N2-1):                    #iteration
    f2[i+1]=f2[i]+h2*fun2(w2[i],x2[i])     #finding the guess value for implicit Euler's method using explicit Euler's method
    
    w2[i+1]=newton(func2,f2[i+1],args=(w2[i],x2[i+1],))  #finding value of y
    
plt.plot(x2,w2,label="Implicit Euler's method")
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 1-(b)",size=18)
plt.legend()
plt.grid()
plt.show()