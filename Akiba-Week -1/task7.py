
# Task 7: Travel Planner

destination = input("Enter your destination: ")
distance = float(input("Enter distance in kilometers: "))
average_speed = float(input("Enter average speed in km/h: "))

travel_time = distance / average_speed

print("\n========================================")
print("              TRAVEL PLANNER")
print("========================================")

print(f"Destination: {destination}")
print(f"Distance: {distance:g} km")
print(f"Average speed: {average_speed:g} km/h")
print(f"Estimated travel time: {travel_time:.2f} hours")

# Bonus: Display hours and minutes

hours = int(travel_time)
minutes = round((travel_time - hours) * 60)

if minutes == 60:
    hours += 1
    minutes = 0

print(f"Travel duration: {hours} hours and {minutes} minutes")
print("========================================")