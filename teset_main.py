from Reservation_System import Car, CarRentalService

def test_car_rental_service():
    # Initialize the service and add cars
    service = CarRentalService()
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Civic", 2019)
    car3 = Car("Ford", "Focus", 2021)
    service.add_car(car1)
    service.add_car(car2)
    service.add_car(car3)

    # Test displaying available cars
    print("Test: Display available cars")
    service.display_available_cars()

    # Test renting an available car
    print("\nTest: Rent an available car")
    service.rent_car("Toyota", "Camry")
    assert not car1.is_available, "Car should be marked as not available after renting."

    # Test renting a car that is already rented
    print("\nTest: Rent a car that is already rented")
    service.rent_car("Toyota", "Camry")

    # Test returning a rented car
    print("\nTest: Return a rented car")
    service.return_car("Toyota", "Camry")
    assert car1.is_available, "Car should be marked as available after returning."

    # Test returning a car that is not rented
    print("\nTest: Return a car that is not rented")
    service.return_car("Toyota", "Camry")

    # Test renting a car that does not exist
    print("\nTest: Rent a car that does not exist")
    service.rent_car("Tesla", "Model S")

    # Test returning a car that does not exist
    print("\nTest: Return a car that does not exist")
    service.return_car("Tesla", "Model S")

if __name__ == "__main__":
    test_car_rental_service()
