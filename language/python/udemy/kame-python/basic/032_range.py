for i in range(0, 5, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)

target1 = 3
target2 = 5
for i in range(1, 51, 1):
    if i % (target1 * target2) == 0:
        print("FizzBuzz")
    elif i % target1 == 0:
        print("Fizz")
    elif i % target2 == 0:
        print("Buzz")
    else:
        print(i)