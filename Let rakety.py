# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:45:57 2020

@author: Ondra Zikmund
"""

import matplotlib.pyplot as plt

#-------------------------------------------------#
# ROCKET SIMULATION
#-------------------------------------------------#

# All numbers are in S.I. units

# Motor parameters

m_m = 0.0167
I = 20  # total impuls

v_e = I/m_m   # velocity of products


r = 0.0625  # radius of the rocket
mass_r = 0.239 # inital mass of the rocket with the motors
th = 0   # initial force of thrust
t_th = 9
a_th  = th/mass_r  # acceleration due to thrust
g = -9.8  # gravitational acceleration, positive direction is oriented upward
dens = 1.225  # densitiy of air
c_d = 0.35  # drag coefficient of the rocket
s = r*r*3.14  # cross-sectional area of the rocket

y = 0  # initial hight is 0
v = 0 # initial velociy is 0
position = []  # vector of y values
velocity = []  # vector of v  values

#--------------------------------------------#
# Accelerating phase  (thrust accelerates the rocket)
#--------------------------------------------#

dt = 0.0001  # elementary time interval
n = t_th/dt  # number of intervals


n = round(n)

t = 0
y= 0
v = 0

TH = []
T = []
V = []
Y = []


for interval in range(n+1):
       
    if t>=0 and t<=0.7:
        th = 12.86*t

    if t>0.7 and t<1:
        th = -20*t + 23
    if t>1 and t<5.5:
        th = 3
    if t>5.5 and t<6.25:
        th = -4*t+25
    if t>6.25:
        th = 0
    
    mass_r -= dt*th/v_e
    
    # Acceleration

    a_th = th/mass_r  # acceleration due to thrust
    
    a_d = (- 0.5*s*c_d*dens*v*v)/mass_r  # acceleration due to drag
    
    a = a_th+g+a_d  # overall acceleration
    
    

    if a<0 and y==0:
        y = 0
        v = 0
        Y.append(y)
        V.append(v)

    else:
        v += a*dt
        V.append(v)
        y += v*dt
        Y.append(y)
        
    T.append(t)
    TH.append(th)
  
    t += dt
plt.plot(T,TH, label = 'Thrust')
#--------------------------------------------#
# Decelerating phase (rocket is moving up by it's inertia)
# -------------------------------------------#

t_dp = -v/g  # duration of the decelerating phase before the rocket stops in air  !!!

n_2 = t_dp/dt
n_2 = round(n_2)


v_2 = v
y_2 = y

t +=-dt
print(n_2)

for interval_2 in range(100):
    

    f_d = -abs(v_2)/v_2*0.5*s*c_d*dens*v_2*v_2
    v_2 += dt*(g+f_d/mass_r)
    y_2 += dt*v_2
    position.append(y_2)
    velocity.append(v_2)
    t +=dt
    T.append(t)
    Y.append(y_2)
    V.append(v_2)


times = []  # vector of time values
for time in range(n+n_2):
    times.append(time*dt)
    
a = [n for n in range(80)]
b= [6]*80



# =============================================================================
# Analysis
# =============================================================================

print("The maximal hight was:")
print(max(Y))
print("The maximal velocity was")
print(max(V))

plt.plot(T,V, label = 'velocity')
plt.plot(T,Y, label = 'hight')

plt.title("Rocket flight")
plt.xlabel("time(s)")
plt.ylabel("Characteristics (SI)")

plt.legend(loc="lower center", bbox_to_anchor=(1, 1))


    