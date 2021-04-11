# Asks for amount of marketing dollars spent
input("Marketing dollar spent this month: ")

# Asks for customer information
customer = input("Enter phone number: ")
while len(customer) != 10:
    print("Invalid input")
    customer = input("Enter phone number: ")

# How did you hear about us?
channel = input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n" )
while channel != 0:
    input("Enter customer phone number: ")
    channel = input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n")
    if channel == 0:
        break

