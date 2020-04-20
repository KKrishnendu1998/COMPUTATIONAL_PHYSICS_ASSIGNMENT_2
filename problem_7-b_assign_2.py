#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python code for solving initial value problems using scipy.integrate,solve_ivp . Also find
the nalytical solution of the probelm using Mathematica and plot it.
Created on Thu Apr  2 17:17:42 2020

@author: krishnendu
"""
import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
def fun(t,y):                   #defining function for the derivative 
    return 1-(t-y)**2
t=np.linspace(2,2.99,1000)       #creating mesh points.sice at t=3 the solution diverges,we have plotted it upto t=2.99
sol=solve_ivp(fun,[2,2.99],[1],dense_output="True")    #solving the problem using solve_ivp
plt.plot(t,sol.sol(t).T,label='solve_ivp')             #plotting the solution using solve_ivp
T=np.linspace(2,2.99,100)
plt.plot(T,(1-3*T+T**2)/(-3+T),label='analytical')   #plotting the analytical solution
plt.legend()
plt.xlabel("t",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 7-b",size=18)
plt.grid()
plt.show()
