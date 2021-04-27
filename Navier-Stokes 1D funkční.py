# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:11:38 2021

@author: Ondra Zikmund
"""

import matplotlib.pyplot as plt


N = 9

L = 10

dx = L/(N+1)

dt = 0.1

C = 1/(4*dx)
E = 1/(2*dx**2)

X = []

T = 1

x = [0,0,1,5,1,30,3,1,1]

a = [i for i in range(len(x))]
for i in range(round(T/dt)):
    
    x_n = [0 for i in range(len(x))]
    
    for j in range(round(len(x)-2)):
         x_n[j+2] = (x_n[j+1]-x[j+1]-x[j+1]*C*(x[j+1]-x_n[j+2]-x[j])-E*(x_n[j+2]-2*x_n[j+1]+x[j]-2*x[j+1]+x[j+1]))/(x[j+1]*C+E*x_n[j+2]+0.00001)
    
    X.append(x)
    x = x_n
    plt.plot(a,x)


print(X)

