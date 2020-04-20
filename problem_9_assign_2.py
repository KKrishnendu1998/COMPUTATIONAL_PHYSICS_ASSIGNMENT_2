#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 9: Python code for solving initial value problem using 4th order Runge-Kutta method implementing 
adaptive step size control
Created on Sun Apr 12 08:46:07 2020

@author: krishnendu
"""

import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt
from scipy.integrate import *
def fun(y,t):               #defining function that returns derivative
   
    return (y**2+y)/t

def RK(h,t,w):              #function for 4th order Runge-Kutta method
    k1=h*fun(w,t)
    k2=h*fun(w+k1/2,t+h/2)
    k3=h*fun(w+k2/2,t+h/2)
    k4=h*fun(w+k3,t+h)
    w=w+1/6*(k1+2*k2+2*k3+k4)
    return w
    
d=0.0001         #accuracy 
a=1           #starting value
b=10          #end value
h=0.01        #initial step size
t=[a]         #creating array that stores the t value
w=[-2]        #creating array that stores y value
Flag=1
while(Flag==1):

    y=RK(h,t[len(t)-1],w[len(w)-1])    
    y1=RK(h,t[len(t)-1]+h,y)     #calculating the value of the  function at t_i + 2h using RK4 twice with step size h  
    
    
    y2=RK(2*h,t[len(t)-1],w[len(w)-1]) #calculating the value of the  function at t_i + 2h using RK4 once with step size 2h  
    
    h=h*(d*h*30/abs(y1-y2))**0.25    #calculating the perfect step size
    
    if(t[len(t)-1]+h>b):          #this if check whether the value of t crosses the valu of b or not.if it does cross the value of b it will evaluate the value at b instead of t_i+h
                                   
        h=b-t[len(t)-1]
        y=RK(h,t[len(t)-1],w[len(w)-1])    #calculating the value of y with the perfect step size
        t.append(b)       #appending the t values 
        w.append(y)        #appending the y values
        break
    y=RK(h,t[len(t)-1],w[len(w)-1])      #calculating the value of y with the perfect step size
   
    
    t.append(t[len(t)-1]+h)         #appending the t values 
    w.append(y)                      #appending the y values
    
   
    
    
plt.scatter(t,w,label="points obtained by adaptive step size")
plt.legend(loc="lower right")
plt.xlabel("t",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 9",size=18)
plt.grid()
plt.show()