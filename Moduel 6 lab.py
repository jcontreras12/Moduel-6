# Jose Contreras
# Date 11/5/21

# problem number 1 Use a for statement and random to print 10 random integers between 25-35
import random
for i in range (10):
    print (random.randrange(25-36))

#Problem 2 Use random randrange to print an odd integer from 0 to 100
 print (random.randrange(0, 50)* 2 + 1)

# Problem 3 use random choice to select a day of the week from a list and print that day
days = ["Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday"]
print (random.choice(days))

# Problem 4 write a program to compute the approximate and print the values of pi
import math
J = 1
C = 0
for i in range(100000):
    if i % 2 ==0:
        C += 4/J
    else:
        C -= 4/J
    J += 2
print ("Estimated value of Pi:", C)
print ("Value of Pi in math module:", math.pi)

# Problem 5 write a program to compute a conversion radians to degrees given by user input, print value and calculated value
rad = float(input(" Enter amount of radians:"))
Degrees = rad * (180/math.pi)
print ("Degrees of {} radians using calculations:{}".format(rad, Degrees))
print ("Degrees of {} radians using inbuilt function:{}".format(rad, math.degrees(rad)))

# problem 6 use a for statement to calculate the factorial of a users input value
x = int(input("Enter a number:"))
number = 1
for i in range(1, x+1):
    number = number * i
print("Factorial of {} using for Loop {}".format(x, number))
print(" Factorial of {} using inbuilt function: {}".format(x, math.factorial(x)))
