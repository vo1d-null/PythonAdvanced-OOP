# This class represents a circle with methods to calculate its area and circumference.
class Circle:
    # Constructor to initialize the radius of the circle.
    def __init__(self, radius: int or float):
        self.radius = radius
    # Class variable to store the value of pi.
    pi = 3.14
    # Method to set the radius of the circle.
    def set_radius(self, radius):
        self.radius = radius
    # Method to get the radius of the circle.
    def get_radius(self):
        return self.radius
    # Method to calculate the area of the circle.
    def area(self):
        return self.radius ** 2 * self.pi
    # Method to get the area of the circle.
    def get_area(self) -> float:
        return self.area()
    # Method to calculate the circumference of the circle.
    def circumference(self) -> float:
        return 2 * self.pi * self.radius
    # Method to get the circumference of the circle.
    def get_circumference(self) -> float:
        return self.circumference()