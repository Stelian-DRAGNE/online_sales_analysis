
# product.py

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def update_quantity(self, new_quantity):
        """Updates the quantity of the product."""
        self.quantity = new_quantity
        print(f"Updated quantity of {self.name}: {self.quantity}")