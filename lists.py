janbudget = 2000
jan = []
jancust = []

cust_count_jan = 0

purchase_amount = 0

facebook = 0
instagram = 0
word_of_mouth = 0
google = 0
channel_list = {facebook,instagram,word_of_mouth,google}

facebook_purchase_amt = 0
instagram_purchase_amt = 0
word_of_mouth_purchase_amt = 0
google_purchase_amt = 0
enter_another = 'y'


#Customer input for number

while enter_another == 'y':
    customer = input("Enter phone number in format (000)000-0000: ")
    while len(customer) != 13:
        print("Invalid input")
        customer = input("Enter phone number: ")

    if len(customer) == 13:
        cust_count_jan += 1
        jancust.append(customer)

    print(jancust, cust_count_jan)

#customer input for channel

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
    if channel == 1:
        facebook_purchase_amt += purchase_amount
    elif channel == 2:
        instagram_purchase_amt += purchase_amount
    elif channel == 3:
        word_of_mouth_purchase_amt += purchase_amount
    elif channel == 4:
        google_purchase_amt += purchase_amount

    enter_another = input("Enter another customer? (y/n): ")
if enter_another == 'n':
    run_report = input("Would you like to run the end of day report? (y/n): ")
    if run_report == "y":











