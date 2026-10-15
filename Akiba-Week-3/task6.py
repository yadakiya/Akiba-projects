
def add_product(inventory, name, price, stock):
    name = name.strip()

    if not name:
        return False, "Product name cannot be empty."

    for product in inventory:
        if product["name"].lower() == name.lower():
            return False, "Product already exists."

    if price < 0:
        return False, "Price cannot be negative."

    if stock < 0:
        return False, "Stock cannot be negative."

    product = {
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)
    return True, "Product added successfully."


def search_product(inventory, name):
    for product in inventory:
        if product["name"].lower() == name.strip().lower():
            return product

    return None


def update_price(inventory, name, new_price):
    if new_price < 0:
        return False, "Price cannot be negative."

    product = search_product(inventory, name)

    if product is None:
        return False, "Product not found."

    product["price"] = new_price
    return True, "Price updated successfully."


def increase_stock(inventory, name, quantity):
    if quantity <= 0:
        return False, "Quantity must be greater than zero."

    product = search_product(inventory, name)

    if product is None:
        return False, "Product not found."

    product["stock"] += quantity
    return True, "Stock increased successfully."


def sell_product(inventory, name, quantity):
    if quantity <= 0:
        return False, "Sale quantity must be greater than zero."

    product = search_product(inventory, name)

    if product is None:
        return False, "Product not found."

    if quantity > product["stock"]:
        return False, "Not enough stock available."

    product["stock"] -= quantity

    return True, (
        f"Sale successful. Total: "
        f"{product['price'] * quantity:.2f} Birr."
    )


def calculate_inventory_value(inventory):
    total_value = 0

    for product in inventory:
        total_value += product["price"] * product["stock"]

    return total_value


def generate_low_stock_report(inventory, threshold=5):
    low_stock = []

    for product in inventory:
        if product["stock"] < threshold:
            low_stock.append(product)

    return low_stock


def display_inventory(inventory):
    print("\n===== INVENTORY =====")

    if not inventory:
        print("Inventory is empty.")
        return

    for product in inventory:
        print(
            f"Name: {product['name']} | "
            f"Price: {product['price']:.2f} Birr | "
            f"Stock: {product['stock']}"
        )


def main():
    inventory = [
        {"name": "Notebook", "price": 80, "stock": 3},
        {"name": "Pen", "price": 15, "stock": 20},
        {"name": "Bag", "price": 650, "stock": 4}
    ]

    while True:
        print("\n===== INVENTORY MENU =====")
        print("1. Add product")
        print("2. Search product")
        print("3. Update product price")
        print("4. Increase stock")
        print("5. Sell product")
        print("6. Calculate inventory value")
        print("7. Low-stock report")
        print("8. Display inventory")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        try:
            if choice == "1":
                name = input("Product name: ")
                price = float(input("Product price: "))
                stock = int(input("Initial stock: "))

                success, message = add_product(
                    inventory, name, price, stock
                )
                print(message)

            elif choice == "2":
                name = input("Enter product name: ")
                product = search_product(inventory, name)

                if product is None:
                    print("Product not found.")
                else:
                    print(product)

            elif choice == "3":
                name = input("Product name: ")
                price = float(input("New price: "))

                success, message = update_price(
                    inventory, name, price
                )
                print(message)

            elif choice == "4":
                name = input("Product name: ")
                quantity = int(input("Quantity to add: "))

                success, message = increase_stock(
                    inventory, name, quantity
                )
                print(message)

            elif choice == "5":
                name = input("Product name: ")
                quantity = int(input("Quantity to sell: "))

                success, message = sell_product(
                    inventory, name, quantity
                )
                print(message)

            elif choice == "6":
                value = calculate_inventory_value(inventory)
                print(f"Total inventory value: {value:.2f} Birr")

            elif choice == "7":
                threshold = int(
                    input("Low-stock threshold (default 5): ") or "5"
                )

                if threshold < 0:
                    print("Threshold cannot be negative.")
                    continue

                report = generate_low_stock_report(
                    inventory, threshold
                )

                print("\n===== LOW-STOCK REPORT =====")

                if not report:
                    print("No low-stock products.")
                else:
                    for product in report:
                        print(
                            f"{product['name']}: "
                            f"{product['stock']} units remaining"
                        )

            elif choice == "8":
                display_inventory(inventory)

            elif choice == "9":
                print("Inventory program closed.")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
