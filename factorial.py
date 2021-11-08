# problem 6 use a for statement to calculate the factorial of a users input value
import math
x = int(input("Enter a number:"))
number = 1
for i in range(1, x+1):
    number = number * i
print("Factorial of {} using for Loop {}".format(x, number))
print(" Factorial of {} using inbuilt function: {}".format(x, math.factorial(x)))