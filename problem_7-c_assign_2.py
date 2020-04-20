#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python code for solving initial value problems using scipy.integrate,solve_ivp . Also find
the nalytical solution of the probelm using Mathematica and plot it.
Created on Thu Apr  2 17:19:18 2020

@author: krishnendu
"""

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
def fun(t,y):                          #defining the function for the derivative 
    return 1+(y/t)
t=np.linspace(1,2,1000)                #creating mesh points
sol=solve_ivp(fun,[1,2],[2],dense_output="True")     #solving the problem using solve_ivp
plt.plot(t,sol.sol(t).T,label='solve_ivp')             #plotting the solution using solve_ivp
plt.plot(t,t*(2+np.log(t)),label='analytical')          #plotting the analytical solution
plt.legend()
plt.xlabel("t",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 7-c",size=18)
plt.grid()
plt.show()
