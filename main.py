# main.py

import random
from product import Product
from product_manager import ProductManager
from cart import Cart

def main():
    # Create an instance of ProductManager
    manager = ProductManager()

    # Add some arbitrary products to the product manager
    product1 = Product("Laptop", 1000.00, 5)
    product2 = Product("Smartphone", 500.00, 10)
    product3 = Product("Headphones", 150.00, 20)
    product4 = Product("Tablet", 300.00, 7)
    product5 = Product("Smartwatch", 200.00, 15)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    manager.add_product(product4)
    manager.add_product(product5)

    # Create an instance of Cart
    cart = Cart()

    # Randomly select 3 products from the available products
    selected_products = random.sample(manager.products, 3)

    # Add selected products to the cart
    for product in selected_products:
        cart.add_product(product.name, product.price, random.randint(1, 3))  # Random quantity between 1 and 3

    # Display the cart content
    cart.display_cart()

if __name__ == "__main__":
    main()