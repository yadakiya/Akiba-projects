
number = int(input("Enter a number: "))

if number <= 1:
    print(number, "is Not Prime")
else:
    is_prime = True

    # We only need to check divisors up to the square root.
    # If a number has a divisor greater than its square root,
    # it must also have a matching divisor smaller than it.

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is Prime")
    else:
        print(number, "is Not Prime")