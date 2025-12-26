def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def subtract_fractions(a, b, c, d):
    num = a*d - b*c
    den = b*d
    g = gcd(abs(num), den)
    return num // g, den // g

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

num, den = subtract_fractions(A, B, C, D)
print(f"Result: {num}/{den}")

n = int(input("Enter number: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")