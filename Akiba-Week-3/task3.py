
def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def get_divisors(number):
    divisors = []

    if number <= 0:
        return divisors

    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)

    return divisors


def sum_of_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total


def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_value = 0

    while number > 0:
        digit = number % 10
        reversed_value = reversed_value * 10 + digit
        number = number // 10

    return sign * reversed_value


def analyze_number(number):
    if number == 0:
        number_type = "Zero"
    elif number % 2 == 0:
        number_type = "Even"
    else:
        number_type = "Odd"

    analysis = {
        "number": number,
        "even_or_odd": number_type,
        "is_prime": is_prime(number),
        "sum_of_digits": sum_of_digits(number),
        "reversed_number": reverse_number(number),
        "divisors": get_divisors(number)
    }

    return analysis


try:
    number = int(input("Enter an integer: "))

    result = analyze_number(number)

    print("\n===== NUMBER ANALYSIS =====")
    print(f"Number:          {result['number']}")
    print(f"Type:            {result['even_or_odd']}")
    print(f"Is prime:        {result['is_prime']}")
    print(f"Sum of digits:   {result['sum_of_digits']}")
    print(f"Reversed number: {result['reversed_number']}")
    print(f"Divisors:        {result['divisors']}")
    print("===========================")

except ValueError:
    print("Error: Please enter a valid integer.")
