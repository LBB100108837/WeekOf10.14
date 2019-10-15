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


print(archimedes(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))


# This is pi 3.14159265359



# Experiment with the loop above alongside the actual value of Pi. How many
# sides does it take to make the two close
# IT TAKES MORE SIDES

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
print(archimedes(100000000000))
