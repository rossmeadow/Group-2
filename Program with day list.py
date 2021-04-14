
#Establishes lists of data for each possible day of the month

d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []
d7 = []
d8 = []
d9 = []
d10 = []
d11 = []
d12 = []
d13 = []
d14 = []
d15 = []
d16 = []
d17 = []
d18 = []
d19 = []
d20 = []
d21 = []
d22 = []
d23 = []
d24 = []
d25 = []
d26 = []
d27 = []
d28 = []
d29 = []
d30 = []
d31 = []

#Definition of Variables

cust_count = 0
listof_phonenumbers = []
purchase_amount = 0

facebook = 0
instagram = 0
word_of_mouth = 0
google = 0

facebook_purchase_amt = 0
instagram_purchase_amt = 0
word_of_mouth_purchase_amt = 0
google_purchase_amt = 0
tot_purchase_amount = 0

#User prompt for month, date, and marketing budget

datemonth = input("Enter a month: ")
marketing_dollars = float(input("How much money was spent on marketing in ", datemonth," ? (eg $1000.00):" ))
dateday = int(input("Enter a day: "))

# Begin loop for daily data
# Customer input for number

enter_another = 'y'
while enter_another == 'y':
    customer = input("Enter phone number in format (000)000-0000: ")
    while len(customer) != 13:
        print("Invalid input")
        customer = input("Enter phone number: ")

    if len(customer) == 13:
        cust_count += 1
        listof_phonenumbers.append(customer)

    print(listof_phonenumbers, cust_count)

# Customer input for channel increases count by +1 per channel

    channel = int(input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n" ))

    while channel < 1 or channel > 4:
        print("Invalid input")
        channel = int(input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n"))
    if channel == 1:
        facebook +=1
    elif channel == 2:
        instagram += 1
    elif channel == 3:
        word_of_mouth += 1
    elif channel == 4:
        google += 1

# What was the purchase amount?

    purchase_amount = float(input("What was the purchase amount? (eg. 123.33): "))
    tot_purchase_amount += purchase_amount
    if channel == 1:
        facebook_purchase_amt += purchase_amount
    elif channel == 2:
        instagram_purchase_amt += purchase_amount
    elif channel == 3:
        word_of_mouth_purchase_amt += purchase_amount
    elif channel == 4:
        google_purchase_amt += purchase_amount

# Loop BREAK for customer input

    enter_another = input("Enter another customer? (y/n): ")
if enter_another == 'n':

# Need to establish loop for new day
# Begin end of day report line... need to do formulas.

    run_report = input("Would you like to run the end of day report? (y/n): ")
    if run_report == "y":
        print("Total number of customers entered for ",datemonth," ", dateday," is: ", cust_count)
        print(facebook_purchase_amt)
        print(word_of_mouth_purchase_amt/purchase_amount)
        print(google_purchase_amt/purchase_amount)

# Adds input data to the d1 list

        if dateday == 1:
            d1.append(purchase_amount)
            d1.append(cust_count)
            d1.append(tot_purchase_amount)

# Returns count to ZERO for new day

facebook = 0
instagram = 0
word_of_mouth = 0
google = 0
channel_list = [facebook,instagram,word_of_mouth,google]

facebook_purchase_amt = 0
instagram_purchase_amt = 0
word_of_mouth_purchase_amt = 0
google_purchase_amt = 0
tot_purchase_amount = 0

