import datetime

def rent_bill(user_name, kitta_numbers, land_durations, total_prices):
    file_name = user_name + "_" + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + ".txt"
    with open(file_name, 'w') as file:
        file.write("------------------------------------------------------\n")
        file.write("                  Techno Property Nepal                 \n")
        file.write("                  RENTED LAND INFORMATION                 \n")
        file.write("------------------------------------------------------\n")
        file.write("                      BILL DETAILS                        \n")
        file.write("------------------------------------------------------\n")
        file.write("Date of rent:               " + str(datetime.datetime.now()) + "\n")
        file.write("Name: " + user_name + "\n")
        file.write("------------------------------------------------------\n")
        file.write("Kitta numbers: ")
        for kitta in kitta_numbers:
            file.write(kitta + ", ")
        file.write("\n")
        file.write("------------------------------------------------------\n")
        file.write("Land Durations:\n")
        for duration in land_durations:
            file.write("- " + str(duration) + " months\n")
        file.write("------------------------------------------------------\n")
        total_amount = 0
        file.write("Amount: \n")
        for price in total_prices:
            file.write("- Rs. " + str(price) + "\n")
            total_amount += int(price)
        file.write("------------------------------------------------------\n")
        file.write("Total Amount: Rs.                               " + str(total_amount) + "\n")
        file.write("------------------------------------------------------\n\n")
        file.write("Thank you for using our service. Please visit again.\n")
        file.write("------------------------------------------------------\n")
    print("------------------------------------------------------\n")
    print("Renting Bill generated successfully: ", file_name)
    print()
    print("Thank you for using our service. Please visit again.\n")
    with open(file_name, 'r') as file:
        print(file.read())





def return_bill(user_name, kitta_nos, rent_durations, total_prices, actual_return_durations, late_fees):
    file_name = user_name + "_" + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + ".txt"
    with open(file_name, 'w') as file:
        file.write("------------------------------------------------------\n")
        file.write("                  Techno Property Nepal                 \n")
        file.write("                 RETUNED LAND INFORMATION               \n")
        file.write("------------------------------------------------------\n")
        file.write("                      BILL DETAILS                        \n")
        file.write("------------------------------------------------------\n")
        file.write("Date of return:            " + str(datetime.datetime.now()) + "\n")
        file.write("Name: " + user_name + "\n")
        file.write("------------------------------------------------------\n")
        file.write("Kitta numbers: ")
        for kitta in kitta_nos:
            file.write(kitta + ", ")
        file.write("\n")
        file.write("------------------------------------------------------\n")
        file.write("Initial Durations of Rent (in Contract):\n")
        for duration in rent_durations:
            file.write("- " + str(duration) + " months\n")
        file.write("------------------------------------------------------\n")
        file.write("Actual Return Durations:\n")
        for actual_duration in actual_return_durations:
            file.write("- " + str(actual_duration) + " months\n")
        file.write("------------------------------------------------------\n")
        late_fee_total = 0
        file.write("Late Fees:\n")
        for late_fee in late_fees:
            late_fee = int(late_fee)
            if late_fee > 0:
                late_fee_total += late_fee
                file.write("- Rs. " + str(late_fee) + "\n")
        file.write("------------------------------------------------------\n")
        file.write("Price of Each land :\n")
        grand_total = 0
        for land_price in total_prices:
            file.write("- Rs." + land_price + "\n")
            grand_total += int(land_price)
        file.write("------------------------------------------------------\n")
        file.write("Total Amount: Rs.                             " + str(grand_total) + "\n")
        file.write("------------------------------------------------------\n\n")
        file.write("Thank you for using our service. Please visit again.\n")
        file.write("------------------------------------------------------\n")
    print("------------------------------------------------------\n")
    print("Returning Bill generated successfully: ", file_name)
    print()
    print("Thank you for using our service. Please visit again.\n")
    with open(file_name, 'r') as file:
        print(file.read())


