import datetime
today = datetime.date.today()

print("Todays Date is {:%b, %d %Y}".format(today))

# Asks for amount of marketing dollars spent
marketingDollar = input("Marketing dollar spent in {:%b}: ".format(today))

# Asks for customer information
customer = input("Enter phone number: ")
listofCustomers=[customer]
while len(customer) != 10:
    print("Invalid input")
    customer = input("Enter phone number: ")

# How did you hear about us?

channel = int(input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n" ))
listofChannels= [channel]
while channel != "1" or channel != "2" or channel != "3" or channel != "4":
    print(channel)
    print("Invalid input")
    channel = input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n")



#Formulas for report

dollarperChannel = marketingDollar/channel

#Report

if channel == 0:
    report = input("Run Report? (Y/N): ")
    if report == "Y":
        print(dollarperChannel)