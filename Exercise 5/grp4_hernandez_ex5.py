import math

# Example: factorial
n = 5
result = math.factorial(n)
print(f"The factorial of {n} is: {result}")

# Example: power and logarithmic function
x = 2
y = 3

# Power function: x raised to the power y
power_result = math.pow(x, y)

# Logarithmic function: base 10 logarithm of x
log_result = math.log10(x)

print(f"{x} raised to the power {y} is: {power_result}")
print(f"Logarithm of {x} with base 10 is: {log_result}")

# Example: sine function
angle_degrees = 45

# Convert degrees to radians
angle_radians = math.radians(angle_degrees)

# Sine function
sin_result = math.sin(angle_radians)

print(f"The sine of {angle_degrees} degrees is: {sin_result}")

# Example: radians to degrees conversion
angle_radians = math.pi / 4

# Convert radians to degrees
angle_degrees = math.degrees(angle_radians)

print(f"{angle_radians} radians is equal to {angle_degrees} degrees.")

# Example: hyperbolic sine function
x = 2

# Hyperbolic sine function
sinh_result = math.sinh(x)

print(f"The hyperbolic sine of {x} is: {sinh_result}")