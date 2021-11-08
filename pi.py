# Problem 4 write a program to compute the approximate and print the values of pi
import math
J = 1
C = 0
for i in range(100000):
    if i % 2 == 0:
        C += 4/J
    else:
        C -= 4/J
    J += 2
print("Estimated value of Pi:", C)
print("Value of Pi in math module:", math.pi)