m = 0.6
v0 = 2.0
beta = 30.0

import numpy as np

# Write your solution below.
# Explain the physical reasoning using comments.
beta_rad = np.radians(beta)
#p = m*v 
#we need the whole system so: 
#P_total = P_box + P_cart 
#since v0_cart = 0:
#P_total = P_box
#meaning: 
#P_total = m_box*v0_box
#since the box moves along an incline, its velocity vector is at an angle beta relative to the horizontal 
#we will break the mumentum to x and y components: 
Px = -m*v0*(np.cos(beta_rad))
Py = m*v0*(np.sin(beta_rad))

#part 2: 
#Horizontal momentum is conserved because there is no net external force in the x direction.
#Vertical momentum is not conserved because external vertical forces act on the system, such as gravity and the normal force from the ground.
#Since there are no external horizontal forces (friction with the floor is negligible), the total momentum Px 
#remains constant throughout the motion.
#At the moment the box is "at rest relative to the cart," both objects move together as a single unit with a combined mass of 
# m + 5m = 6m 
#Because the cart moves along the incline, its velocity vector
#v_cart s oriented at an angle beta 
#from the horizontal. Therefore, the horizontal component of its velocity is v_cart*cos(beta)
ANS2 = Px / (6*m)

#part 3: 
#To find the minimum static friction coefficient, we consider the limiting case where the box is just about to slide.
#At this point, the required static friction equals its maximum value: fs = mu_s*N.
#Using fs = m*g*sin(beta) and N = m*g*cos(beta), we get mu_s = tan(beta).
ANS3 = np.tan(beta_rad)

#part 4: 
#For Part 4, horizontal momentum conservation is combined with the condition that the magnitude of the box velocity in the lab frame is again equal to v0.
#These two equations are solved together to obtain the cart velocity V4.
tan_beta = np.tan(beta_rad)
cos_beta = np.cos(beta_rad)

numerator_V4 = -v0 * cos_beta * (10 + 12 * tan_beta**2)
denominator_V4 = 25 + 36 * tan_beta**2

V4 = numerator_V4 / denominator_V4

#part 5: 
#At this moment, the box has the same speed magnitude v0 as initially, but the wedge is also moving.
#Therefore, the total kinetic energy of the system is greater than it was initially, while friction has also dissipated energy.
#The additional energy must come from gravitational potential energy, so the box is lower than its initial height.
ANS5 = "Lower"







