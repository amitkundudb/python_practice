class Car:
    def __init__(self, model):
        self.model = model
    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Tesla(Car):
    def drive(self):
        return f"{self.model} is driving with autopilot engaged."
    def stop(self):
        return f"{self.model} has stopped with regenerative braking."
def main():
    # Create instances of different cars
    model_s = Tesla("Model S")
    model_3 = Tesla("Model 3")

    # Polymorphism in action
    print(model_s.drive())
    print(model_3.drive())
    print(model_s.stop())
    print(model_3.stop())
if __name__ == "__main__":
    main()