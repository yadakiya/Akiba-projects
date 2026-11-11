"""Question 5: Instance/class/static methods and composition."""


class Product:
    store_name = "Akiba Store"  # Class attribute shared by all products

    def __init__(self, name, price):
        if not self.is_valid_price(price):
            raise ValueError("Product price must be greater than zero.")

        self.name = name
        self.price = price

    def display_product(self):
        print(f"Store: {self.store_name}")
        print(f"Product: {self.name}")
        print(f"Price: {self.price:.2f}")

    @classmethod
    def change_store_name(cls, new_name):
        if not new_name.strip():
            raise ValueError("Store name cannot be empty.")
        cls.store_name = new_name

    @staticmethod
    def is_valid_price(price):
        return isinstance(price, (int, float)) and not isinstance(price, bool) and price > 0


class ShoppingCart:
    def __init__(self):
        self.products = []  # ShoppingCart contains Product objects

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to the cart.")
        self.products.append(product)
        print(f"{product.name} added to the cart.")

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def display_cart(self):
        print("\n========== SHOPPING CART ==========")
        if not self.products:
            print("The cart is empty.")
        else:
            for product in self.products:
                print(f"{product.name}: {product.price:.2f}")
        print(f"Total: {self.calculate_total():.2f}")


if __name__ == "__main__":
    Product.change_store_name("Akiba Technologies Store")

    laptop = Product("Laptop", 45000)
    mouse = Product("Wireless Mouse", 1200)
    keyboard = Product("Keyboard", 1800)

    laptop.display_product()

    cart = ShoppingCart()
    cart.add_product(laptop)
    cart.add_product(mouse)
    cart.add_product(keyboard)
    cart.display_cart()
