n = int(input("Enter n: "))
for i in range(1, n+1):
    digits = [int(d) for d in str(i) if d != '0']
    if digits and all(i % d == 0 for d in digits):
        print(i, end=" ")

print()

m = int(input("Array length: "))
arr = list(map(int, input("Array elements: ").split()))

print("Original:", arr)
arr[0], arr[-1] = arr[-1], arr[0]
print("Swapped:", arr)