from cmath import phase

complex_number = complex(input())

polar_coordinates = (abs(complex_number), phase(complex_number))

print(f"{polar_coordinates[0]:.3f}")
print(f"{polar_coordinates[1]:.3f}")
