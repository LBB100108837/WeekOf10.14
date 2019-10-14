import math

# starting off
print(12/6)
print(355/113)

print(24 / (6 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(8))
print(archimedes(32))




for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# Experiment with the loop above alongside the actual value of Pi. How many
# sides does it take to make the two close


# Modify the archimedes function to take the radius of the circle as a parameter
# Can you get a better answer more quickly using a larger circle?