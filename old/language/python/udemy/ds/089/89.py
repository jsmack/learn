class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind
    @staticmethod
    def about(year=2020):
        print('about human {}'.format(year))

a = Person()
print(a.x)
print(a.what_is_your_kind())
b = Person
print(b)
print(a.what_is_your_kind())

print(Person.kind)
print(Person.what_is_your_kind())

Person.about()
Person.about(1998)