import string


with open('design/email_template.html') as f:
    t = string.Template(f.read())

#t = string.Template(s)

contents = t.substitute(name='Mike', contents='How are you?')

print(contents)