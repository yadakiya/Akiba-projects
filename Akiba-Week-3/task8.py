def validate_units(units):
    """Validate that electricity consumption is a non-negative number."""
    if units < 0:
        return False
    return True


def calculate_tier_charges(units):
    """Calculate the charge for each electricity pricing tier."""
    first_tier = min(units, 50)
    remaining = max(units - 50, 0)

    second_tier = min(remaining, 100)
    remaining = max(remaining - 100, 0)

    third_tier = remaining

    charge_first = first_tier * 0.50
    charge_second = second_tier * 0.75
    charge_third = third_tier * 1.20

    return charge_first, charge_second, charge_third


def calculate_total_bill(units, service_fee=0):
    """Calculate the total electricity bill."""
    charge_first, charge_second, charge_third = calculate_tier_charges(units)

    total = charge_first + charge_second + charge_third + service_fee

    return total


def generate_summary(units, service_fee=0):
    """Generate and display a billing summary."""
    charge_first, charge_second, charge_third = calculate_tier_charges(units)
    total = calculate_total_bill(units, service_fee)

    print("\n===== ELECTRICITY BILL =====")
    print(f"Units consumed: {units}")
    print(f"First 50 units:       {charge_first:.2f} Birr")
    print(f"Next 100 units:       {charge_second:.2f} Birr")
    print(f"Above 150 units:      {charge_third:.2f} Birr")
    print(f"Service fee:          {service_fee:.2f} Birr")
    print("-----------------------------")
    print(f"Total bill:           {total:.2f} Birr")


# Main program
try:
    units = float(input("Enter units consumed: "))

    if not validate_units(units):
        print("Units consumed cannot be negative.")
    else:
        service_fee = float(input("Enter service fee (0 if none): "))

        if service_fee < 0:
            print("Service fee cannot be negative.")
        else:
            generate_summary(units, service_fee)

except ValueError:
    print("Please enter valid numbers.")