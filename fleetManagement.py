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
        # self.fleet_management = FleetManagement()  # Integrate FleetManagement

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





class FleetManagement:
    def __init__(self):
        self.maintenance_schedule = {}  # Tracks maintenance dates for cars

    def schedule_maintenance(self, car, date):
        self.maintenance_schedule[car] = date
        print(f"Maintenance scheduled for {car} on {date}.")

    def display_maintenance_schedule(self):
        print("Maintenance Schedule:")
        for car, date in self.maintenance_schedule.items():
            print(f"- {car}: {date}")

    def check_overdue_maintenance(self):
        print("Checking for overdue maintenance...")
        today = datetime.now().date()
        for car, date in self.maintenance_schedule.items():
            if date < today:
                print(f"Alert: {car} is overdue for maintenance!")

    # Expansion A: Car maintenance tracking and scheduling
    def schedule_car_maintenance(self, make, model, date, cars):
        for car in cars:
            if car.make == make and car.model == model:
                self.schedule_maintenance(car, date)
                return
        print("Car not found in the fleet.")

    # Expansion B: Alerts for overdue maintenance or low availability
    def check_fleet_status(self, cars):
        self.check_overdue_maintenance()
        available_cars = sum(1 for car in cars if car.is_available)
        if available_cars < 3:  # Example threshold for low availability
            print("Alert: Low car availability!")

