import math

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

a1 = float(input("Triangle 1 leg a: "))
b1 = float(input("Triangle 1 leg b: "))
a2 = float(input("Triangle 2 leg a: "))
b2 = float(input("Triangle 2 leg b: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("Hypotenuse 1:", h1)
print("Hypotenuse 2:", h2)

if h1 > h2:
    print("First hypotenuse is greater")
elif h2 > h1:
    print("Second hypotenuse is greater")
else:
    print("They are equal")

def sort_words(s):
    words = s.split()
    return " ".join("".join(sorted(w)) for w in words)

text = input("Enter string: ")
print(sort_words(text))