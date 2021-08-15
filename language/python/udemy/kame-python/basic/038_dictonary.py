fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

print(fruits_colors)
# {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

print(fruits_colors['apple'])
# red

fruits_colors['peach'] = 'pink'
print(fruits_colors)
# {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple', 'peach': 'pink'}

dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}
print(dict_sample)
# {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}

print(dict_sample['four']['inner'])
# dict

colors = {}
colors[1] = 'blue'
colors[0] = 'red'
colors[2] = 'green'
print(colors)
# {1: 'blue', 0: 'red', 2: 'green'}

for x in fruits_colors:
    print(x)
# apple
# lemon
# grapes
# peach

for fruit in fruits_colors.keys():
    print(fruit)

# apple
# lemon
# grapes
# peach

for color in fruits_colors.values():
    print(color)

# red
# yellow
# purple
# pink

for fruit, color in fruits_colors.items():
    print(f'fruit: {fruit}, color: {color}')

# fruit: apple, color: red
# fruit: lemon, color: yellow
# fruit: grapes, color: purple
# fruit: peach, color: pink
