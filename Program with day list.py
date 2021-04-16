# Establishes lists of data for each possible day of the month

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

# Definition of Variables

cust_count = 0
listof_phonenumbers = []


facebook = 0
instagram = 0
word_of_mouth = 0
google = 0

fl_purchase_amount = 0
facebook_purchase_amt = 0
instagram_purchase_amt = 0
word_of_mouth_purchase_amt = 0
google_purchase_amt = 0
tot_purchase_amount = 0

# User prompt for month, date, and marketing budget
# Need Checkers
datemonth = input("Enter a month: ")
marketing_dollars = input("How much money was spent on marketing? (eg. 10000.00): ")
dateday = input("Enter a day: ")

# Begin loop for daily data
# Customer input for number
# Duplicate number checker for listof_phonenumbers

j = 0
k = 0
duplicates = False
enter_another = 'y'

while enter_another == 'y' and duplicates == False:
    customer = input("Enter phone number in format (000)000-0000: ")
    #### Need an int checker here ###
    while len(customer) != 13:
        print("Invalid input")
        customer = input("Enter phone number: ")

    if len(customer) == 13:
        cust_count += 1
        listof_phonenumbers.append(customer)
        for j in range(0, len(listof_phonenumbers)):
            for k in range(0, len(listof_phonenumbers)):
                if (listof_phonenumbers[k] == listof_phonenumbers[j] and j != k):
                    duplicates = True
                    print("This number already exists.")
                    customer = input("Enter phone number: ")


    # Customer input for channel increases count by +1 per channel

    channel = int(
        input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n"))

# Needs failsafe against CH input

    while channel < 1 or channel > 4:
        print("Invalid input")
        channel = int(
            input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n"))
    if channel == 1:
        facebook += 1
    elif channel == 2:
        instagram += 1
    elif channel == 3:
        word_of_mouth += 1
    elif channel == 4:
        google += 1

# What was the purchase amount?

    purchase_amount = input("What was the purchase amount? (eg. 123.33): ")
    while purchase_amount.isalpha() and type(purchase_amount) == str or purchase_amount == "":
        print("Invalid input")
        purchase_amount = input("What was the purchase amount? (eg. 123.33): ")

    # Converts purchase_amount to float
    fl_purchase_amount = float(purchase_amount)




    tot_purchase_amount += fl_purchase_amount
    if channel == 1:
        facebook_purchase_amt += fl_purchase_amount
    elif channel == 2:
        instagram_purchase_amt += fl_purchase_amount
    elif channel == 3:
        word_of_mouth_purchase_amt += fl_purchase_amount
    elif channel == 4:
        google_purchase_amt += fl_purchase_amount

    # Loop BREAK for customer input

    enter_another = input("Enter another customer? (y/n): ")
    while enter_another != "y" and enter_another != 'n':
        print("Invalid input")
        enter_another = input("Enter another customer? (y/n): ")


if enter_another == 'n':

# function for finding avg of sales per channel
    def percent(x):
        return "{:.0%}".format(x/tot_purchase_amount)

# Need to append correct data to lists

    if dateday == 1:
        d1.append(fl_purchase_amount)
        d1.append(cust_count)
        d1.append(tot_purchase_amount)


    run_report = input("Would you like to run the end of day report? (y/n): ")

while run_report != "y" and run_report != 'n':
    print("Invalid input")
    run_report = input("Would you like to run the end of day report? (y/n): ")


    if run_report == "y":
        print("\nTotal number of customers entered for",datemonth, dateday, "is: ", cust_count)
        print("Total amount of sales entered for",datemonth, dateday, "is: ",tot_purchase_amount)
        print("\nNumber of customers from:")
        print("Facebook \t Instagram \t Word of Mouth \t Google")
        print(facebook,"\t\t\t",instagram,"\t\t\t",word_of_mouth,"\t\t\t\t",google)
        print("\nPercentage of sales in:")
        print("Facebook \t Instagram \t Word of Mouth \t Google")
        print(percent(facebook_purchase_amt),"\t\t",percent(instagram_purchase_amt),"\t\t",percent(word_of_mouth_purchase_amt),"\t\t\t",percent(google_purchase_amt))

        new_day = input("\nWould you like to begin a new day? (y/n)")
        while new_day != "y" and new_day != 'n':
            print("Invalid input")
            new_day = input("\nWould you like to begin a new day? (y/n)")

        while new_day == "n":
            view_phonelist = input("Would you like to view the list of phone numbers? (y/n): ")
            while view_phonelist != "y" and view_phonelist != 'n':
                print("Invalid input")
                view_phonelist = input("Would you like to view the list of phone numbers? (y/n): ")

            if view_phonelist == "y":
                print(listof_phonenumbers)
                new_day = input("Would you like to begin a new day? (y/n)")
                while new_day != "y" and new_day != 'n':
                    print("Invalid input")
                    new_day = input("Would you like to begin a new day? (y/n)")

            elif view_phonelist == "n":
                new_day = input("Would you like to begin a new day? (y/n)")


    elif run_report == "n":
        view_phonelist = input("Would you like to view the list of phone numbers? (y/n): ")
        if view_phonelist == "y":
            print(listof_phonenumbers)
            new_day = input("Would you like to begin a new day? (y/n)")

        elif view_phonelist == "n":
            new_day = input("Would you like to begin a new day? (y/n)")

        while new_day == "n":
            new_day = input("Would you like to begin a new day? (y/n)")




if new_day == "y":
    print("next day")


# Returns count to ZERO for new day

facebook = 0
instagram = 0
word_of_mouth = 0
google = 0
channel_list = [facebook, instagram, word_of_mouth, google]

facebook_purchase_amt = 0
instagram_purchase_amt = 0
word_of_mouth_purchase_amt = 0
google_purchase_amt = 0
tot_purchase_amount = 0
