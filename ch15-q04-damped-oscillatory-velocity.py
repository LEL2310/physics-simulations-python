v0 = 5.0
gamma = 0.5

import numpy as np
import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    b=np.sign(ar)
    d=np.diff(b)
    return np.nonzero(d)[0]

# Write your solution below.
# Explain your solution using comments.
dt = 0.01
t = np.arange(0, 7, dt)
n = len(t) - 1 

#Calculate velocity based on the given damped oscillation formula
v = v0*np.exp(-gamma*t)*np.cos(10*gamma*t)

#Calculate acceleration using numerical differentiation (central difference)
a = np.gradient(v, dt)

#Calculate position using numerical integration (cumulative sum of displacements)
x = np.cumsum(v * dt)

#Find the second time when v = 0.1*v0
#we will check when v-0.1*v0 is zero_cross 
target_v = 0.1 * v0
indices = zero_cross(v - target_v)

#Take the exact index of the second crossing
second_index = indices[1]
T2 = t[second_index] #Use the exact time from the array

#Plot the particle position as a function of time
plt.plot(t, x, label='Position x(t)')

#Find the index in the time array corresponding to T2
idx = np.argmin(np.abs(t - T2))

#Mark the particle position at time T2 with a red point
plt.plot(T2, x[idx], 'ro')

#Add a label next to the marked point
plt.annotate('T2', (T2, x[idx]))

#Add axis labels, title and legend
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Particle Position over Time')
plt.legend()

#Display the graph
plt.show()


    