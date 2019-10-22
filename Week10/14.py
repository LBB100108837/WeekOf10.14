import math

# starting off


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(100000000000))


# This is pi 3.14159265359



# Experiment with the loop above alongside the actual value of Pi. How many
# sides does it take to make the two close
# IT TAKES MORE SIDES ex; 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

# Modify the archimedes function to take the radius of the circle as a parameter
# Can you get a better answer more quickly using a larger circle?


def archimedes(numSides):
    innerAngleB = 1440.0 / numSides
    halfAngleA = innerAngleB / 8
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 8
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 8
    return pi
print(archimedes(1000000000))




# Accumulators
acc = 0
for x in range(0, 6):
    acc = acc + x
print(acc)


# compute the sum of the first 100 even numbers
acc = 0
for x in range(1, 101):
    acc = acc + x * 2
print(acc)
# compute the sum of the first 50 odd numbers
acc = 50
for x in range(1, 50):
    acc = acc + x * 2
print(acc)
# compute the average of the first 100 odd numbers
acc = 0
for x in range(1, 200):
    if x % 2:
        acc = (acc + x)

print(acc/100)

# write a function that returns the average of the first N numbers where
#   N is a parameter
# write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
# each number in the Fibonacci sequence is the sum of the previous two numbers
#   The first two numbers in the sequence are 1 and 1. Compute the 10th
#   Fibonacci number
# Write a function to compute the Nth Fibonacci number, where N is a Parameter.
#   You may assume that N will be greater than or equal to 3.





## A Monte Carlo Simulation

import random

print(random.random())

# Boolean expressions
# > Greater than\
# >= greater than or equal to
# < Less than or equal to
# <= Less than or equal to
# == The same as ( equal to )
# != Not equal to
# = is assigning it and == is comparing it
CatWeight = 25
print(CatWeight == 25)
dogWeight = 15

# compound Boolean operators
# and
# or
# not

print(CatWeight > 30 and dogWeight < 20)

print(CatWeight > 30 or dogWeight < 20)

print(not dogWeight < 20)
# "not" takes the original answer and "flips" it.

# Decision Making -- Selection statements
a = 5
b = 10
c = 75

if a > b:
    c = 45

print(c)

if a > b:
    c = 45
    if b > c:
        a = 25
    else:
        a = -25
else:
    c = 1050
    if b == a:
        c = 25


print(a, b, c)


d = 85
e = 72
f = 44
ans = 0

if d > e:
    ans = 12
else:
    if d == e:
        ans = 50
    else:
        if f < d * e:
            ans = 100
        else:
            ans = 75
print(ans)

def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(10000))