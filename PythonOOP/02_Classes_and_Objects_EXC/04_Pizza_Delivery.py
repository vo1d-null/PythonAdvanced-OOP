# Define a class for Pizza Delivery
class PizzaDelivery:
    # Initialize the class with name, price and ingredients
    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    # Add extra ingredients to the pizza
    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        # Check if the pizza is already prepared
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        # Check if the ingredient exists in the pizza
        if ingredient not in self.ingredients.keys():
            self.ingredients[ingredient] = quantity
        else:
            self.ingredients[ingredient] += quantity
        # Update the price of the pizza
        self.price += quantity * price_per_quantity

    # Remove an ingredient from the pizza
    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        # Check if the pizza is already prepared
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        # Check if the ingredient exists in the pizza
        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        # Check if the quantity of the ingredient is correct
        elif quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        # Update the ingredients and price of the pizza
        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity

    # Make the order for the pizza
    def make_order(self):
        # Change the order status
        self.ordered = not self.ordered
        # Get the final ingredients for the pizza
        final_ingredients = "".join(
            f"{key}: {value}, " for key, value in self.ingredients.items()
        )
        # Return the order details
        return f"You've ordered pizza {self.name} prepared with {final_ingredients.rstrip(', ')} " \
               f"and the price will be {self.price}lv."


# Create a pizza object and tests the methods
margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
