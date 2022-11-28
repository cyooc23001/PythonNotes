import area_good

circleRadius = 10
circleArea = area_good.getCircleArea(circleRadius)
print("A circle with radius {} has an area of {}".format(circleRadius, circleArea))

## See how we didn't run the code inside 'if __name__" == __main__:' block in area_good
## We just ran the code here in main_good. That's exactly what we want! This is the good way to import!