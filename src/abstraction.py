import logging

# Configure logging
logging.basicConfig(format='%(message)s',level=logging.INFO)

class Animal:
    def make_sound(self):
        pass  # Abstract method, to be overridden by subclasses

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
# Function to demonstrate abstraction
def make_animal_sound(animal):
    logging.info(f"The animal makes the sound: {animal.make_sound()}")

# Creating instances of different classes
dog = Dog()
cat = Cat()

# Calling the common method make_sound() on different objects
make_animal_sound(dog)
make_animal_sound(cat)