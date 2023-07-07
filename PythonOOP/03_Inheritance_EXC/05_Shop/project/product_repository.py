from project.product import Product
class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self,product: Product):
        self.products.append(product)

    def find(self,name: str):
        for product in self.products:
            if product.name == name:
                return product

    def remove(self,name: str):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)

    def __repr__(self):
        result = ''.join(
            f'{product.name}: {product.quantity}\n' for product in self.products
        )
        return result.strip()