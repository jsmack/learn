# closure

def compute_square(num):
    return num * num

print(type(compute_square))
# <class 'function'>

print(compute_square)
# <function compute_square at 0x7f9ed5adf040>



def execute_func(func, param):
    return func(param)
f = compute_square
print(execute_func(f, 10))
# 100


def return_func():

    def inner_func():
        print("This is an inner function")

    return inner_func

f = return_func()
print(f)
# <function return_func.<locals>.inner_func at 0x7f9ed5adf1f0>

f()
# This is an inner function


# 状態をきーぷした　関数を作ることができる
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

power_four = power(4)
print(power_four)
# <function power.<locals>.inner_power at 0x7fa0582db3a0>
print(power_four(2))
# 16 (2 ** 4)

power_five = power(5)
print(power_five(2))
# 32 (2 ** 5)


# 状態を動的
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average

average_nums = average()
print(average_nums(5))
# 5.0
print(average_nums(15))
# 10.0 
