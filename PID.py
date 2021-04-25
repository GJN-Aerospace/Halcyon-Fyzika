# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 13:07:25 2021

@author: Ondra Zikmund
"""

import matplotlib.pyplot as plt
plt.close()

dt = 0.1  # time step


E = [0,0]

x = 0  # initial position
v_0 = 2
x_f = 33  # final position

t_o = 30 # length of simulation
T = [0,0]
X = [0,0]
V = [v_0]


def PID(E):
    
    P = 30    # proportional constant 18
    I = 0.001  # integral constant 16
    D = -1.5 # differential constant 9

    P_a = E[-1]*P
    I_a = sum(E)*dt*I
    D_a = (E[-1]-E[-2])/dt*D

    alpha = P_a + I_a + D_a   # angular acceleration in a direction  
    
    return alpha




#for i  in range(round(t_o/dt)):
for i  in range(200):
    T.append((i+1)*dt)
    error = x_f-x
    E.append(error)
    alpha = PID(E)
    
    
    v = X[-1]-X[-2]+alpha*dt   #past velocity is augmented by the acceleration term
    
    dx = v*dt  # element of distance 
    x +=dx
    
    X.append(x)   # list of distances
    V.append(v)  # list of velocities

print(V)
plt.plot(T,X)
    
    



    
#plt.plot(T,X)
           
# =============================================================================
# # =============================================================================
# # PID CONTROLLER 
# # =============================================================================
# dt = 0.01  # time step
# 
# 
# disc_a = []
# disc_w = []  # real angular velocity in the a direction
# 
# 
# def PID_velocity(disc_a):
#     
#     P = 4    # proportional constant
#     I = 0  # integral constant
#     D = -0.15  # differential constant
# 
#     P_a = disc_a[-1]*P
#     I_a = sum(disc_a)*dt*I
#     D_a = (disc_a[-1]-disc_a[-2])/dt*D
# 
#     w_a = P_a + I_a + D_a   # angular velocity in a direction  
#     
#     return w_a
# 
# def PID_acceleration(disc_w):
#     
#     P = 6   # proportional constant
#     I = 0  # integral constant
#     D = -0.6 # differential constant
#     
#     P_a = P*disc_w[-1]
#     I_a = sum(disc_w)*dt*I
#     D_a = (disc_w[-1]-disc_w[-2])/dt*D
#    
#     alpha_a = P_a + I_a + D_a   # angular velocity in a direction  
#     
#     return alpha_a
# 
# x_f = 25  # final angle
# w_f = 0  # final speed
# 
# x = 50  # initial angle
# w = 0   # initial speed
# 
# 
# t_o = 10
# dt = 0.01
# 
# disc_a = [x_f-x]
# disc_w = [w_f-w]
# 
# X = []
# W = []
# T = []
# 
# #for i in range(round(t_o/dt)):
#     
# for i in range(round(t_o/dt)):
#     
#     T.append(i*dt)
#     
#     disc_p = x_f - x
#     disc_a.append(disc_p)
#     w_n = PID_velocity(disc_a)
# 
# 
#     disc_ww = w_n - w
# 
#     disc_w.append(disc_ww)
#     alpha = PID_acceleration(disc_w)
#    # print(alpha)
# 
#     w+=dt*alpha
#     x += dt*w
#     X.append(x)
#     W.append(w)
# 
# plt.plot(T,X)
# 
# =============================================================================

# =============================================================================
# PID CONTROLLER 
# =============================================================================
    
    