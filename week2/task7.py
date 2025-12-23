from collections import Counter

items = input().split()
cnt = Counter(items)

print("Purchase frequency:")
for item, c in cnt.items():
    print(f"{item}: {c}")

most = max(cnt, key=cnt.get)
print(f"Most popular item: {most}")

once = [item for item, c in cnt.items() if c == 1]
print("Purchased once:", " ".join(once))

print("Sorted by frequency:")
for item, c in cnt.most_common():
    print(item, c)