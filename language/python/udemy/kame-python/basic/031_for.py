fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    print(f'I love {fruit}')

for char in "Hello world!":
    print(f'char is {char}')


# iteration and iterable

input_fruit = input("Please input fruits: ")

if input_fruit in fruits:
    print(f'I like {input_fruit}')
else:
    print(f'I do not line {input_fruit}')

for fruit in fruits:
    if fruit == input_fruit:
        print(f'I like {fruit}')
        break
    else:
        print(f'I do not like {fruit}')

like_fruits = []
dislike_fruits = []
for fruit in fruits:
    input_fruit = input(f"Do you like {fruit}? y/n: ")
    if input_fruit == "y":
        like_fruits.append(fruit)
    elif input_fruit == "n":
        dislike_fruits.append(fruit)

print(f'You like fruits is {like_fruits}')
print(f'You dislike fruits if {dislike_fruits}')
