from abc import ABC, abstractmethod


@abstractmethod
class Shape(ABC):
    def calculate_area(self):
        ...


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes
    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value,list):
            raise AssertionError('`shapes` should be of type `list`.')

        self.__shapes = value
    @property
    def total_area(self):
        # Converted for loop into call to sum() to inline variable that is immediately returned
        return sum(shape.calculate_area() for shape in self.shapes)


shapes = [Rectangle(2, 3), Rectangle(1, 6) , Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
