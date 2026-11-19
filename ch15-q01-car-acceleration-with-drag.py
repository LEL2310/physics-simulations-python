m = 1300.0
mu = 0.8
c = 0.5
g = 10.0
dt = 0.01

# Write your solution below.
# Explain the physical model and the Euler method using comments.
#Physical parameters
#The car starts from rest
t = 0            #Initial time [s]
v = 0            #Initial velocity [m/s]

#Convert the target velocity from km/h to m/s
vT = 100 / 3.6   #Final velocity [m/s]

#On a horizontal road, the normal force is equal to the car's weight
n = m*g          #Normal force [N]

#Continue the simulation until the car reaches the target velocity
while v < vT: 
    #The maximum static friction force acts forward and drives the car
    #The quadratic air drag acts opposite to the direction of motion
    #According to Newton's second law, acceleration equals the net force divided by mass
    a = (mu*n - c*v**2) / m
    
    #Euler method: update the velocity using the current acceleration
    v = a*dt + v 
    
    #Advance the simulation time by one time step
    t = t + dt 

print("Time needed to reach 100 km/h:", t, "seconds")



