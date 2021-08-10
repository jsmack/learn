fruits = ["apple", "peach", "grapes", "banana"]
print('apple' in fruits)
print('lemon' in fruits)

print('h' in 'hello')

fruits_list = ["apple", "peach", "grapes", "banana"]
fruits = input("What do you like fruits?: ")

print(fruits_list)
if fruits in fruits_list:
    fruits_list.remove(fruits)
else:
    fruits_list.append(fruits)

print(fruits_list)