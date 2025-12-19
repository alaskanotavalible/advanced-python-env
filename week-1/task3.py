a = float(input())

integer_part = int(a)
fractional_part = a - integer_part

new_number = fractional_part * 100 + integer_part / 100
print(new_number)