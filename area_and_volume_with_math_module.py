# Write a program that begins by reading a radius, r, from the user. The program will continue by computing and displaying the area of a circle with radius r and the volume of a sphere with radius r.
# Hint: The area of a circle is computed using the formula area = πr**2. The volume of a sphere is computed using the formula volume = (4/3)πr**3.

from math import pi

r = float(input("Please type a radius: "))
print(f"For radius {r} you have the values:")

area = pi * r**2
volume = 4/3 * pi * r**3

print(f"Area: {area}")
print(f"Volume: {volume}")
