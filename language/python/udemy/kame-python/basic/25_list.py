# list
fruits = ['apple', 'banana', 'peach', 'melon', 'grapes']
hetro_list = ['sting', 1, 3.4, True, fruits]

print(fruits)
print(hetro_list[-1])
print("hello world"[3])

# .append
# .insert
# .remove
# .sort
# len()

fruits.append('watermelon')
print(fruits)
fruits.insert(3, 'lemon')
print(fruits)

fruits.remove('peach')
print(fruits)

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

print(len(fruits))
