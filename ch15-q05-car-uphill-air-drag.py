m = 1500.0
P = 80000.0
c = 0.4
g = 9.8

import numpy as np

def zero_cross(ar):
    # returns an array of indices where ar changes sign
    b = np.sign(ar)
    d = np.diff(b)
    return np.nonzero(d)[0]

# Write your solution below.
# Explain the physical model and your reasoning using comments.

#part 1: 
#Flat road (alpha = 0)
#At constant speed on a flat surface, all engine power P is used
#to overcome air resistance: P = F_drag*v (c*v^2)*v = c*v^3
V1 = np.power(P/c, 1/3)

#part 2: 
#alpha = 12
alpha = np.radians(12)

#Create an array of possible velocities
v_range = np.linspace(0, 150, 1000)

#Calculate the power required at each velocity
#P_req = cv^3 + mg*sin(alpha)*v
p_required = c*v_range**3 + (m*g* np.sin(alpha))*v_range

#The difference between available power and required power
#We look for where this equals zero
diff = p_required - P
ind = zero_cross(diff)
V2 = v_range[ind[0]]

#part 3: 
#alpha = 12
#Calculate V3 by neglecting air resistance (c=0)
#Since c=0, the equation becomes linear: P = mg*sin(alpha)*v
V3 = P/(m*g*np.sin(alpha))

#part 4: 
epsilon = abs(V3 - V2)/V2 

if epsilon <= 0.1: 
    ANS4a = "yes"
else: 
    ANS4a = "no"

if epsilon <= 0.05: 
    ANS4b = "yes"
else: 
    ANS4b = "no"

#part 5: 
#alpha = 0 
#When the road is flat, gravity does not oppose motion
#In this case, the ONLY force the engine must overcome is air resistance
#Therefore, if we neglect air resistance (c=0), the required power becomes zero
#and the car would theoretically accelerate indefinitely or reach an undefined speed
#Since air resistance is the only limiting factor on a flat road, it cannot be ignored

