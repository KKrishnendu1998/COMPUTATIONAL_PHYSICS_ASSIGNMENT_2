#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python code for solving initial value problem using Euler's method
Created on Wed Apr  8 16:31:19 2020

@author: krishnendu
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt
from scipy.integrate import *
def fun(r,t):              #defining the function that returns derivative
    p=np.zeros(2)
    p[0]=r[1]
    p[1]=2*r[1]/t-2*r[0]/t**2+t*np.log(t)
    return p
a=1    #starting value
b=2    #end value
h=0.001      # step size
N=int((b-a)/h +1)    #number of  mesh points

t=np.linspace(a,b,N)    #creating mesh points

w2=np.zeros(2*N)
w2=w2.reshape(2,N) 
w2[0,0]=1         #putting initial conditions
w2[1,0]=0         #putting initial conditions

for i in range(N-1):           #iteration for Euler's method
    k=h*fun(w2[:,i],t[i])
    w2[:,i+1]=w2[:,i]+k
    
plt.plot(t,w2[0,:],label=" Euler method")       #plotting the solution obtained using Euler's method
plt.plot(t,7*t/4+(t**3)*np.log(t)/2-3*(t**3)/4,label="actual")   #plotting the actual solution
plt.legend(loc="best")
plt.xlabel("t",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 13",size=18)
plt.grid()
plt.show()