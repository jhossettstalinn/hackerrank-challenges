import math

a = float(input()) # Length of side AB
b = float(input()) # Length of side BC
c = math.sqrt(a**2 + b**2) 

# Calculate the angle alpha and beta
alpha = math.atan(b / a)
beta = math.atan(a / b)

# Calculating the angle MBC (theta)
# after doing some math
theta = math.atan(math.sin(beta)/math.sin(alpha))

# Convert the angle from radians to degrees
theta = math.degrees(theta)

print(f"{round(theta)}\u00b0")
