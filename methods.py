from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # this is an instance method, where with each created instance this function will change the values
    def description(self):
        print(f"My name is {self.name} and my age is {self.age}")

    # this is a static method which doesn't relate to the class at all, it can be placed anywhere in the
    # code & it will have the same output if its not placed inside the class
    # def add_numbers(self, *nums):
    @staticmethod
    def add_numbers(*nums):
        print(sum(nums))

    # this is a class method, this method can change the attributes of the class Person. it has direct
    # affect on the main class.
    @classmethod
    def age_from_birthdate(cls, name, year):
        current_year = datetime.now().year
        age = current_year - year
        return cls(name, age)

if __name__ == '__main__':
    het = Person("Het", 19)
    het.description()
    Person.add_numbers(10,10,10)

    het2 = Person.age_from_birthdate("Het", 2004)
    het2.description()