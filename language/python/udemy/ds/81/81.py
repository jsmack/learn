
class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Bady(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError


class Car (object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

    def ride(self, person):
        person.drive()

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        # self.model = model
        super().__init__(model)
        # self.enable_auto_run = enable_auto_run
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self.__enable_auto_run = is_enable
        else:
            raise ValueError

    def auto_run(self):
        print('auto run')
    def run(self):
        print('super fast')
        print(self.__enable_auto_run)

baby = Bady()
adult = Adult()
car = Car()
car.ride(adult)
car.run()
print('############')

toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('############')
#tesla_car = TeslaCar('Model s')

tesla_car = TeslaCar('Model s', passwd='456')

print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()


## 83
print(tesla_car.enable_auto_run)
tesla_car.__enable_auto_run = 'xxxxxxxxxxx'

print(tesla_car.__enable_auto_run)


class T(object):
    pass

t = T()

t.name = 'Mike'
t.age = 20
print(t.name)