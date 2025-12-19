ticket = input()

first_sum = sum(map(int, ticket[:3]))
second_sum = sum(map(int, ticket[3:]))

if first_sum == second_sum:
    print("YES")
else:
    print("NO")