# *args
print("hello", "world")
# hello world


def get_average(*args):
    print(*args)
    # 1 2 3 4 5
    print(args)
    # (1, 2, 3, 4, 5)
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num


average = get_average(1, 2, 3, 4, 5)
print(average)
# 3.0

# ** kwargs
def kwargs_func(**kwargs):
    print(kwargs)
    # {'param1': 10, 'param2': 6}
    
    param1 = kwargs.get('param1', 1)
    param2 = kwargs.get('param2', 2)
    param3 = kwargs.get('param3', 3)

    print(f"param1: {param1}, param2: {param2}, param3: {param3}")


kwargs_func(param1=10, param2=6, param3=100)
# param1: 10, param2: 6, param3: 100

# * and ** are unpacking operator
numbers = (1, 2, 3)
print(numbers)
# (1, 2, 3)

print(*numbers)
# 1 2 3

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
# a.update(b)

d = {**a, **b}
print(f"a: {a}, b: {b}")
# a: {'a': 1, 'b': 2}, b: {'c': 3, 'd': 4}

print(d)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
