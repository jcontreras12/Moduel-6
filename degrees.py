# Problem 5 write a program to compute a conversion radians to degrees given by user input,print value and calculated value
import math
rad = float(input(" Enter amount of radians:"))
Degrees = rad * (180/math.pi)
print("Degrees of {} radians using calculations:{}".format(rad, Degrees))
print("Degrees of {} radians using inbuilt function:{}".format(rad, math.degrees(rad)))