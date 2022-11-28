## Good way to compute the Circle Area!! This is IMPORTABLE
## Now, when we import this file, the print statement will NOT run!
import math

def getCircleArea(radius):
    return math.pi * radius**2 

if __name__ == "__main__":
    
    print("Circle area is {}".format(getCircleArea(float(input("Enter a circle radius: ")))))