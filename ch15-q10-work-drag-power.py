m = 2.0
c = 0.6
g = 9.8
v0 = 6.0
mu = 0.3

import numpy as np

# Write your solution below.
# Explain the physical model and numerical method using comments.

#part 1: 
#the work done by the total force is equal to the change in kinetic energy.
#Since the box starts with velocity v0 and ends at rest (v=0), the work W1 can be calculated using:
# W1 = delta_Ek = 0.5*m*v_final^2 - 0.5*m*v0^2 
# since v_final = 0, the work W1 can be calculated using:
# W1 = delta_Ek = - 0.5*m*v0^2 
W1 = -(m*(v0**2))/2

#part 2: 
dt = 0.01
t = np.arange(0, 30, dt)
n = len(t) - 1 

v = np.zeros_like(t)
x  = np.zeros_like(t)

#initial conditions
v[0] = v0

i = 0
while v[i] > 1e-3:
    
    #Calculate acceleration
    a = -((c/m)*v[i]**2 + mu*g)

    #valocity update
    v[i + 1] = a*dt + v[i]

    #position update 
    x[i + 1] = v[i]*dt + x[i]

    i += 1 

T = t[i]
L = x[i]

#part 3: 
#The total work done on the box, W1  is the sum of the work done by all forces acting on it. In this system, there are two resistive forces: kinetic friction and air drag. Therefore:
#W_total = W1 = W_friction + W_drag
W_friction = -mu*m*g*L
W2 = W1 - W_friction 

#part 4: 
#Calculate work done by drag using power over time
P_drag = -c * (v**3)
#Sum the power over time to get W3
W3 = np.sum(P_drag * dt)

#Part 5:
#Calculate work done by drag using integral over distance
#Since dx = v * dt, we multiply the term -c * v^2 by (v * dt)
W4 = np.sum(-c * (v**2) * (v * dt))

#Part 6:
print(f"W2 (Analytical/Subtraction): {W2}")
print(f"W3 (Power Integral): {W3}")
print(f"W4 (Distance Integral): {W4}")
#You should expect all three values to be very close to each other.
#W2 is the "exact" value based on energy conservation.
#W3 and W4 are numerical approximations of that same value.
#Small differences between them (if any) are due to the
#discretization error from using a finite time step dt.

