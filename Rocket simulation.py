# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:40:15 2021

@author: Ondra Zikmund
"""


def Runge_kutta4(y,v,a_1,a_2,a_3,dt):
    
    j_1 = dt*(a_1)
    k_1 = dt*v
    
    j_2 = dt*(a_2)
    
    k_2 = dt*(v+j_1/2)
    
    j_3 = dt*(a_2)
    k_3 = dt*(v+j_2/2)
    
    j_4 = dt*(a_3)
    k_4 = dt*(v+j_2)
    
    dy = 1/6*(k_1+2*k_2+2*k_3+k_4)
    dv = 1/6*(j_1+2*j_2+2*j_3+j_4)
    
    y = y+dy
    v = v+dv
    
    return y,v

def Forward_Euler(y,v,a_1,dt):
    
    dy = v*dt
    dv = a_1*dt
    
    y = y+dy
    v = v+dv
    
    return y,v

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

#--------------------------------------------#
# Accelerating phase  (thrust accelerates the rocket)
#--------------------------------------------#

TH = [0]
T = [0]
T1 = [0]
T2 = [0]
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
   
    a_th1 = Thrust(t)/m  # acceleration due to thrust
    a_th2 = Thrust(t+dt)/m
    a_th3 = Thrust(t+2*dt)/m
    

    a_1 = a_th1-g-k*v**2 # entire acceleration
    a_2 = a_th2-g-k*v**2 # entire acceleration
    a_3 = a_th3-g-k*v**2 # entire acceleration


    if a_1<=0 and y==0:
        
        y = 0
        v = 0
        Y.append(y)
        V.append(v)

    else:
     #   y = Runge_kutta4(y,v,a_1,a_2,a_3,dt)[0]
        #y = Forward_Euler(y,v,a_1,dt)[0]
        y = Leap_frog(y,v,a_1,dt)[0]
        Y.append(y)
        
       # v = Runge_kutta4(y,v,a_1,a_2,a_3,dt)[1]
        #v = Forward_Euler(y,v,a_1,dt)[1]
        v = Leap_frog(y,v,a_1,dt)[1]
        V.append(v)
    t +=dt
    T1.append(2*dt*interval)   # time for Leap frog scenario
    T2.append(2*dt*interval+dt) # time for Leap frog scenario
    T.append(t)


# =============================================================================
# Visualisation
# =============================================================================

plt.close()
print("The maximal height was:")
print(max(Y))
print("The maximal velocity was")
print(max(V))

#plt.plot(T,V, label = 'velocity')  # Runge-Kutta and forward Euler
#plt.plot(T,Y, label = 'height')    # Runge-Kutta and forward Euler
plt.plot(T,TH, label = 'thrust')

plt.plot(T1,V, label = 'velocity')  # Leap frog
plt.plot(T2,Y, label = 'height')    # Leap frog

plt.title("Rocket flight", size=25)
plt.xlabel("time(s)")
plt.ylabel("Characteristics (SI)")

plt.legend(loc="lower center", bbox_to_anchor=(1, 1))



