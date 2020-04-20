#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 3: Python code for solving differential equation using Runge-Kutta method
Created on Wed Apr  1 16:58:45 2020

@author: krishnendu
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt
from scipy.integrate import *
def fun(r,x):                    #defining the function for derivative 
    p=np.zeros(2)
    p[0]=r[1]
    p[1]=2*r[1]-r[0]+x*np.exp(x)-x
    return p
a=0                  #starting point
b=1                  #ending point
N=1000        #number of mesh points
x=np.linspace(a,b,N)         #creating mesh points
h=(b-a)/(N-1)   #step size


w=np.zeros(2*(N))
w=w.reshape(2,N) 
w[[0,0] ,[1,0]]=[0,0]   #putting the initial conditions
for i in range(N-1):     #iteration
    k1=h*fun(w[:,i],x[i])
    k2=h*fun(w[:,i]+k1/2,x[i]+h/2)
    k3=h*fun(w[:,i]+k2/2,x[i]+h/2)
    k4=h*fun(w[:,i]+k3,x[i]+h)
    w[:,i+1]=w[:,i]+1/6*(k1+2*k2+2*k3+k4)
    
plt.plot(x,w[0,:],label=" Euler method")
plt.legend(loc="best")
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 3",size=18)
plt.grid()

plt.show()