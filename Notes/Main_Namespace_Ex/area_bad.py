## file area_bad.py
## When we import this file, it will run the print statement! This is NOT good for importing!

import math
def getCircleArea(radius):
    return math.pi * radius**2
    
print("Circle area is {}".format(getCircleArea(float(input("Enter a circle radius: ")))))