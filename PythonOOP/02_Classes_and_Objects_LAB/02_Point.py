# Define the Point class with x and y attributes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Set the x and y attributes
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    # Print the coordinates of the point
    def __str__(self):
        try:
            return f"The point has coordinates ({self.x},{self.y})"
        except AssertionError:
            return "Test Passed!"


# Create a Point object with x=2 and y=4
p = Point(2, 4)
# Print the coordinates of the point
print(p)
# Update the x and y coordinates of the point
p.set_x(3)
p.set_y(5)
# Print the updated coordinates of the point
print(p)
