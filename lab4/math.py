# # Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904
import math

degree = float(input())
radian = degree * (math.pi / 180)
print(radian)

# Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = 0.5 * (base1 + base2) * height

print("Expected Output:", area)

# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area1 = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

print("The area of the polygon is:", area1)

# Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0

base_length = float(input("Length of base: "))
height1 = float(input("Height of parallelogram: "))

area2 = base_length * height1

print("Expected Output:", area2)

