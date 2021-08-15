fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

# print(fruits_colors['peach'])
#     print(fruits_colors['peach'])
# KeyError: 'peach'

if 'peach' in fruits_colors:
    print(fruits_colors['peach'])
else:
    print('THe key is not found')
# THe key is not found


print(fruits_colors.get('peach', 'Nothing'))
# Nothing


fruit = input('Please enter the fruit name: ')
print(fruits_colors.get(fruit, 'Nothing'))
# input lemon:
# yellow

fruits_color2 = {'peach': 'pink', 'kiwi': 'green'}

fruits_colors.update(fruits_color2)
print(fruits_colors)
# {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple', 'peach': 'pink', 'kiwi': 'green'}
