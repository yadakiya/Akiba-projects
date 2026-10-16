def add_expense(expenses, description, category, amount):
    """Add a new expense to the expense list."""
    if amount < 0:
        print("Amount cannot be negative.")
        return

    expense = {
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)


def calculate_total_expenses(expenses):
    """Calculate the total amount spent."""
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def calculate_spending_by_category(expenses):
    """Calculate total spending for each category."""
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    return category_totals


def find_largest_expense(expenses):
    """Find the expense with the largest amount."""
    if not expenses:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def find_expenses_above_threshold(expenses, threshold):
    """Find expenses greater than a specified threshold."""
    result = []

    for expense in expenses:
        if expense["amount"] > threshold:
            result.append(expense)

    return result


def calculate_category_percentages(expenses):
    """Calculate each category's percentage of total spending."""
    total = calculate_total_expenses(expenses)
    category_totals = calculate_spending_by_category(expenses)

    percentages = {}

    if total == 0:
        return percentages

    for category, amount in category_totals.items():
        percentages[category] = (amount / total) * 100

    return percentages


def find_highest_spending_category(expenses):
    """Find the category with the highest total spending."""
    category_totals = calculate_spending_by_category(expenses)

    if not category_totals:
        return None

    highest_category = max(category_totals, key=category_totals.get)

    return highest_category


def generate_spending_report(expenses, threshold=300):
    """Generate a complete spending report."""

    total = calculate_total_expenses(expenses)
    category_totals = calculate_spending_by_category(expenses)
    category_percentages = calculate_category_percentages(expenses)
    largest = find_largest_expense(expenses)
    above_threshold = find_expenses_above_threshold(expenses, threshold)
    highest_category = find_highest_spending_category(expenses)

    print("\n========== SPENDING REPORT ==========")

    print(f"Total expenses: {total:.2f} Birr")

    print("\n--- Spending by Category ---")
    for category, amount in category_totals.items():
        percentage = category_percentages[category]

        print(
            f"{category}: "
            f"{amount:.2f} Birr "
            f"({percentage:.2f}%)"
        )

    print("\n--- Largest Expense ---")
    if largest:
        print(
            f"{largest['description']} - "
            f"{largest['amount']:.2f} Birr "
            f"({largest['category']})"
        )
    else:
        print("No expenses recorded.")

    print(f"\n--- Expenses Above {threshold} Birr ---")

    if above_threshold:
        for expense in above_threshold:
            print(
                f"{expense['description']} - "
                f"{expense['amount']:.2f} Birr"
            )
    else:
        print("No expenses above the threshold.")

    print("\n--- Highest Spending Category ---")
    if highest_category:
        print(
            f"{highest_category} "
            f"({category_totals[highest_category]:.2f} Birr)"
        )
    else:
        print("No categories available.")

    print("=====================================")


# Example data
expenses = [
    {
        "description": "Lunch",
        "category": "Food",
        "amount": 180
    },
    {
        "description": "Taxi",
        "category": "Transport",
        "amount": 120
    },
    {
        "description": "Groceries",
        "category": "Food",
        "amount": 450
    },
    {
        "description": "Internet",
        "category": "Bills",
        "amount": 300
    }
]


# Add another expense
add_expense(
    expenses,
    "Coffee",
    "Food",
    80
)


# Generate report
generate_spending_report(expenses, threshold=300)