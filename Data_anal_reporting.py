class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_available = True

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {'Available' if self.is_available else 'Not Available'}"

class CarRentalService:
    def __init__(self):
        self.cars = []
        self.reservations = []

    def add_car(self, car):
        self.cars.append(car)

    def display_available_cars(self):
        print("Available Cars:")
        for car in self.cars:
            if car.is_available:
                print(car)

    def rent_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model and car.is_available:
                car.is_available = False
                print(f"You have rented: {car}")
                return
        print("Sorry, the car is not available.")

    def return_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model and not car.is_available:
                car.is_available = True
                print(f"You have returned: {car}")
                return
        print("Sorry, this car was not rented from us.")

