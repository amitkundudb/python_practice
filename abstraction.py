import logging

# Configure logging format without including level and logger name
logging.basicConfig(format='%(message)s', level=logging.INFO)

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.logger = logging.getLogger('Car')

    def start(self):
        # Abstracting the implementation details of starting the car
        self.logger.info(f"Starting the {self.make} {self.model}")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Using the start method without knowing the implementation details
my_car.start()  # Output: Starting the Toyota Camry
