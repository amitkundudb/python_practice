import logging

# Configure logging
logging.basicConfig(format='%(message)s',level=logging.INFO)

class Animal:
    def speak(self):
        pass  # Abstract method, to be overridden by subclasses

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Function to demonstrate polymorphism
def make_animal_speak(animal):
    logging.info(f"The animal says: {animal.speak()}")

# Creating instances of different classes
dog = Dog()
cat = Cat()

make_animal_speak(dog)
make_animal_speak(cat)