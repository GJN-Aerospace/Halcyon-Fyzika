# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:10:37 2021

@author: Ondra Zikmund
"""

import matplotlib.pyplot as plt
import numpy as np

l = 10
h = 0.01

Y = [5]
X = [0]

for i in range(round(l/h)):
    
    x = X[-1]
    y = Y[-1]
    
    k_1 = h*(x+y)*np.sin(x*y)
    
    k_2 = h*(x+h/2+y+k_1/2)*np.sin((x+h/2)*(y+k_1/2))
    
    k_3 = h*(x+h/2+y+k_2/2)*np.sin((x+h/2)*(y+k_2/2))
    
    k_4 = h*(x+h+y+k_3)*np.sin((x+h)*(y+k_3))
    
    y += 1/6*(k_1+2*k_2+2*k_3+k_4)
    
    X.append((i+1)*h)
    Y.append(y)
    
plt.plot(X,Y)

