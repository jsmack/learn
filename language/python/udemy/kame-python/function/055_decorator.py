# decorator 関数に機能を付属

def greeting(func):
    def inner(*args, **kwargs):
        print("Hello!")
        func(*args, **kwargs)
        print("Nice to meet you!")
    return inner

@greeting
def say_name(name):
    print(f"I'm {name}")

# return inner function
f = greeting(say_name)
#say_name("Jiro")

f("Jiro")
# Hello!
# Hello!
# I'm Jiro
# Nice to meet you!
# Nice to meet you!

#say_name = greeting(say_name)
say_name("Jiro")
# Hello!
# I'm Jiro
# Nice to meet you!

@greeting
def say_name_and_origin(name, origin):
    print(f"I am {name}, I am from {origin}")

say_name_and_origin("taro", "Japan")
# Hello!
# I am taro, I am from Japan
# Nice to meet you!

say_name_and_origin(name="taro", origin="Japan")
# Hello!
# I am taro, I am from Japan
# Nice to meet you!

