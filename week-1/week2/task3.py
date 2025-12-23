eq = input().strip()

a, op, b, _, c = eq

def val(x):
    return int(x)

if a == 'x':
    b, c = val(b), val(c)
    x = c - b if op == '+' else c + b
elif b == 'x':
    a, c = val(a), val(c)
    x = a - c if op == '+' else a - c
else:
    a, b = val(a), val(b)
    x = a + b if op == '+' else a - b

print(x)