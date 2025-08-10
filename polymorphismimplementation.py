class Cat:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def info(self):
        print(f"My cat's name is {self.name} and my cat is {self.age} years old.")

    def makeSound(self):
        print("meow")

class Dog:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def info(self):
        print(f"My dog's name is {self.name} and my dog is {self.age} years old.")

    def makeSound(self):
        print("Bark")

cat1 = Cat("Billi", 3)
dog2 = Dog("Coco", 5)

for animal in (cat1, dog2):
    animal.info()
    animal.makeSound()