
# cart.py

class Cart:
    def __init__(self):
        # Initializing an empty list to store the items in the cart
        self.cart_items = []

    def add_product(self, product, price, quantity=1):
        """
        Adds a product to the cart. The product is represented by a dictionary ontaining 'name', 'price', and 'quantity'. If the product already exists, the quantity will be updated.

        :param product: The name of the product.
        :param price: The price of the product.
        :param quantity: The quantity of the product to add (default is 1).
        """

        # Checking if the product already exists in the cart
        for item in self.cart_items:
            if item['name'] == product:
                item['quantity'] += quantity
                return

        # If the product is not found, adding it to the cart
        self.cart_items.append({
            'name': product,
            'price': price,
            'quantity': quantity
        })

    def total_value(self):
        """
        Calculates the total value of the cart by summing the price * quantity for each product.

        :return: The total price of all items in the cart.
        """

        total = 0
        for item in self.cart_items:
            total += item['price'] * item['quantity']
        return total

    def display_cart(self):
        """
        Displays the content of the cart, including the name, price, and quantity of each product.
        """

        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for item in self.cart_items:
                print(f"Product: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
            print(f"Total value of the cart: {self.total_value()}")