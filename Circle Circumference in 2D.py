import math
def circle_circumference(radius):
    circumference = round(2 * math.pi * radius)
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return circumference

print(circle_circumference(5))
