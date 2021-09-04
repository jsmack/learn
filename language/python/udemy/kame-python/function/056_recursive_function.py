# recursive function
# 階乗 (factorial)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(3))
# 6

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
# 8

def fibonacci_2(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        result = 0
        for i in range(n-1):
            result = n_2 + n_1
            print(f"{n_2}, {n_1}, {result}")
            n_2 = n_1
            n_1 = result
        return result


print(fibonacci_2(6))
# 0, 1, 1
# 1, 1, 2
# 1, 2, 3
# 2, 3, 5
# 3, 5, 8
# 8

#for i in range(50):
#    print(i, fibonacci(i))

for i in range(50):
    print(i, fibonacci_2(i))