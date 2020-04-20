#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 5:Python code for solving boundary value problem using shooting method
Created on Sun Apr  5 17:04:12 2020

@author: krishnendu
"""

import numpy as np
from scipy.integrate import *
from scipy.optimize import *
import matplotlib.pyplot as plt
oldroot=10                      #taking a initial guess for 
tol=1
g=10        #value of g
def fun(y,t):                    #defining the function for derivatives
    return [y[1],-g]
t=np.linspace(0,10,100)          #creating mesh points
def ivp(k):                      #function for solving the initial value probelems for different values of initial velocity
    sol=odeint(fun,[0,k],t)
    return sol[99,0]
while(tol>0.01):
    newroot=newton(ivp,oldroot)    #iteration 
    tol=abs(newroot-oldroot)       
    oldroot=newroot
sol2=odeint(fun,[0,newroot],t)      #solving the initial value problem using the exact velocity that satisfies the boundary conditions
y=np.arange(newroot,newroot+12,2)   #candidate solutions
count=1
for i in (y):
    s=odeint(fun,[0,i],t)
    if(count==1):                  #this if loop is for labelling the candidate solution once
         plt.plot(t,s[:,0],"b-",label="candidate solutions")     #plotting the candidate solution
    
    plt.plot(t,s[:,0],"b-")             
    count+=1
z=np.linspace(0,100,10000)          #creating mesh points for numpy.argmin method
X=[]
for i in z:
    s1=odeint(fun,[0,i],t)
    X=np.append(X,s1[99,0])
print("the value of the initial velocity by argmin method :", z[np.argmin(abs(X))])   #printing the solution which I get using argmin 
plt.plot(t,sol2[:,0],"r-",label="actual")    #plotting the actual solution
plt.plot(t,50*t-1/2*g*t**2,"g-",label="true solution") 
plt.legend()   
plt.xlim(0,10) 
plt.xlabel("t",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 5-Shooting method",size=18)
plt.show()