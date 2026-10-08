
largest = None
smallest = None
total = 0
even_count = 0
odd_count = 0

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))

    if largest is None or number > largest:
        largest = number

    if smallest is None or number < smallest:
        smallest = number

    total += number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / 10

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)