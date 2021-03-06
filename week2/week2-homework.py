# Week-2 homework
# 1. Write fizz_buzz function
# from pywin.mfc.object import Object


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number


print(fizz_buzz(12))

# 2. write a try and except block to avoid IndexError
lst = [5, 10, 20]
try:
    index = int(input('inter the index of an item in the list: > '))
    element = lst[index]
    print(element)
except ValueError:
    print('Index should be Integer number')
except IndexError:
    print('list index out of range')


# 3. Create a class of Jet inventory with two arguments


class Jet:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def print_name_country(self):
        print(f'{self.name} {self.country}')


jet1 = Jet('helicopter', 'Denmark')
jet1.print_name_country()
jet2 = Jet('Boing', 'USA')
jet2.print_name_country()

# 5. Write a Python script to check whether a given key already exists in a dictionary.
customers = {'name': 'Jonis', 'phone': '123-345-8',
             'address': 'CPH'}


def check_key(key):
    return key in customers


print(check_key('phone'))


# 6. Odd or Even


def show_numbers(limit):
    for num in range(0, limit + 1):
        if num % 2 == 0:
            even_or_odd = 'EVEN'
        else:
            even_or_odd = 'ODD'
        print(f' {num} {even_or_odd}')


show_numbers(6)


# 8. Class


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(f'{self.first_name} {self.last_name}')


person_1 = Person('Lars', 'Andersen')
person_2 = Person('Susanne', 'Mikel')
person_1.print_name()
person_2.print_name()

# 9. try-except block for numeric entry
try:
    x = float(input('enter a numeric value:> '))
    print(x)
except ValueError:
    print('Not numeric entry')


# 10. Write a Python program to create two empty classes, Student and Marks


class Student:
    pass


class Marks(Student):
    pass


student_1 = Student()
record_1 = Marks()
print(isinstance(student_1, Student))  # results True
print((isinstance(record_1, Marks)))
#   To check if a class is subclass of other class or object
print(issubclass(Marks, Student))       # True
print(issubclass(Student, object))      # True
print(issubclass(Marks, object))




