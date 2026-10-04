
# Convert Celsius to Kelvin and Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Kelvin
kelvin = celsius + 273.15

# Convert Celsius to Fahrenheit
fahrenheit = celsius * 1.80 + 32.00

# Store the results in a list
ans = [kelvin, fahrenheit]

# Display the result
print("Kelvin:", kelvin)
print("Fahrenheit:", fahrenheit)
print("Answer:", ans)