class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Return a readable description of the product
    def __str__(self):
        return (
            f"Product: {self.name}, "
            f"Price: {self.price} birr, "
            f"Quantity: {self.quantity}"
        )

    # Calculate total value of the product
    def total_value(self):
        return self.price * self.quantity


# Create three product objects
product1 = Product("Laptop", 45000, 2)
product2 = Product("Mouse", 500, 10)
product3 = Product("Keyboard", 1200, 5)

print("\n========== TASK 4 ==========")

# Print objects directly
print(product1)
print("Total Value:", product1.total_value(), "birr")

print()

print(product2)
print("Total Value:", product2.total_value(), "birr")

print()

print(product3)
print("Total Value:", product3.total_value(), "birr")