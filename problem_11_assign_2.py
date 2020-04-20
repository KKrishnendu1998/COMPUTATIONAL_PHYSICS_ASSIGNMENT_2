#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 10 : Python code for solving initial value problem using fourth order Runge-Kutta method
Created on Wed Apr  8 15:59:22 2020

@author: krishnendu
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt
from scipy.integrate import *
def fun(r,x):             #defining functions that returns derivatives
    p=np.zeros(3)
    p[0]=r[0]+2*r[1]-2*r[2]+np.exp(-x)
    p[1]=r[1]+r[2]-2*np.exp(-x)
    p[2]=r[0]+2*r[1]+np.exp(-x)
    return p
a=0     #starting value
b=1     #end value  
N=100   #number of mesh points
h=(b-a)/(N-1)  #step size
x=np.linspace(a,b,N)   #creating mesh points


w2=np.zeros(3*N)
w2=w2.reshape(3,N) 
w2[0,0] =3        #putting the initial condition 
w2[1,0]=-1         #putting the initial condition 
w2[2,0]=1          #putting the initial condition 

for i in range(N-1):                #iteration for Runge-Kutta method
    k1=h*fun(w2[:,i],x[i])
    k2=h*fun(w2[:,i]+k1/2,x[i]+h/2)
    k3=h*fun(w2[:,i]+k2/2,x[i]+h/2)
    k4=h*fun(w2[:,i]+k3,x[i]+h)
    w2[:,i+1]=w2[:,i]+1/6*(k1+2*k2+2*k3+k4)
    
plt.plot(x,w2[0,:],label=r"$u_1$")
plt.plot(x,w2[1,:],label=r"$u_2$")
plt.plot(x,w2[2,:],label=r"$u_3$")
plt.legend()
plt.xlabel("t",size=18)
plt.title("Problem 11",size=18)
plt.grid()
plt.show()