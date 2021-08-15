# byref <-> byvalue

def add_nums(a, b):
    print(f"a: {id(a)}, b:{id(b)}")
    # a: 140337039415600, b:140337039415632
    return a + b


one = 1
two = 2
print(f"one: {id(one)}, two:{id(two)}")
# one: 140337039415600, two:140337039415632

print(add_nums(one, two))

# int is immutable
def add_one(num):
    print(f"before change{id(num)}")
    # before change140479158163760
    num += 1
    print(f"after  change{id(num)}")
    # after  change140479158163792
    return num

one = 1
print(f'one: {id(one)}')
# one: 140479158163760

add_one(one)
print(f'one: {id(one)}')
# one: 140479158163760
print(f"one: {one}")
# one: 1

# list is mutable
def add_fruit(fruits, fruit):
    print(f'before id: {id(fruits)}')
    # before id: 140593658688768

    fruits.append(fruit)
    print(f'aftre  id: {id(fruits)}')
    # aftre  id: 140593658688768

    return fruits

myfruits = ['apple', 'banana', 'peach']
myfruit = 'lemon'
print(f"before id:{id(myfruits)}")
# before id:140593658688768

add_fruit(myfruits, myfruit)
print(f"after  id:{id(myfruits)}")
# after  id:140593658688768

print(f"after    :{myfruits}")
# after    :['apple', 'banana', 'peach', 'lemon']

