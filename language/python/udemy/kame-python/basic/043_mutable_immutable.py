# mutable : modifable object list, dict, set
fruits = ['apple', 'peach', 'banana']
print(f"fruits id is {id(fruits)}")
# fruits id is 140692694597248

fruits.append('lemon')
print(fruits)
# ['apple', 'peach', 'banana', 'lemon']

print(f"fruits id is {id(fruits)}")
# fruits id is 140692694597248

# immutable; Unchangeble object int, float, str, bool, tuple
fruit = 'apple'
print(f"frut id is {id(fruit)}")
# frut id is 140487056202096

fruit += ', lemon'
print(fruit)
# apple, lemon

print(f"frut id is {id(fruit)}")
# frut id is 140487056597296
## Change id

# 1-2-3-4-5-6-7-..
text = ""

# inefficiency
# Consume memory every time
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)

print(text)
# 1-2-3-4-5-6-7-8-9-10

# efficiency
# Consume memory one time
text_list =[]
for i in range(1, 11):
    text_list.append(str(i))

text = "-".join(text_list)
print(text)
# 1-2-3-4-5-6-7-8-9-10
