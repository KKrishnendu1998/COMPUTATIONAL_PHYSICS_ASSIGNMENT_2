#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 6 :Python code for solving boundary value problem using Relaxation method
Created on Mon Apr  6 01:29:45 2020

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt
N=32     #number of mesh points
a=0      #starting value
b=10     #end value
g=10     #value of g
h=(b-a)/(N-1)    #step size
t=np.linspace(a,b,N)  #creating mesh points
n=N-2        #the sizedof the matrix to be solves
a=np.zeros(n**2).reshape(n,n)
for i in range(n):      #forming the a matrix
        if(i==0 ):
            a[i][i]=-2
            a[i][i+1]=1
        elif (i==n-1):
            a[i][i]=-2
            a[i][i-1]=1
        else:
            a[i][i-1]=1
            a[i][i+1]=1
            a[i][i]=-2          
b=np.zeros(n)
for i in range(n):    #forming the b matrix
    b[i]=-(h**2)*g
xa=0       # boundary value at x=a
xb=0       #boundary value at x=b
b[0]=-(xa+g)*h**2        #putting the boundary value
b[n-1]=-(xb+g)*h**2      #putting the boundary value


def gauss_seidel(x):      #function for Gauss-seidel method
    p=np.copy(x)
    x=np.zeros(n)
    for j in range(len(x)):
       
       for k in range(len(x)):
           if k<j :
               x[j]=x[j]-(a[j][k]*x[k])
           if k>j:
                x[j]=x[j]-(a[j][k]*p[k])
             
       
       x[j]=(x[j]+b[j])/a[j][j]
    return x

X=[]
x=np.zeros(n)
Flag=1
c=0
err=0.1
while(Flag==1):
    z=np.zeros(N)
    for i in range(n):          #creating the full matrix of size N from the solution of the matrix of size n 
        z[i+1]=x[i]           
    z[0]=xa              #inserting the boundary value at x=a to the solution
    z[n+1]=xb            #inserting the boundary value at x=b to the solution
    X.append(z)
    p=np.copy(x)
    x=gauss_seidel(x)
    if(np.all(abs(x-p))<err):     #checking the error 
        break
    
    c+=1
    

plt.plot(t,X[c],"r-",label="actual solution")              #plotting the actual solution 
plt.plot(t,50*t-1/2*g*t**2,"g-",label="true solution")   
plt.plot(t,X[int(c/10)],"b-",label="candidate solutions")      #plotting the candidate solution
plt.plot(t,X[int(c/15)],"b-")       #plotting the candidate solution
plt.plot(t,X[int(c/20)],"b-")      #plotting the candidate solution      
plt.plot(t,X[int(c/25)],"b-")       #plotting the candidate solution
plt.plot(t,X[int(c/30)],"b-")       #plotting the candidate solution
plt.legend()
plt.xlabel("x",size=18)
plt.ylabel("t",size=18)
plt.title("Problem 6-Relaxation method",size=18)
plt.show()
