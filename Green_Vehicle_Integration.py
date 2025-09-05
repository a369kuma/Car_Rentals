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
        # self.green_vehicle_service = GreenVehicleService()

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




    # Expansion B: Emissions tracking for green vehicles
    def rent_green_vehicle(self, make, model, duration):
        for car in self.cars:
            if car.make == make and car.model == model and car.is_available:
                if hasattr(car, "vehicle_type") and car.vehicle_type in ["Hybrid", "Electric"]:
                    car.is_available = False
                    print(f"You have rented: {car} for {duration} days.")
                    self.green_vehicle_service.track_emissions_savings(car.vehicle_type, duration)
                    return
        print("Sorry, the green vehicle is not available.")

class GreenVehicleService:
    def __init__(self):
        self.emissions_savings = 0  # Tracks total emissions savings

    def calculate_emissions_savings(self, vehicle_type, duration):
        savings_per_day = {
            "Hybrid": 10,  # Example: 10 kg CO2 saved per day
            "Electric": 20  # Example: 20 kg CO2 saved per day
        }
        return savings_per_day.get(vehicle_type, 0) * duration

    def track_emissions_savings(self, vehicle_type, duration):
        savings = self.calculate_emissions_savings(vehicle_type, duration)
        self.emissions_savings += savings
        print(f"Emissions savings for this rental: {savings} kg CO2")
        print(f"Total emissions savings: {self.emissions_savings} kg CO2")

    # Expansion A: Eco-friendly incentives
    def display_eco_friendly_incentives(self):
        print("Eco-Friendly Incentives:")
        print("- Discount on rentals for hybrid and electric vehicles.")
        print("- Loyalty points for choosing sustainable options.")
        print("- Contribution to environmental initiatives.")

