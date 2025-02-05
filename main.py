
# main.py

from product import Product
from product_manager import ProductManager

def main():
    # Create an instance of ProductManager
    manager = ProductManager()

    # Add some arbitrary products to the product manager
    product1 = Product("Bread", 11.00, 2)
    product2 = Product("Milk", 9.00, 5)
    product3 = Product("Bananas", 8.00, 3)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

if __name__ == "__main__":
    main()