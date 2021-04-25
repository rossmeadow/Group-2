# Definition of Variables

# Globals 

data = {} ### Using a dictionary so that we can dynamically add all days here for monthly comparison ###
cust_count_month = 0
tot_purchase_amount_month = 0
total_facebook = 0
total_instagram = 0
total_word = 0
total_google = 0


def dollar_format(x):
    return "${:,.2f}".format(x)

# function to format percentages of purchase amounts
def percentOfTotal(val):
    return "{:.0%}".format(val/tot_purchase_amount_month)

# function to calculate and print monthly report
def showMonth():
    fb_total = 0
    insta_total = 0
    word_total = 0
    google_total = 0

### Indexs data in temp list in dict. for month report ##

    for key in data:
        temp = data[key]
        fb_total += temp[3]
        insta_total += temp[4]
        word_total += temp[5]
        google_total += temp[6]

    print("\nMonthy sales for respective channel:")
    print(dollar_format(fb_total),"\t", dollar_format(insta_total),"\t", dollar_format(word_total),"\t", dollar_format(google_total))
    print("\nTotal number of customers entered for the month is: ", cust_count_month)
    print("Total amount of sales entered for the month is: ",dollar_format(tot_purchase_amount_month))
    print("\nNumber of monthly customers from:")
    print("Facebook \t Instagram \t Word of Mouth \t Google")
    print(total_facebook,"\t\t\t",total_instagram,"\t\t\t",total_word,"\t\t\t\t",total_google)
    print("\nPercentage of monthly sales in:")
    print("Facebook \t Instagram \t Word of Mouth \t Google")
    print(percentOfTotal(fb_total),"\t\t",percentOfTotal(insta_total),"\t\t",percentOfTotal(word_total),"\t\t\t",percentOfTotal(google_total))

# User prompt for month, date, and marketing budget
# Need Checkers to check for valid day and that no repeats are made

new_day = input("\nWould you like to begin a new day? (y/n)")

while new_day == "y":

### RESETS COUNT TO ZERO FOR NEW DAY ###

    cust_count_day = 0
    facebook = 0
    instagram = 0
    word_of_mouth = 0
    google = 0

    tot_purchase_amount_day = 0
    facebook_purchase_amt = 0
    instagram_purchase_amt = 0
    word_of_mouth_purchase_amt = 0
    google_purchase_amt = 0
    fl_purchase_amount = 0

    dateday = int(input("Enter a day as an integer (eg. 1-31): "))

    while dateday < 1 or dateday > 31: #### Crashes if 33 is entered??? ####
        print("Invalid input")
        dateday = input("Enter a day: ")

    # Begin loop for daily data
    # Customer input for number
    # Duplicate number checker for listof_phonenumbers

    listof_phonenumbers = []
    enter_another = 'y'

    while enter_another == 'y':
        customer = input("Enter phone number in format (000)000-0000: ")
        while len(customer) != 13:
            print("\nInvalid input")
            customer = input("Enter phone number: ")

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
            total_facebook += 1
        elif channel == '2':
            instagram += 1
            total_instagram += 1
        elif channel == '3':
            word_of_mouth += 1
            total_word += 1
        elif channel == '4':
            google += 1
            total_google += 1
        
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

        def showday():
            print("\nDaily sales for respective channel:")
            print(dollar_format(facebook_purchase_amt),"\t",dollar_format(instagram_purchase_amt)
                  ,"\t",dollar_format(word_of_mouth_purchase_amt),"\t",dollar_format(google_purchase_amt))
            print("\nTotal number of customers entered for today is: ", cust_count_day)
            print("Total amount of sales entered for today is: ", dollar_format(tot_purchase_amount_day))
            print("\nNumber of customers from:")
            print("Facebook \t Instagram \t Word of Mouth \t Google")
            print(facebook, "\t\t\t", instagram, "\t\t\t", word_of_mouth, "\t\t\t\t", google)
            print("\nPercentage of sales in:")
            print("Facebook \t Instagram \t Word of Mouth \t Google")
            print(percent(facebook_purchase_amt), "\t\t", percent(instagram_purchase_amt), "\t\t",
                  percent(word_of_mouth_purchase_amt), "\t\t\t", percent(google_purchase_amt))

    run_report = input("Would you like to run the end of day report? (y/n): ")
    while run_report != "y" and run_report != 'n':
        print("\nInvalid input")
        run_report = input("Would you like to run the end of day report? (y/n): ")

    if run_report == "y":
        showday()

### Appends temp list with customer data ####

    temp = []
    temp.append(listof_phonenumbers)
    temp.append(cust_count_day) ## Number of customers for the current day
    temp.append(tot_purchase_amount_day ) ## total purchase amount for the current day
    temp.append(facebook_purchase_amt)
    temp.append(instagram_purchase_amt)
    temp.append(word_of_mouth_purchase_amt)
    temp.append(google_purchase_amt) ## percentage of dollars per channel

### Appends dictionary with temp lists ###

    data[dateday] = temp

    new_day = input("\nWould you like to begin a new day? (y/n)")
    while new_day != "y" and new_day != 'n':
        print("\nInvalid input")
        new_day = input("Would you like to begin a new day? (y/n)")

    if new_day == "n":
        view_phonelist = input("Would you like to view todays list of phone numbers? (y/n): ")
        while view_phonelist != "y" and view_phonelist != 'n':
            print("Invalid input")
            view_phonelist = input("Would you like to view todays list of phone numbers? (y/n): ")

        if view_phonelist == "y":
            print(listof_phonenumbers)

        show_month = input("\nPress \"y\" to run the monthly report, and anything else to end the program: ")

        if (show_month == 'y'):
            # call the function to calculate and print monthly report, and finish running the program
            showMonth()
