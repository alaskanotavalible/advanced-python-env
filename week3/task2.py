import math

def triangle_area(a):
    return (math.sqrt(3) / 4) * a * a

def hexagon_area(a):
    return 6 * triangle_area(a)

a = float(input("Hexagon side: "))
print("Hexagon area:", hexagon_area(a))

for i in range(3):
    x = float(input("Rectangle side 1: "))
    y = float(input("Rectangle side 2: "))
    print("Rectangle area:", x * y)