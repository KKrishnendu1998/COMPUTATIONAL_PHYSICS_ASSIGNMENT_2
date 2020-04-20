#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python code for solving initial value problems using scipy.integrate,solve_ivp . Also find
the nalytical solution of the probelm using Mathematica and plot it.
Created on Thu Apr  2 17:22:29 2020

@author: krishnendu
"""

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
def fun(t,y):                   #defining the function for the derivative
    return np.cos(2*t)+np.sin(3*t)
t=np.linspace(0,1,1000)          #creating mesh points
s=solve_ivp(fun,[0,1],[1],dense_output="True")    #solving the problem using solve_ivp
plt.plot(t,s.sol(t).T,label='solve_ivp')   #plotting the solution using solve_ivp
plt.plot(t,1/6*(8-2*np.cos(3*t)+3*np.sin(2*t)),label='analytical')    #plotting the analytical solution
plt.legend()
plt.xlabel("t",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 7-d",size=18)
plt.grid()
plt.legend()
plt.show()
