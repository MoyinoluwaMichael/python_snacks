# Calculate the area and circumference of a circle form its radius.
# Area = pi*r^2
# Circumference = 2*pi*r

import math

radius = int(input("Enter the radius pof your circle: "))

area = math.pi *(radius**2)
circumference = 2*math.pi*radius

print ("The circumference of the circle is: ",circumference,", while the area is: ",area)