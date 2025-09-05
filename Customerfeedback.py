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
        # self.feedback_list = []

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







    def leave_feedback(self, user, car, rating, comments):
        if 1 <= rating <= 5:
            feedback = Feedback(user, car, rating, comments)
            self.feedback_list.append(feedback)
            print("Thank you for your feedback!")
        else:
            print("Invalid rating. Please provide a rating between 1 and 5.")

    def display_feedback(self):
        print("Customer Feedback:")
        for feedback in self.feedback_list:
            print(feedback)

    # Expansion A: Address customer complaints
    def address_complaints(self):
        print("Addressing complaints...")
        for feedback in self.feedback_list:
            if feedback.rating <= 2:
                print(f"Complaint from {feedback.user}: {feedback.comments}")
                print("Action: Investigating and resolving the issue.")

    # Expansion B: Utilize feedback for improvements
    def analyze_feedback(self):
        print("Analyzing feedback for improvements...")
        total_ratings = sum(feedback.rating for feedback in self.feedback_list)
        count = len(self.feedback_list)
        average_rating = total_ratings / count if count > 0 else 0
        print(f"Average Rating: {average_rating:.2f}/5")
        print("Suggestions for improvement based on feedback:")
        for feedback in self.feedback_list:
            if feedback.rating <= 3:
                print(f"- {feedback.comments}")

class Feedback:
    def __init__(self, user, car, rating, comments):
        self.user = user
        self.car = car
        self.rating = rating
        self.comments = comments

    def __str__(self):
        return f"Feedback by {self.user}: {self.car} - Rating: {self.rating}/5, Comments: {self.comments}"

