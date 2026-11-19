m1 = 5.0
m2 = 2.0
mu = 0.2
beta = 30.0
g = 9.81

import numpy as np

# Write your solution below.
# Explain your physical reasoning using comments.

#part 1:
#For static equilibrium, the absolute difference between the forces pulling along the incline must be less than or equal to the maximum static friction: 
#abs(m1 * g * sin(beta) - m2 * g) <= mu * m1 * g * cos(beta) The downward incline pull is 24.525 N and the upward tension is 19.62 N, yielding a net driving force of 4.905 N.
#The maximum static friction is 8.495 N. Since 4.905 N <= 8.495 N, the system is balanced and the box remains at rest. The positive x-axis is directed down the incline.
#If motion occurred, kinetic friction would act opposite to the direction of motion. Since it is at rest, a_x = 0.0.

#part 2: 
beta_rad = np.radians(beta)

# Calculate theoretical pulling forces and maximum static friction using radians 
T = m2*g
F_down = m1*g*np.sin(beta_rad)
N = m1*g*np.cos(beta_rad)
f_s_max = mu*N

F_drive = F_down - m2*g

if abs(F_down - T) <= f_s_max: 
    #System is at rest
    a_x = 0 
else: 
    #System accelerates
    f_k = mu*N
    a_x = (F_drive - np.sign(F_drive)*f_k) / (m1 + m2)
