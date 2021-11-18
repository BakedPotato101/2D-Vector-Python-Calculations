import math
import os

def DirectionAngle(a,b):
    return math.degrees(math.atan(b / a))


os.system('clear')

a = float(input("A= "))
b = float(input("B= "))

print(DirectionAngle(a,b))