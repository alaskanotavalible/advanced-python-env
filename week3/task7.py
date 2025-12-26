def right_triangle_area(a, b):
    return a * b / 2

def rectangle_area(a, b):
    return a * b

x = float(input("X: "))
y = float(input("Y: "))
z = float(input("Z: "))
t = float(input("T: "))

area = right_triangle_area(x, y) + rectangle_area(z, t)
print("Area:", area)

n = int(input("Enter number: "))
print(format(n, "010o"))