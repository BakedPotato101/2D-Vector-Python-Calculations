import os
import math

os.system('clear')

FVA = float(input("Vector 1 A: "))
FVB = float(input("Vector 1 B: "))
SVA = float(input("Vector 2 A: "))
SVB = float(input("Vector 1 B: "))

DotProduct = (FVA*SVA)+(FVB*SVB)

MagnitudeF = math.sqrt(FVA**2+FVB**2)

MagnitudeS = math.sqrt(SVA**2+SVB**2)

Angle = math.degrees(math.acos(DotProduct / (MagnitudeF*MagnitudeS)))

print(Angle)