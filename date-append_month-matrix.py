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

month = [
    [d1],
    [d1],
    [d2],
    [d3],
    [d4],
    [d5],
    [d6],
    [d7],
    [d8],
    [d9],
    [d10],
    [d11],
    [d12],
    [d13],
    [d14],
    [d15],
    [d16],
    [d17],
    [d18],
    [d19],
    [d20],
    [d21],
    [d22],
    [d23],
    [d24],
    [d25],
    [d26],
    [d27],
    [d28],
    [d29],
    [d30],
    [d31],]

# Definition of Variables


cust_count_month = 0 #Global Variable
tot_purchase_amount_month = 0  # Global Variable



# User prompt for month, date, and marketing budget
# Need Checkers to check for valid day and that no repeats are made
new_day = input("\nWould you like to begin a new day? (y/n)")


while new_day == "y":

### RETURNS COUNT TO ZERO FOR NEW DAY ###

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

    while dateday < 1 or dateday >= 32: #### Crashes if 33 is entered??? ####
        print("Invalid input")
        dateday = input("Enter a day: ")

    # Begin loop for daily data
    # Customer input for number
    # Duplicate number checker for listof_phonenumbers

    listof_phonenumbers = []
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
        print(percent(facebook_purchase_amt),"\t\t",percent(instagram_purchase_amt),"\t\t",percent(word_of_mouth_purchase_amt),"\t\t\t",percent(google_purchase_amt),"\n")

    if dateday == 1:
        d1.append(listof_phonenumbers)
        d1.append(cust_count_day) ## Number of customers for day 1
        d1.append(tot_purchase_amount_day ) ## total purchase amount for d1
        d1.append(facebook_purchase_amt)
        d1.append(instagram_purchase_amt)
        d1.append(word_of_mouth_purchase_amt)
        d1.append(google_purchase_amt) ## percentage of dollars per channel
    elif dateday == 2:
        d2.append(listof_phonenumbers)
        d2.append(cust_count_day)
        d2.append(tot_purchase_amount_day)
        d2.append(facebook_purchase_amt)
        d2.append(instagram_purchase_amt)
        d2.append(word_of_mouth_purchase_amt)
        d2.append(google_purchase_amt)
    elif dateday == 3:
        d3.append(listof_phonenumbers)
        d3.append(cust_count_day)
        d3.append(tot_purchase_amount_day)
        d3.append(facebook_purchase_amt)
        d3.append(instagram_purchase_amt)
        d3.append(word_of_mouth_purchase_amt)
        d3.append(google_purchase_amt)
    elif dateday == 4:
        d4.append(listof_phonenumbers)
        d4.append(cust_count_day)
        d4.append(tot_purchase_amount_day)
        d4.append(facebook_purchase_amt)
        d4.append(instagram_purchase_amt)
        d4.append(word_of_mouth_purchase_amt)
        d4.append(google_purchase_amt)
    elif dateday == 5:
        d5.append(listof_phonenumbers)
        d5.append(cust_count_day)
        d5.append(tot_purchase_amount_day)
        d5.append(facebook_purchase_amt)
        d5.append(instagram_purchase_amt)
        d5.append(word_of_mouth_purchase_amt)
        d5.append(google_purchase_amt)
    elif dateday == 6:
        d6.append(listof_phonenumbers)
        d6.append(cust_count_day)
        d6.append(tot_purchase_amount_day)
        d6.append(facebook_purchase_amt)
        d6.append(instagram_purchase_amt)
        d6.append(word_of_mouth_purchase_amt)
        d6.append(google_purchase_amt)
    elif dateday == 7:
        d7.append(listof_phonenumbers)
        d7.append(cust_count_day)
        d7.append(tot_purchase_amount_day)
        d7.append(facebook_purchase_amt)
        d7.append(instagram_purchase_amt)
        d7.append(word_of_mouth_purchase_amt)
        d7.append(google_purchase_amt)
    elif dateday == 8:
        d8.append(listof_phonenumbers)
        d8.append(cust_count_day)
        d8.append(tot_purchase_amount_day)
        d8.append(facebook_purchase_amt)
        d8.append(instagram_purchase_amt)
        d8.append(word_of_mouth_purchase_amt)
        d8.append(google_purchase_amt)
    elif dateday == 9:
        d9.append(listof_phonenumbers)
        d9.append(cust_count_day)
        d9.append(tot_purchase_amount_day)
        d9.append(facebook_purchase_amt)
        d9.append(instagram_purchase_amt)
        d9.append(word_of_mouth_purchase_amt)
        d9.append(google_purchase_amt)
    elif dateday == 10:
        d10.append(listof_phonenumbers)
        d10.append(cust_count_day)
        d10.append(tot_purchase_amount_day)
        d10.append(facebook_purchase_amt)
        d10.append(instagram_purchase_amt)
        d10.append(word_of_mouth_purchase_amt)
        d10.append(google_purchase_amt)
    elif dateday == 11:
        d11.append(listof_phonenumbers)
        d11.append(cust_count_day)
        d11.append(tot_purchase_amount_day)
        d11.append(facebook_purchase_amt)
        d11.append(instagram_purchase_amt)
        d11.append(word_of_mouth_purchase_amt)
        d11.append(google_purchase_amt)
    elif dateday == 12:
        d12.append(cust_count_day)
        d12.append(tot_purchase_amount_day)
        d12.append(facebook_purchase_amt)
        d12.append(instagram_purchase_amt)
        d12.append(word_of_mouth_purchase_amt)
        d12.append(google_purchase_amt)
    elif dateday == 13:
        d13.append(cust_count_day)
        d13.append(tot_purchase_amount_day)
        d13.append(facebook_purchase_amt)
        d13.append(instagram_purchase_amt)
        d13.append(word_of_mouth_purchase_amt)
        d13.append(google_purchase_amt)
    elif dateday == 14:
        d14.append(cust_count_day)
        d14.append(tot_purchase_amount_day)
        d14.append(facebook_purchase_amt)
        d14.append(instagram_purchase_amt)
        d14.append(word_of_mouth_purchase_amt)
        d14.append(google_purchase_amt)
    elif dateday == 15:
        d15.append(cust_count_day)
        d15.append(tot_purchase_amount_day)
        d15.append(facebook_purchase_amt)
        d15.append(instagram_purchase_amt)
        d15.append(word_of_mouth_purchase_amt)
        d15.append(google_purchase_amt)
    elif dateday == 16:
        d16.append(cust_count_day)
        d16.append(tot_purchase_amount_day)
        d16.append(facebook_purchase_amt)
        d16.append(instagram_purchase_amt)
        d16.append(word_of_mouth_purchase_amt)
        d16.append(google_purchase_amt)
    elif dateday == 17:
        d17.append(cust_count_day)
        d17.append(tot_purchase_amount_day)
        d17.append(facebook_purchase_amt)
        d17.append(instagram_purchase_amt)
        d17.append(word_of_mouth_purchase_amt)
        d17.append(google_purchase_amt)
    elif dateday == 18:
        d18.append(cust_count_day)
        d18.append(tot_purchase_amount_day)
        d18.append(facebook_purchase_amt)
        d18.append(instagram_purchase_amt)
        d18.append(word_of_mouth_purchase_amt)
        d18.append(google_purchase_amt)
    elif dateday == 19:
        d19.append(cust_count_day)
        d19.append(tot_purchase_amount_day)
        d19.append(facebook_purchase_amt)
        d19.append(instagram_purchase_amt)
        d19.append(word_of_mouth_purchase_amt)
        d19.append(google_purchase_amt)
    elif dateday == 20:
        d20.append(cust_count_day)
        d20.append(tot_purchase_amount_day)
        d20.append(facebook_purchase_amt)
        d20.append(instagram_purchase_amt)
        d20.append(word_of_mouth_purchase_amt)
        d20.append(google_purchase_amt)
    elif dateday == 21:
        d21.append(cust_count_day)
        d21.append(tot_purchase_amount_day)
        d21.append(facebook_purchase_amt)
        d21.append(instagram_purchase_amt)
        d21.append(word_of_mouth_purchase_amt)
        d21.append(google_purchase_amt)
    elif dateday == 22:
        d22.append(cust_count_day)
        d22.append(tot_purchase_amount_day)
        d22.append(facebook_purchase_amt)
        d22.append(instagram_purchase_amt)
        d22.append(word_of_mouth_purchase_amt)
        d22.append(google_purchase_amt)
    elif dateday == 23:
        d23.append(cust_count_day)
        d23.append(tot_purchase_amount_day)
        d23.append(facebook_purchase_amt)
        d23.append(instagram_purchase_amt)
        d23.append(word_of_mouth_purchase_amt)
        d23.append(google_purchase_amt)
    elif dateday == 24:
        d24.append(cust_count_day)
        d24.append(tot_purchase_amount_day)
        d24.append(facebook_purchase_amt)
        d24.append(instagram_purchase_amt)
        d24.append(word_of_mouth_purchase_amt)
        d24.append(google_purchase_amt)
    elif dateday == 25:
        d25.append(cust_count_day)
        d25.append(tot_purchase_amount_day)
        d25.append(facebook_purchase_amt)
        d25.append(instagram_purchase_amt)
        d25.append(word_of_mouth_purchase_amt)
        d25.append(google_purchase_amt)
    elif dateday == 26:
        d26.append(cust_count_day)
        d26.append(tot_purchase_amount_day)
        d26.append(facebook_purchase_amt)
        d26.append(instagram_purchase_amt)
        d26.append(word_of_mouth_purchase_amt)
        d26.append(google_purchase_amt)
    elif dateday == 27:
        d27.append(cust_count_day)
        d27.append(tot_purchase_amount_day)
        d27.append(facebook_purchase_amt)
        d27.append(instagram_purchase_amt)
        d27.append(word_of_mouth_purchase_amt)
        d27.append(google_purchase_amt)
    elif dateday == 28:
        d28.append(cust_count_day)
        d28.append(tot_purchase_amount_day)
        d28.append(facebook_purchase_amt)
        d28.append(instagram_purchase_amt)
        d28.append(word_of_mouth_purchase_amt)
        d28.append(google_purchase_amt)
    elif dateday == 29:
        d29.append(cust_count_day)
        d29.append(tot_purchase_amount_day)
        d29.append(facebook_purchase_amt)
        d29.append(instagram_purchase_amt)
        d29.append(word_of_mouth_purchase_amt)
        d29.append(google_purchase_amt)
    elif dateday == 30:
        d30.append(cust_count_day)
        d30.append(tot_purchase_amount_day)
        d30.append(facebook_purchase_amt)
        d30.append(instagram_purchase_amt)
        d30.append(word_of_mouth_purchase_amt)
        d30.append(google_purchase_amt)
    else:
        d31.append(cust_count_day)
        d31.append(tot_purchase_amount_day)
        d31.append(facebook_purchase_amt)
        d31.append(instagram_purchase_amt)
        d31.append(word_of_mouth_purchase_amt)
        d31.append(google_purchase_amt)

    new_day = input("Would you like to begin a new day? (y/n)")
    while new_day != "y" and new_day != 'n':
        print("\nInvalid input")
        new_day = input("Would you like to begin a new day? (y/n)")

    while new_day == "n":
        EOM_report = input("Would you like to view the end of month report? (y/n): ")
        while EOM_report != "y" and EOM_report != 'n':
            print("Invalid input")
            EOM_report = input("Would you like to view the end of month report? (y/n): ")

        if EOM_report == "y":
            for i in month:
                for j in i:
                    print(j, end=" ")
                print()

            new_day = input("Would you like to begin a new day? (y/n)")

        elif EOM_report == "n":
            new_day = input("\nWould you like to begin a new day? (y/n)")




if new_day == "n":

    EOM_report = input("Would you like to view the end of month report? (y/n)")


if EOM_report == "y":
    print("Metrics")
    for i in month:
        for j in i:
            print(j, end=" ")
        print()






























### NEED TO START LIST COMPARISONS FOR END OF MONTH ###



