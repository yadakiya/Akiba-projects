customer_name = input("Enter your name: ")
product_name = input("Enter product name: ")
Price= int(input("Price of product: "))
Quantity = int(input("Number of the  product bought: "))
total = Price * Quantity

print("========================================")
print("         RECEIPT         ")
print("========================================")
print("Customer:", customer_name)
print("Product: " , product_name)
print("Price:" , Price )    
print("Quntity:"  ,Quantity)
print("---------------------------")


print("Total :" , total )
print("Thank you for shopping!")
print("========================================")