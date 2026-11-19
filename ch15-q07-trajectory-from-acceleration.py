A = 1.0
omega = 0.8
t1 = 4.0

import numpy as np
import matplotlib.pyplot as plt

def zero_cross(ar):
    # returns an array of indices where ar changes sign
    b = np.sign(ar)
    d = np.diff(b)
    return np.nonzero(d)[0]

# Write your solution below.
# Explain your solution using comments.
#part 1: 
dt = 10**-2
t = np.arange(0, 10, dt)
n = len(t) - 1 

vx = np.zeros_like(t)
vy = np.zeros_like(t)
x  = np.zeros_like(t)
y = np.zeros_like(t)

#initial conditions
vx[0] = A
vy[0] = 0

for i in range(n):
    ax = -(2*A*omega*(np.sin(omega*t[i])) + (omega**2)*A*t[i]*(np.cos(omega*t[i])))
    ay = 2*A*omega*np.cos(omega*t[i]) - (omega**2)*A*t[i]*np.sin(omega*t[i])

    #valocity update
    vx[i + 1] = ax*dt + vx[i]
    vy[i + 1] = ay*dt + vy[i]

    #position update 
    x[i + 1] = vx[i + 1]*dt + x[i]
    y[i + 1] = vy[i + 1]*dt + y[i]

plt.plot(x, y)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trajectory in the xy plane')
plt.grid(True)

#part 2: 
#The tangent to the trajectory is parallel to the y-axis when
#the horizontal component of velocity is zero, i.e., vx = 0

#part 3: 
#Find the time when the tangent is parallel to the y-axis for the third time
indices = zero_cross(vx)

#The third occurrence is at index 2 of the results
T3 = t[indices[2]]

#part 4: 
#Find index corresponding to t1
idx_t1 = np.argmin(np.abs(t - t1))

#Get values at t1 for plotting
x_t1 = x[idx_t1]
y_t1 = y[idx_t1]
v_x_t1 = vx[idx_t1]
v_y_t1 = vy[idx_t1]

#Calculate acceleration at t1 (using the formulas from your loop)
ax_t1 = -(2*A*omega*np.sin(omega*t1) + (omega**2)*A*t1*np.cos(omega*t1))
ay_t1 = 2*A*omega*np.cos(omega*t1) - (omega**2)*A*t1*np.sin(omega*t1)

#Plot the trajectory
plt.plot(x, y, label='Trajectory')

#Plot velocity arrow (red) and acceleration arrow (black)
#Note: You might need to multiply v_x_t1/v_y_t1 or ax_t1/ay_t1 by a
#constant factor if they are too small/large to see clearly.
plt.quiver(x_t1, y_t1, v_x_t1, v_y_t1, color='red', label='Velocity at t1')
plt.quiver(x_t1, y_t1, ax_t1, ay_t1, color='black', label='Acceleration at t1')

plt.legend()
plt.show()

#part 5: 
R1 = np.sqrt(x_t1**2 + y_t1**2)