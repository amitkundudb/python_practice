import logging

# Configure logging
logging.basicConfig(format='%(message)s',level=logging.INFO)

class Car:
    def __init__(self, make, model, mileage):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        logging.info("Car object created")

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def set_make(self, make):
        self.__make = make
        logging.info("Make updated")
    def set_model(self, model):
        self.__model = model
        logging.info("Model updated")

    def set_mileage(self, mileage):
        self.__mileage = mileage
        logging.info("Mileage updated")

my_car = Car("Toyota", "Camry", 50000)

logging.info("Make: %s", my_car.get_make())
logging.info("Model: %s", my_car.get_model())
logging.info("Mileage: %d", my_car.get_mileage())
my_car.set_make("Tesla")
my_car.set_model("S")
my_car.set_mileage(50)

logging.info("Make: %s", my_car.get_make())
logging.info("Model: %s", my_car.get_model())
logging.info("Mileage: %d", my_car.get_mileage())