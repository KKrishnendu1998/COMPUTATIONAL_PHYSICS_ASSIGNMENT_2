#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 7-a : Python code for solving initial value problems using scipy.integrate,solve_ivp . Also find
the nalytical solution of the probelm using Mathematica and plot it.
Created on Wed Apr  1 19:00:20 2020

@author: krishnendu
"""

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
def fun1(t,y):                   ##defining the function for derivative 
    return t*np.exp(3*t)-2*y
t=np.linspace(0,1,1000)           #creating mesh points
s=solve_ivp(fun1,[0,1],[0],dense_output="True")     #solving the probelm using solve_ivp 
plt.plot(t,s.sol(t).T,label='using soe_ivp')        #plotting the solution using solve_ivp
plt.plot(t,(1/25)*(np.exp(-2*t)-np.exp(3*t))+(1/5)*np.exp(3*t)*t,label='analytical')   #plotting the analytical solution
plt.legend()
plt.xlabel("t",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 7-a",size=18)
plt.grid()
plt.show()


