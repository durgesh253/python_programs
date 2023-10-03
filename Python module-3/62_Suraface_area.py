import math

radius = float(input("Enter Radius: "))
height = float(input("Enter Height: "))

lateral_suraface_area =  2 * math.pi * radius * height

total_surfce_area =  2 * math.pi * radius * (radius + height)

volume = math.pi * radius**2 * height



print(f"surface Area is {lateral_suraface_area}")
print(f"total surafce area is {total_surfce_area}")
print(f"Volume of cyilender is {volume}")