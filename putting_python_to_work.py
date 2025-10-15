import math
#test 4

# TO-DO: get the radius of the circle from the user
try:
    radius = float(input("Enter the radius of the circle: "))
except ValueError:
    print("Invalid input. Please enter a number for the radius.")
    exit()

# Ensure the radius is non-negative
if radius < 0:
    print("Radius cannot be negative.")
    exit()

# TO-DO: calculate the diameter of the circle
diameter = 2 * radius

# TO-DO: calculate the circumference of the circle (C = 2 * pi * r)
circumference = 2 * math.pi * radius

# TO-DO: calculate the area of the circle (A = pi * r^2)
area = math.pi * (radius ** 2)

# TO-DO: print the values for the user
print("\n--- Circle Calculations ---")
print(f"Radius: {radius}")
print(f"Diameter: {diameter:.2f}") # Formatted to 2 decimal places
print(f"Circumference: {circumference:.2f}") # Formatted to 2 decimal places
print(f"Area: {area:.2f}") # Formatted to 2 decimal places
