# product_manager.py

from product import Product

class ProductManager:
    def __init__(self):
        """Initializes an empty list of products."""
        self.products = []

    def add_product(self, product):
        """Adds a product to the list of products."""
        self.products.append(product)

    def display_all_products(self):
        """Displays information about all products in the list."""
        for product in self.products:
            print(product.display_info())

    def total_value(self):
        """Calculates and returns the total value of all products in stock."""
        total = sum(product.price * product.quantity for product in self.products)
        return f"Total value of all products: ${total:.2f}"

    def remove_product_by_name(self, name):
        """Removes a product from the list by its name."""
        self.products = [product for product in self.products if product.name != name]
        print(f"Product(s) with name '{name}' have been removed.")
