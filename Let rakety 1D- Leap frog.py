# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 23:53:50 2021

@author: Ondra Zikmund
"""

def Leap_frog(y,v,a_1,dt):
    
    dv = a_1*dt
    dy = (v+dv)*dt
    
    y = y+dy
    v = v+dv
    
    return y,v
    
    

def Thrust(t):   # thrust force as a funtion of time
    if t>=0 and t<=0.7:
        th = 12.86*t
    if t>0.7 and t<=1:
        th = -20*t + 23
    if t>1 and t<=5.5:
        th = 3
    if t>5.5 and t<=6.25:
        th = -4*t+25
    if t>6.25:
        th = 0
    
    return th

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Rocket parameters
# =============================================================================
# All numbers are in S.I. units


m_m = 0.0167
I = 20  # total impuls

v_e = I/m_m   # velocity of products


r = 0.0625  # radius of the rocket
m = 0.239 # inital mass of the rocket with the motors
th = 0   # initial force of thrust
t_th = 9
a_th  = th/m  # acceleration due to thrust
g = 9.8  # gravitational acceleration, positive direction is oriented upward
dens = 1.225  # densitiy of air
c_d = 0.65 # drag coefficient of the rocket  0,35
S = r*r*3.14  # cross-sectional area of the rocket


#-------------------------------------------------#
# ROCKET SIMULATION
#-------------------------------------------------#


y = 0  # initial hight is 0
v = 0 # initial velociy is 0
t = 0
  
position = []  # vector of y values
velocity = []  # vector of v  values


dt = 0.01  # elementary time interval
n = round(t_th/dt)# number of intervals

T = np.array([i*dt for i in range(n+1)])
T_v = []
for i in T:
    T_v.append(i-dt/2)
#--------------------------------------------#
# Accelerating phase  (thrust accelerates the rocket)
#--------------------------------------------#

TH = [0]
V = [0]
Y = [0]
M = [0.239]


for interval in range(n):
        
    th = Thrust(t)
    TH.append(th)
    m -= dt*th/v_e  # as the rocket is burning fuel, it's mass decrease
    M.append(m)
    
    if V[-1]>0:
        k = +1/2*dens*c_d*S
    else:
        k = -1/2*dens*c_d*S
   
    a_th = Thrust(t)/m  # acceleration due to thrust
    a = a_th-g-k*v**2 # entire acceleration



    if a<=0 and y==0:
        
        y = 0
        v = 0
        Y.append(y)
        V.append(v)

    else:
        if len(V)==0:
            V.append(-dt*a/2)
        
        else:
            y +=v*dt
            v += a*dt
            
            Y.append(y)
            V.append(v)
            
    t +=dt

# =============================================================================
# Visualisation
# =============================================================================



plt.close()
print("The maximal height was:")
print(max(Y))
print("The maximal velocity was")
print(max(V))



plt.plot(T,TH, label = 'thrust')

plt.plot(T_v,V, label = 'velocity')  # Leap frog
plt.plot(T,Y, label = 'height')    # Leap frog

plt.title("Rocket flight", size=25)
plt.xlabel("time(s)")
plt.ylabel("Characteristics (SI)")

plt.legend(loc="lower center", bbox_to_anchor=(1, 1))

