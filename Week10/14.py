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
for x in range(1, 101):
    acc = acc + x * 2

print(acc)


# compute the sum of the first 100 even numbers
acc = 0
for x in range(0, 101, 2):
    acc = acc + x

print(acc)
# compute the sum of the first 50 odd numbers
# compute the average of the first 100 odd numbers
# write a function that returns the average of the first N numbers where
#   N is a parameter
# write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
# each number in the Fibonacci sequence is the sum of the previous two numbers
#   The first two numbers in the sequence are 1 and 1. Compute the 10th
#   Fibonacci number
# Write a function to compute the Nth Fibonacci number, where N is a Parameter.
#   You may assume that N will be greater than or equal to 3.


