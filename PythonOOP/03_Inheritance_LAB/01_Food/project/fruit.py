from project.food import Food
class Fruit(Food):
    def __init__(self, name, expiration_date: str):
        # Call the parent class constructor
        super().__init__(expiration_date)
         # Set the name of the fruit
        self.name = name