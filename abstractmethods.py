from abc import ABC, abstractmethod

from urllib3.connection import VerifiedHTTPSConnection


# abstract method is basically a method that a parent class (abstract class) defines and all the child classes
# referring to the parent(abstract) class must compulsorily implement the abstract method
# Also you cannot create instances of the parent (abstract) class
# ABC stands for abstract base class

class Vehicle(ABC):
    @abstractmethod
    def help(self):
        print("I help humans!")

class Bike(Vehicle):
    def ride(self):
        print("I ride on roads")
    def help(self):
        print("I also help humans")

class Car(Vehicle):
    def ride(self):
        print("I ride on 4 wheels")
    def help(self):
        print("I also help humans")

if __name__ == '__main__':
    # vehicle1 = Vehicle()

    bike1 = Bike()
    bike1.ride()
    bike1.help()

    car1 = Car()
    car1.ride()
    car1.help()