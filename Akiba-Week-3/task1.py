
def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        subtotal += item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0


def calculate_tax(amount, tax_rate):
    return amount * tax_rate


def generate_receipt(items, tax_rate):

    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    
    for item in items:
        if item["price"] < 0:
            raise ValueError("Product prices cannot be negative.")

        if item["quantity"] < 0:
            raise ValueError("Product quantities cannot be negative.")

    
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    amount_after_discount = subtotal - discount
    tax = calculate_tax(amount_after_discount, tax_rate)
    final_amount = amount_after_discount + tax

   
    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "final_amount": final_amount
    }



items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]


tax_rate = 0.15

try:
    receipt = generate_receipt(items, tax_rate)

    print("====== SHOPPING RECEIPT ======")
    print(f"Subtotal:     {receipt['subtotal']:.2f} Birr")
    print(f"Discount:     {receipt['discount']:.2f} Birr")
    print(f"Tax:          {receipt['tax']:.2f} Birr")
    print(f"Final Amount: {receipt['final_amount']:.2f} Birr")
    print("==============================")

except ValueError as error:
    print("Error:", error)
