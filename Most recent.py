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

listof_phonenumbers = []
cust_count_month = 0 #Global Variable

cust_count_day = 0
facebook = 0
instagram = 0
word_of_mouth = 0
google = 0



tot_purchase_amount_month = 0  # Global Variable

tot_purchase_amount_day = 0
facebook_purchase_amt = 0
instagram_purchase_amt = 0
word_of_mouth_purchase_amt = 0
google_purchase_amt = 0
fl_purchase_amount = 0

# User prompt for month, date, and marketing budget
# Need Checkers to check for valid day and that no repeats are made



dateday = int(input("Enter a day as an integer (eg. 1-31): "))

while dateday < 1 or dateday >= 32: #### Crashes if 33 is entered???
    print("Invalid input")
    dateday = input("Enter a day: ")

# Begin loop for daily data
# Customer input for number
# Duplicate number checker for listof_phonenumbers



enter_another = 'y'

while enter_another == 'y':
    customer = input("Enter phone number in format (000)000-0000: ")

    #### Need an int checker here ###

    while len(customer) != 13:
        print("\nInvalid input")
        customer = input("Enter phone number: ")

#### FIGURE THIS OUT #### Need a loop to make sure no duplicates are are entered to the phone list.
   ### and append number to the list

   # FIXED IT. Don't use the same bool for your overall loop and for your phone check. Your issue was thay you were appending the number
   # to the list first, and then checking if it existed in the list afterwards. So it was always detecting duplicates.

    ask_for_number = True

    while ask_for_number:
        if customer in listof_phonenumbers:
            print("\nThis number already exists.")
            customer = input("Enter phone number: ")
        else:
            listof_phonenumbers.append(customer)
            ask_for_number = False


    # Customer input for channel increases count by +1 per channel

    channel = input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n")

    while channel != '1' and channel != '2' and channel != '3' and channel != '4':
        print("\nInvalid input")
        channel =  input("How did you hear about us? \n 1.) Facebook \n 2.) Instagram \n 3.) Word of mouth\n 4.) Google \n")

    if channel == '1':
        facebook += 1
        cust_count_month += 1
        cust_count_day += 1
    elif channel == '2':
        instagram += 1
        cust_count_month += 1
        cust_count_day += 1
    elif channel == '3':
        word_of_mouth += 1
        cust_count_month += 1
        cust_count_day += 1
    elif channel == '4':
        google += 1
        cust_count_month += 1
        cust_count_day += 1

# What was the purchase amount?

    purchase_amount = input("What was the purchase amount? (eg. 123.33): ")
    while purchase_amount.isalpha() and type(purchase_amount) == str or purchase_amount == "":
        print("\nInvalid input")
        purchase_amount = input("What was the purchase amount? (eg. 123.33): ")

    # Converts purchase_amount to float
    fl_purchase_amount = float(purchase_amount)
    tot_purchase_amount_month += fl_purchase_amount
    tot_purchase_amount_day += fl_purchase_amount

    if channel == '1':
        facebook_purchase_amt += fl_purchase_amount
    elif channel == '2':
        instagram_purchase_amt += fl_purchase_amount
    elif channel == '3':
        word_of_mouth_purchase_amt += fl_purchase_amount
    elif channel == '4':
        google_purchase_amt += fl_purchase_amount

    # Loop BREAK for customer input

    enter_another = input("Enter another customer? (y/n): ")
    while enter_another != "y" and enter_another != 'n':
        print("\nInvalid input")
        enter_another = input("Enter another customer? (y/n): ")


if enter_another == 'n':

# function for finding avg of sales per channel
    def percent(x):
        return "{:.0%}".format(x/tot_purchase_amount_day)

# Need to append correct data to lists




run_report = input("Would you like to run the end of day report? (y/n): ")

while run_report != "y" and run_report != 'n':
    print("\nInvalid input")
    run_report = input("Would you like to run the end of day report? (y/n): ")


if run_report == "y":
    print("\nTotal number of customers entered for today is: ", cust_count_day)
    print("Total amount of sales entered for today is: ",tot_purchase_amount_day)
    print("\nNumber of customers from:")
    print("Facebook \t Instagram \t Word of Mouth \t Google")
    print(facebook,"\t\t\t",instagram,"\t\t\t",word_of_mouth,"\t\t\t\t",google)
    print("\nPercentage of sales in:")
    print("Facebook \t Instagram \t Word of Mouth \t Google")
    print(percent(facebook_purchase_amt),"\t\t",percent(instagram_purchase_amt),"\t\t",percent(word_of_mouth_purchase_amt),"\t\t\t",percent(google_purchase_amt))


d1.append(cust_count_day) ## Number of customers for day 1
d1.append(tot_purchase_amount_day ) ## total purchase amount for d1
d1.append(facebook_purchase_amt)
d1.append(instagram_purchase_amt)
d1.append(word_of_mouth_purchase_amt)
d1.append(google_purchase_amt) ## percentage of dollars per channel


new_day = input("Would you like to begin a new day? (y/n)")
while new_day != "y" and new_day != 'n':
    print("\nInvalid input")
    new_day = input("Would you like to begin a new day? (y/n)")

while new_day == "n":
    view_phonelist = input("Would you like to view the list of phone numbers? (y/n): ")
    while view_phonelist != "y" and view_phonelist != 'n':
        print("Invalid input")
        view_phonelist = input("Would you like to view the list of phone numbers? (y/n): ")

    if view_phonelist == "y":
        print(listof_phonenumbers)
        new_day = input("Would you like to begin a new day? (y/n)")
        while new_day != "y" and new_day != 'n':
            print("\nInvalid input")
            new_day = input("Would you like to begin a new day? (y/n)")

    elif view_phonelist == "n":
        new_day = input("Would you like to begin a new day? (y/n)")


    elif run_report == "n":
        view_phonelist = input("Would you like to view the list of phone numbers? (y/n): ")
        if view_phonelist == "y":
            print(listof_phonenumbers)
            new_day = input("\nWould you like to begin a new day? (y/n)")
        while new_day == "n":
            new_day = input("\nWould you like to begin a new day? (y/n)")




if new_day == "y":


#### need to append the day list with sales data listed in the proposal

# Returns count to ZERO for new day

    facebook = 0
    instagram = 0
    word_of_mouth = 0
    google = 0


    facebook_purchase_amt = 0
    instagram_purchase_amt = 0
    word_of_mouth_purchase_amt = 0
    google_purchase_amt = 0
    tot_purchase_amount = 0


