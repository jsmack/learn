def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f'k: {k}, v:{v}')


a = {"one": 1, "two": 2}
print(a)
# {'one': 1, 'two': 2}

print_dict(a)
# k: one, v:1
# k: two, v:2

return_value = print_dict(a)
print(return_value)
# If return is not written, it returns "None".
# None


def get_first_last_word(text):
    text = text.replace(",", "")
    words = text.split()
    return words[0], words[1]

text = "Hello, My name is Mike."
r = get_first_last_word(text)
print(r)
# Return type is tuple
# ('Hello', 'My')

# Tuples is unpack
f, l = get_first_last_word(text)
print(f'f:{f}, l{l}')
# f:Hello, lMy


