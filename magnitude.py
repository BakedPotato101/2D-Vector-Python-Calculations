import os
import math

def getMagnitude(a,b):
    return math.sqrt(math.pow(a,2) + math.pow(b,2))


os.system('clear')


a = float(input("A= "))
b = float(input("B= "))


print(getMagnitude(a,b))




