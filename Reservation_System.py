from datetime import datetime, timedelta

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



#First add the reservationclass at the bottom
    def reserve_car(self, make, model, start_date, end_date):
        for car in self.cars:
            if car.make == make and car.model == model and car.is_available:
                for reservation in self.reservations:
                    if reservation.car == car and not (end_date < reservation.start_date or start_date > reservation.end_date):
                        print("Sorry, the car is already reserved for the selected dates.")
                        return
                new_reservation = Reservation(car, start_date, end_date)
                self.reservations.append(new_reservation)
                print(f"Reservation successful: {new_reservation}")
                return
        print("Sorry, the car is not available.")

    def display_reservations(self):
        print("Reservations:")
        for reservation in self.reservations:
            print(reservation)

    # Expansion A: Calendar view for managing reservations
    def display_calendar(self):
        print("Reservation Calendar:")
        today = datetime.now().date()
        for i in range(30):
            day = today + timedelta(days=i)
            print(f"{day}:")
            for reservation in self.reservations:
                if reservation.start_date <= day <= reservation.end_date:
                    print(f"  - {reservation.car}")

    # Expansion B: Notification system for reminders
    def send_reservation_reminders(self):
        print("Sending reservation reminders:")
        today = datetime.now().date()
        for reservation in self.reservations:
            if reservation.start_date == today:
                print(f"Reminder: Your reservation for {reservation.car} starts today.")
            elif reservation.end_date < today:
                print(f"Notification: Your reservation for {reservation.car} has expired.")

class Reservation:
    def __init__(self, car, start_date, end_date):
        self.car = car
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Reservation for {self.car} from {self.start_date} to {self.end_date}"





