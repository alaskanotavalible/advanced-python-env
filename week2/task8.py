from collections import Counter

s1 = input().strip()
s2 = input().strip()

print("YES" if Counter(s1) == Counter(s2) else "NO")