m = 1.0
k = 20.0
c = 2.0

import numpy as np
import matplotlib.pyplot as plt

def zero_cross(ar):
    # Returns an array of indices where ar changes sign.
    b = np.sign(ar)
    d = np.diff(b)
    return np.nonzero(d)[0]

# Write your solution below.
# Explain the physical model and numerical method using comments.

#part 1: 
#The net force consists of two components: the spring force, which pulls the box toward the equilibrium position, and the air resistance (drag), which opposes the direction of motion
#The equation of motion is:
# ma = -kx - cv|v|

#part 2: 
#To find X0, we use the condition at the moment of release (t=0).
#Since the velocity v = 0 at t = 0, the air resistance force equals zero.
#Therefore, the acceleration at release is due only to the spring: a = -kx/m.
#Given that the magnitude of acceleration at release is 2k/c, we set:
#|-kx0 / m| = 2k/c
X0 = (2*m)/c

#part 3:
#Numerical Simulation using Euler-Cromer Method:
#Time Discretization: We define a time step dt = 10^-3 s over a total
#duration of 20 seconds to simulate the motion in small, discrete steps.
dt = 10**-3
t = np.arange(0, 20, dt)
n = len(t) - 1 

#Force Modeling: The acceleration 'a' is calculated by summing the spring force (-k*x) and the quadratic drag force.
#We use v * abs(v) for the drag term to ensure that the force always opposes
#the direction of motion, regardless of whether velocity is positive or negative
#Euler-Cromer Method: To improve stability in oscillatory systems
#we use the Euler-Cromer method. In this scheme, we update the velocity
#use the Euler-Cromer method. In this scheme, we update the velocity
#first (v[i+1] = v[i] + a*dt) and then use this updated velocity to
#calculate the next position (x[i+1] = x[i] + v[i+1]*dt).
v = np.zeros_like(t)
x = np.zeros_like(t)

#initial conditions: 
v[0] = 0
x[0] = X0
#Implementing the Euler method
for i in range(n): 
    
    #Acceleration components including air resistance
    a = (-k*x[i] - c*(v[i]*abs(v[i])))/m

    #valocity update
    v[i + 1] = a*dt + v[i]

    #position update 
    x[i + 1] = v[i + 1]*dt + x[i]

plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Spring Oscillator with Quadratic Drag')
plt.show()

#Part 4
#The box is momentarily at rest whenever its velocity crosses zero.
stop_indices = zero_cross(v)
stop_times = t[stop_indices]

#Calculate the time differences between consecutive stopping times.
stop_intervals = np.diff(stop_times)



