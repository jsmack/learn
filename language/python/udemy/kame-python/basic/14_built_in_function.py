# built in function
# type()
hello_type = type("Hello")
print(hello_type)

hello_id = id("hello")
print(hello_id)
hello = "hello"
hello2 = "hello"
print(id(hello))
print(id(hello2))
# 同じIDが表示される
w = "world"
print(id(w))
print(id("world"))