def sphere_volume(radius):
    volume = (4/3) * 3.14159 * radius**3
    return volume
radius = float(input("Enter the radius of the sphere: "))
print("Volume of the sphere:", sphere_volume(radius))