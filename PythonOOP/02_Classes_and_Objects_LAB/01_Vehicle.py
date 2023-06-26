# This class represents a vehicle
class Vehicle:
    def __init__(self, mileage, max_speed=150):
        # Constructor to initialize the object with mileage and maximum speed
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []  # List to store the gadgets of the vehicle


# Create a new instance of the Vehicle class with mileage 20
car = Vehicle(20)
# Print the maximum speed, mileage and gadgets of the car
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
# Add a new gadget to the car's gadgets list and print the updated list
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
