num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2 == num3:
    print("All three numbers are equal.")

elif num1 == num2 and num1 > num3:
    print("The largest numbers are:", num1, "and", num2)

elif num1 == num3 and num1 > num2:
    print("The largest numbers are:", num1, "and", num3)

elif num2 == num3 and num2 > num1:
    print("The largest numbers are:", num2, "and", num3)

elif num1 > num2 and num1 > num3:
    print("The largest number is:", num1)

elif num2 > num1 and num2 > num3:
    print("The largest number is:", num2)

else:
    print("The largest number is:", num3)



    