#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python code for solving boundary value problems using scipy.integrate,solve_bvp . Also find
the nalytical solution of the probelm using Mathematica and plot it.
Created on Sun Apr 12 20:23:22 2020

@author: krishnendu
"""

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
a=0                         #starting value 
b=np.pi                     #end value
def fun(x,y):               #function that returns the derivative 
    return np.vstack((y[1],1/2*(1-y[1]**2-y[0]*np.sin(x))))
def bc(ya,yb):              #function that returns the derivative 
    return np.array([ya[0]-2,yb[0]-2])
x=np.linspace(a,b,100)           #creating mesh points
y=np.zeros((2,x.size))
y[0]=1                             #initial guess of the solution
sol=solve_bvp(fun,bc,x,y)            #solving the problem using solve_bvp
y1=np.loadtxt("bvp4.txt",usecols=0)    #importing the text file containing the solution using Mathematica
plt.plot(x,y1,label="analytical")        #plotting the analytical solution
plt.plot(x,sol.sol(x)[0],label="solve-bvp")     #plotting the solution using solve_bvp
plt.legend()
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 8-d",size=18)
plt.grid()
plt.show()