import function, write




print("\t\t\t Welcome to Techno Rental Nepal\n")
print()
print("Press 1 to rent")
print("Press 2 to return")
print("Press 3 to exit")



end = True
while end:
    try:
        print()
        user_choice = int(input("Enter the choice to continue: "))
    except ValueError:
        print()
        print("Please enter a number from 1 to 3")
        continue

    if user_choice == 1:
        mul_kitta_no = []
        mul_rent_duration = []
        mul_total = []
        while True:
            function.display()
            data = function.rent_land()
            data = function.rent_duration(data)  
            mul_kitta_no.append(data[0])
            mul_rent_duration.append(data[4])
            mul_total.append(data[8])
            
            while True:
                try:
                    print()
                    rent_another = input("Do you want to rent another land? (yes/no): ")
                    if rent_another.lower() == "yes" or rent_another.lower() == "no":
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Enter a valid response.")
                    continue
            if rent_another.lower() == "yes":
                continue
            elif rent_another.lower() == "no":
                write.rent_bill(data[6],mul_kitta_no,mul_total,mul_rent_duration)
                break


    elif user_choice == 2:
        mul_kitta_no = []
        mul_rent_duration = []
        mul_total = []
        mul_actual_return_duration = []
        mul_late_fee = []
        while True:
            function.display()
            data = function.return_land()
            data = function.return_duration(data)

            mul_kitta_no.append(data[0])
            mul_rent_duration.append(data[8])
            mul_total.append(str(data[10]))
            mul_actual_return_duration.append(str(data[9]))
            mul_late_fee.append(str(data[10]))
            while True:
                try:
                    print()
                    rent_another = input("Want to return another land? (y/n): ")
                    if rent_another.lower() == "yes" or rent_another.lower() == "no":
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Enter Valid Response")
                    continue
            if rent_another.lower() == "yes":
                continue
            elif rent_another.lower() == "no":
                write.return_bill(data[6],mul_kitta_no,mul_rent_duration,mul_total, mul_actual_return_duration, mul_late_fee)
                break

        
    elif user_choice == 3:
        stop = False
    else: 
        print()
        print("Enter from number between 1 to 3")
