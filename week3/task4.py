def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def divide_fractions(a, b, c, d):
    num = a * d
    den = b * c
    g = gcd(num, den)
    return num // g, den // g

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

num, den = divide_fractions(A, B, C, D)
print(f"Result: {num}/{den}")

def inside_circle(x, y, a, b, r):
    return (x - a)**2 + (y - b)**2 <= r**2

a = float(input("Circle center x: "))
b = float(input("Circle center y: "))
r = float(input("Radius: "))

count = 0
for i in range(3):
    x, y = map(float, input("Point coordinates: ").split())
    if inside_circle(x, y, a, b, r):
        count += 1

print("Points inside:", count)