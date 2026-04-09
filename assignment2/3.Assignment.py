class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):

    def bark(self):
        print("Woof")
d = Dog()
d.eat()
d.bark()  

    