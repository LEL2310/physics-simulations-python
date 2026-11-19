m1 = 1.0
m2 = 1.1
v1 = 10.0

# Given parameters: m1, m2 and v1
# Ball 2 is initially at rest: v2 = 0

# Write the conservation equations and your solution below.
# Explain the limiting cases using comments.
# Since the collision is elastic, both momentum and kinetic energy are conserved
#Momentum: 
# m1*v1 = m1*u1 + m2*u2
#Kinetic Energy: 
#(m1*(v1^2))/2 = (m1*(u1^2))/2 + (m2*(u2^2))/2
#case 1:
ANS1_u1 = ((m1 - m2)*v1) / (m1 + m2)
ANS1_u2 = (2*m1*v1) / (m1 + m2)

#case 2: 
ANS2_u1 = 0
ANS2_u2 = v1

#case 3:
ANS3_u1 = -v1
ANS3_u2 = 0

#case 4: 
ANS4_u1 = v1
ANS4_u2 = 2*v1

C1 = 3
C2 = 4
C3 = 2
C4 = 4
C5 = 3