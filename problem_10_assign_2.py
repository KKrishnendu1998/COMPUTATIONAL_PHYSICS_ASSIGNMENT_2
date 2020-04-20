#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 10 : Python code for solving initial value problem using fourth order Runge-Kutta method and finding 
the solution at a particular value of t 

@author: krishnendu
"""
#Method 1 : by changing variable t=tan(z)
import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt
from scipy.integrate import *

def RK(h,t,w,fun):              #function for 4th order Runge-Kutta method
    k1=h*fun(w,t)
    k2=h*fun(w+k1/2,t+h/2)
    k3=h*fun(w+k2/2,t+h/2)
    k4=h*fun(w+k3,t+h)
    w=w+1/6*(k1+2*k2+2*k3+k4)
    return w






def fun1(x,y):             #defining function for the derivative
   
    return 1/( ( (np.cos(y))**2) * (x**2 + (np.tan(y))**2 ))

a1=0      #starting value
b1=(np.pi)/2  #ending value
h1=0.001 #step size
N1=int((b1-a1)/h1+1)    #number of mesh points
z=np.linspace(a1,b1,N1)  #creating mesh points
        


w1=np.zeros(N1)
w1[0]=1     #putting the initial condition

for i in range(N1-1):      #iteration for RK-4 method
    w1[i+1]=RK(h1,z[i],w1[i],fun1)
    
print("The value of x at t=3.5*10^6 :",w1[np.argmin(abs(z-np.arctan(3.5*10**6)))])   #printing the value of the solution at t=3.5*10^6 

plt.plot(np.tan(z),w1)    #plotting x vs t graph 
plt.xlabel("x",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 10 ,method 1",size=18)

plt.show()


#Method 2: by adaptive step size control

def fun2(x,t):               #defining function that returns derivative
   
    return 1/(x**2+t**2)

def RK(h,t,w,fun):              #function for 4th order Runge-Kutta method
    k1=h*fun(w,t)
    k2=h*fun(w+k1/2,t+h/2)
    k3=h*fun(w+k2/2,t+h/2)
    k4=h*fun(w+k3,t+h)
    w=w+1/6*(k1+2*k2+2*k3+k4)
    return w
    
d=0.00001         #accuracy 
a2=0           #starting value
b2=10**8         #end value
h2=0.01        #initial step size
t=[a2]       #creating array that stores the t value
w2=[1]        #creating array that stores y value
Flag=1
p=3.5*10**6
count=0
while(Flag==1):

    y=RK(h2,t[len(t)-1],w2[len(w2)-1],fun2)    
    y1=RK(h2,t[len(t)-1]+h2,y,fun2)     #calculating the value of the  function at t_i + 2h using RK4 twice with step size h  
    
    
    y2=RK(2*h2,t[len(t)-1],w2[len(w2)-1],fun2) #calculating the value of the  function at t_i + 2h using RK4 once with step size 2h  
    
    h2=h2*(d*h2*30/abs(y1-y2))**0.25    #calculating the perfect step size
    
    if(t[len(t)-1]+h2>p and count==0):          #this if check whether the value of t crosses the valu of p or not.if it does cross the value of b it will evaluate the value at p instead of t_i+h
                                   
        h2=p-t[len(t)-1]
        y=RK(h2,t[len(t)-1],w2[len(w2)-1],fun2)    #calculating the value of y with the perfect step size
        t.append(p)       #appending the t values 
        w2.append(y)        #appending the y values
        count+=1
    y=RK(h2,t[len(t)-1],w2[len(w2)-1],fun2)      #calculating the value of y with the perfect step size
   
    if(max(t)>b2):                   #if t crosses the loop will terminate
        break
    t.append(t[len(t)-1]+h2)         #appending the t values 
    w2.append(y)                      #appending the y values
    
   
print("The value of x at t=3.5*10^6 :",w2[t.index(p)])     #printing the value of x at t=3.5*10^6
   
plt.plot(t,w2)          #plotting the x vs t graph 
plt.xlabel("t",size=18)
plt.ylabel("y",size=18)
plt.title("Problem 10,method 2",size=18)
plt.grid()
plt.show()