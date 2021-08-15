# parameter int, return int(->)
# type annotaion
def add_nums(num1: int, num2: int) -> int:
    return num1 + num2


print(add_nums(1, 2))
# 3

# dynamic typed language
print(add_nums("1", "2"))
# Expected type 'int', got 'str' instead
# 12

