class PizzaDelivery:
    def __innit__(self,name : str, price : float, ingredients : dict, ordered : bool = False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = ordered

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
