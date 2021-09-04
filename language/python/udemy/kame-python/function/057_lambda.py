def square(x):
    return x * x

print(square(4))
# 16

s = lambda x: x * x
print(s(4))
# 16


def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

third_power = power(3)
print(third_power(2))
# 8

def power_2(exponent):
    return lambda base: base ** exponent

third_power = power(3)
print(third_power(2))
# 8


numbers = [6, 2, 5, 34, 23, 13, 5, 57]


def fillterfunc(num):
    if num % 2 == 0:
        return True
    else:
        return False

for num in numbers:
    print(f"{num} = {fillterfunc(num)}")

# 6 = False
# 2 = False
# 5 = True
# 34 = False
# 23 = True
# 13 = True
# 5 = True
# 57 = True

filtered_num = filter(fillterfunc, numbers)
print(f"filter = {list(filtered_num)}")
# filter = [6, 2, 34]

print(list(filter(lambda num: not num % 2, numbers)))
# [6, 2, 34]
