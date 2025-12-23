import re

allowed = "[ABCEHKMOPTX Y]"
pattern = re.compile(rf"^{allowed}\d{{3}}{allowed}{{2}}$")

n = int(input())
for _ in range(n):
    plate = input().strip()
    print("Yes" if pattern.match(plate) else "No")