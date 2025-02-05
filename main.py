
# main.py

from product import Product
from product_manager import ProductManager

def main():
    # Create an instance of ProductManager
    manager = ProductManager()

    # Add some arbitrary products to the product manager
    product1 = Product("Laptop", 1000.00, 5)
    product2 = Product("Smartphone", 500.00, 10)
    product3 = Product("Headphones", 150.00, 20)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    # Display all products
    print("Product Inventory:")
    manager.display_all_products()

    # Display the total value of the inventory
    print(manager.total_value())

if __name__ == "__main__":
    main()