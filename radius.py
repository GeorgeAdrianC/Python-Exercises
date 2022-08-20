from math import pi

r= float(input("Please type a radius: "))
print(f"For radius {r} you have the values")

area = pi * r ** 2
volume = 4/3 * pi* r**3
print(f"Area: {area}")
print(f"Volume: {volume}")