class Animal:
    def __init__(self):
        self.age = 30
    def eat(self):
        print("eat")


class Mamal(Animal):
    def walk(self):
        print("walk")
        
        
class Fish(Animal):
    def swim(self):
        print("swim")
        
animal = Mamal()
print(animal.age)