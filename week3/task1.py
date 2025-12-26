def area_rectangle(a, b):
    return a * b

def area_circle(r):
    return 3.14 * r * r

def array_sum_and_mean(arr):
    s = sum(arr)
    mean = s / len(arr)
    return s, mean

a = float(input("Rectangle side a: "))
b = float(input("Rectangle side b: "))
print("Rectangle area:", area_rectangle(a, b))

r = float(input("Circle radius: "))
print("Circle area:", area_circle(r))

for i in range(3):
    arr = list(map(int, input(f"Enter array {i+1}: ").split()))
    s, m = array_sum_and_mean(arr)
    print("Sum:", s, "Mean:", m)