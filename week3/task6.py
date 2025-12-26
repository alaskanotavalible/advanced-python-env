def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input("A: "))
b = int(input("B: "))
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))

def quad_area(a, b, c, d, diag):
    s1 = (a + b + diag) / 2
    s2 = (c + d + diag) / 2
    area1 = (s1*(s1-a)*(s1-b)*(s1-diag))**0.5
    area2 = (s2*(s2-c)*(s2-d)*(s2-diag))**0.5
    return area1 + area2

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
d = float(input("Side d: "))
diag = float(input("Diagonal: "))

print("Quadrilateral area:", quad_area(a, b, c, d, diag))