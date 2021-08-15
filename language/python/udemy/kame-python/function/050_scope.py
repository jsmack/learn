def print_name_local():
    first_name = "Taro"
    last_name = "Yamada"
    print(f"I'm {first_name} {last_name}")


print_name_local()
# I'm Taro Yamada

# global variables or module variables
age = 30


def print_age():
    # local variables
    age = 20
    print(f"I'm {age} years old.")
    # I'm 20 years old.


print_age()
print(age)
# 30
