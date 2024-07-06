import math
print(f"first co-ordinate point is (0,0)")
x=int(input("Enter the X Co-ordinate of second point: "))
y=int(input("Enter the Y Co-ordinate of second point: "))

distance=math.sqrt(x**2+y**2)
print(f"The Euclidean distance between (0,0) and ({x},{y}) is {distance} units")
