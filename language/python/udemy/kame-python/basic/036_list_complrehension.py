
#0, 1, 4, 9, 16, 25
square_list = []
for i in range(10):
    square_list.append(i ** 2)

print(square_list)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


square_list2 = [ x ** 2 for x in range(10) ]
print(square_list2)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_square_list = [ x ** 2 for x in range(10) if x % 2 == 0 ]
print(even_square_list)
# [0, 4, 16, 36, 64]
