m = 0.0027
g = 9.8
b = 7e-05
c = 0.00034
v0 = 10.0
alpha = 15.0

import numpy as np
import matplotlib.pyplot as plt

def zero_cross(ar):
    # Returns an array of indices where ar changes sign.
    b0 = np.sign(ar)
    d = np.diff(b0)
    return np.nonzero(d)[0]

# Write your solution below.
# Explain the physical model and numerical method using comments.
alpha_rad = np.radians(alpha)
dt = 10**-3
t = np.arange(0, 30, dt)
n = len(t) - 1 
#Part 1 
#In this part, since air resistance is neglected, the acceleration is constant. Therefore, the time to reach maximum height equals the time from peak to initial height.
#Since the motion is under constant acceleration and the vertical velocity at peak height is zero, (vy = 0) we can use the kinematic equation vy = v0y + at to find t_up
a = -g 
t_up = v0*np.sin(alpha_rad)/g
t_down = t_up 
T1 = t_down - t_up 

#Trajectory for Part 1 - no air resistance
x1 = v0*np.cos(alpha_rad)*t
y1 = v0*np.sin(alpha_rad)*t - 0.5*g*t**2
return_index1 = zero_cross(y1)[-1]

#Part 2
#In this part, the quadratic term of air resistance is neglected, but since linear drag remains, the force and acceleration are not constant. Therefore, we must use Euler's method to integrate the equations of motion.
#To determine the position and velocity as functions of time
vx2 = np.zeros_like(t)
vy2 = np.zeros_like(t)
x2  = np.zeros_like(t)
y2 = np.zeros_like(t)

#initial conditions
vx2[0] = v0*np.cos(alpha_rad)
vy2[0] = v0*np.sin(alpha_rad)

#Implementing the Euler method
for i in range(n):
    
    #Acceleration components including air resistance
    ax = -(b/m)*vx2[i]
    ay = -g - (b/m)*vy2[i]

    #valocity update
    vx2[i + 1] = ax*dt + vx2[i]
    vy2[i + 1] = ay*dt + vy2[i]

    #position update 
    x2[i + 1] = vx2[i]*dt + x2[i]
    y2[i + 1] = vy2[i]*dt + y2[i]

#To find t_up we identify where the vertical velocity vy crosses zero. To find t_down we identify where the vertical position y returns to zero.
peak_index2 = zero_cross(vy2)[0]
t_up2 = t[peak_index2]
return_index2 = zero_cross(y2)[-1]
t_return2 = t[return_index2] 
t_down2 = t_return2 - t_up2
T2 = t_down2 - t_up2 

#Part 3
#In this part, the linear term of air resistance is neglected, but since quadratic drag remains, the force and acceleration are not constant. Therefore, we must use Euler's method to integrate the equations of motion.
#To determine the position and velocity as functions of time
vx3 = np.zeros_like(t)
vy3 = np.zeros_like(t)
x3  = np.zeros_like(t)
y3 = np.zeros_like(t)

#initial conditions
vx3[0] = v0*np.cos(alpha_rad)
vy3[0] = v0*np.sin(alpha_rad)

#Implementing the Euler method
for i in range(n):
    
    v = np.sqrt(vx3[i]**2 + vy3[i]**2) #Current speed magnitude

    #Acceleration components including air resistance
    ax = -(c/m)*v*vx3[i]
    ay = -g -(c/m)*v*vy3[i]

    #valocity update
    vx3[i + 1] = ax*dt + vx3[i]
    vy3[i + 1] = ay*dt + vy3[i]

    #position update 
    x3[i + 1] = vx3[i]*dt + x3[i]
    y3[i + 1] = vy3[i]*dt + y3[i]

#To find t_up we identify where the vertical velocity vy crosses zero. To find t_down we identify where the vertical position y returns to zero.
peak_index3 = zero_cross(vy3)[0]
t_up3 = t[peak_index3]
return_index3 = zero_cross(y3)[-1]
t_return3 = t[return_index3] 
t_down3 = t_return3 - t_up3
T3 = t_down3 - t_up3

plt.plot(x1[:return_index1 + 1], y1[:return_index1 + 1], label="No air resistance")
plt.plot(x2[:return_index2 + 1], y2[:return_index2 + 1], label="Linear drag")
plt.plot(x3[:return_index3 + 1], y3[:return_index3 + 1], label="Quadratic drag")

#part 4
#The measured time difference is 0.020 s.
#Model 3 gives the closest result to the measured value, so it best describes the experiment.
ANS4 = 3

