import re

# Regular Expression(RegEx)
email = "myemail@gmail.com"

print("@" in email)
# True

print(re.search('@\w+\.', email))
# <re.Match object; span=(7, 14), match='@gmail.'>

print(re.search('@\w+\.', "myemail@gmail"))
# None

# []

print(re.search('[abc]','a'))
# <re.Match object; span=(0, 1), match='a'>

print(re.search('[abc]','b'))
# <re.Match object; span=(0, 1), match='b'>

print(re.search('[abc]','c'))
# <re.Match object; span=(0, 1), match='c'>

print(re.search('[abc]', 'appble'))
# <re.Match object; span=(0, 1), match='a'>

print(re.search('^[0-9]', 'test'))
# None
print(re.search('^[0-9]', '3test'))
# <re.Match object; span=(0, 1), match='3'>

# {n} n repert
print(re.search('^[0-9]{4}', '2021/04'))
# # <re.Match object; span=(0, 4), match='2021'>


# {n,m} between n to m
print(re.search('^[0-9]{3,4}', '2021/04'))
# <re.Match object; span=(0, 4), match='2021'>

print(re.search('^[0-9]{3,4}', '202'))
# <re.Match object; span=(0, 3), match='202'>

print(re.search('^[0-9]{3,4}', '20'))
# None


# $ last
print(re.search('[0-9]{2}$', '2021/04/04'))
# <re.Match object; span=(8, 10), match='04'>

print(re.search('[0-9]{2}$', '2021/04/4'))
# None

# * right repert  greater than or equal 0
print(re.search('a*b', 'ab'))
# <re.Match object; span=(0, 2), match='ab'>

print(re.search('a*b', 'b'))
# <re.Match object; span=(0, 1), match='b'>

# + right repet greater than or equla 1
print(re.search('a+b', 'ab'))
# <re.Match object; span=(0, 2), match='ab'>

print(re.search('a+b', 'b'))
# None

# ? 0 times or 1 time
print(re.search('a?b', 'ab'))
# <re.Match object; span=(0, 2), match='ab'>
print(re.search('a?b', 'b'))
# <re.Match object; span=(0, 1), match='b'>
print(re.search('ab?c', 'b'))
# None

# | or
print(re.search('abc|123', 'abc'))
# <re.Match object; span=(0, 3), match='abc'>
print(re.search('abc|123', '123'))
# <re.Match object; span=(0, 3), match='123'>
print(re.search('abc|123', 'ab'))
# None

# () group
print(re.search('te(x|s)t', 'text'))
# <re.Match object; span=(0, 4), match='text'>


# . any single character
print(re.search('h.t', 'hat'))
# <re.Match object; span=(0, 3), match='hat'>
print(re.search('h.t', 'hee'))
# None

# \ meta escape
print(re.search('hat\.', 'hat.'))
# <re.Match object; span=(0, 4), match='hat.'>

# \w [a-zA-Z0-9_]
print(re.search('h\wt', 'hit'))
# <re.Match object; span=(0, 3), match='hit'>
print(re.search('h\w+t', 'heat'))
# <re.Match object; span=(0, 4), match='heat'>
print(re.search('h\wt', 'heat'))
# None
print(re.search('h\wt', 'h.t'))
# None

pattern_dob = "^(19|20)[0-9]{2}/(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])$"
while True:
    dob = input("Please enterd your birthday: ")
    #dob_check = re.search('[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}', dob)
    dob_check = re.search(pattern_dob, dob)
    if dob_check:
        print(f'Your birthday is {dob}!')
        break
    else:
        print(f'Your enterd birthday is illegal.')

pattern_email = "^(\w|\.|-)+@(\w|.|-)+\.[a-zA-Z]{2,3}$"
while True:
    email = input("Please enterd your email address: ")
    email_check = re.search(pattern_email, email)
    if email_check:
        print(f'Your email is {email}')
        break
    else:
        print(f'Your enterd email is illegal.')
