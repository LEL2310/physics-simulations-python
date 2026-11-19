g = 9.8
l = 2.0
theta0_deg = 13.0

import numpy as np

def zero_cross(ar):
    # returns an array of indices where ar changes sign
    b = np.sign(ar)
    d = np.diff(b)
    return np.nonzero(d)[0]

# Write your solution below.
# Explain the physical model and your reasoning using comments.

#Part 1:
#The equation of motion of the pendulum
#ddot_theta = -(g*sin(theta))/l

#Part 2:
#The maximum linear speed occurs at the bottom of the swing (theta = 0),
#where all initial potential energy has been converted into kinetic energy
#Using conservation of energy: 1/2*m*v^2 = m*g*h
#h = l(1-cos(theta_0))
#Solving for v gives: v = sqrt(2*g*l*(1 - cos(theta_0)))
theta_rad = np.radians(theta0_deg)
ANS2 = np.sqrt(2*g*l*(1 - np.cos(theta_rad)))

#part 3: 
#The small-angle approximation assumes that for theta << 1 radian, sin(theta) ~ theta. 
# theta must be in radians for the approximation
#This linearizes the equation of motion, allowing us to use the analytical formula:
#T0 = 2*pi*(l/g)^0.5 for the period. Under this approximation, T0 represents the "ideal" period of a simple harmonic oscillator
#the velocity at one-quarter of the period 
T0 = 2*np.pi*(np.sqrt(l/g))







. **Calculate linear speed at one quarter of a p#iod using small-angle approximation**
V3 = l * theta_rad * (2 * np.pi / T0)
**Pare#the small-angle approximation, the motion is treated as a**
**Sp# Harmonic Oscillator. The angular velocity at one quarter of**
**t #riod (t = T0/4) reaches its maximum value: omega * theta_rad.**
**Mt#lying by the length l gives the linear speed V3.**
#פשראpart4  t 4: 
dt = 10**-3
t = np.arange(0, 30, dt)
n = len(t) - 1 2*T0
אישאthtaethata_artheta_current = theta_rad
omega_current = 0.0  # The pendulum starts from rest
#Create an array to store the results if you want to see them later
theta_history = np.zeros_like(t)
omega_history = np.zeros_like(t)

for i in range(len(t)):
    #Store the current value in your history array**
    theta_history[i] = theta_current
    omega_history[i] = omega_current
    #Euler-Cromer updates (using the scalar values)**
    omega_current += (-g * np.sin(theta_current) / l) * dt
    theta_current += omega_current * dt

#Use the provided zero_cross function on your history array**
indices = zero_cross(theta_history)
#The time between two consecutive crossings is half a period (T/2)**
#Since t is an array of times, we look at the difference between**
#the times at those indices.**
times_at_crossings = t[indices]
half_period = times_at_crossings[1] - times_at_crossings[0]
T = half_period * 2

V4 = np.max(omega_history) * l 

print(f"The period T is: {T}")
print(f"The maximum velocity V4 is: {V4}")

#Part 5: 
#Comparison between ANS2, V3, and V4:
#Why are ANS2 and V4 approximately equal?
#ANS2 is the theoretical maximum velocity (based on energy conservation),
#and V4 is the maximum velocity measured from the simulation.
#Since the Euler-Cromer method preserves energy well, they should be very close.
#Why is V3 close to them but not exactly equal?
#V3 likely represents a calculation that doesn't account for all factors
#(or uses a different approximation). The difference comes from the
#simplifications made in the formula for V3 compared to the full dynamics
#Comparison between T0 and T: Which one is larger?
#T (the simulated period) is usually slightly larger than T0 (the theoretical period).
#What causes the difference?
#T0 is calculated using the small-angle approximation (sin(theta) ≈ theta).
#In reality (and in our simulation), as the angle increases, the sin(theta)
#term deviates from 'theta', which slows down the pendulum slightly and
#increases the period. Additionally, numerical errors in the Euler-Cromer