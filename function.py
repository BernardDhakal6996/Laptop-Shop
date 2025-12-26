import read
def display():
    show_lands = read.read_lands()  
    print()
    print("-"*80)
    print("Kitta".ljust(10, ' '), "City".ljust(13, ' '), "Anna".ljust(12, ' '), "Price".ljust(9, ' '), "Availability Status")
    print("-"*80)
    for item in show_lands.split('\n'):
        data = item.strip().split(',')
        if len(data) == 6: 
            print(f"{data[0]: <10}{data[1]:<13} {data[3]:<9}  {data[4]:<12}  {data[5]}")
    print("-"*80)
    

def rent_duration(data):
    while True:
        rent_duration = input("Enter the duration of rent: ")
        if not rent_duration.isdigit():
            print("------------Invalid input. Please enter a valid duration.------------\n")
            continue
        data.append(rent_duration)
        total_price =  int(rent_duration) * int(data[4])
        data.append(total_price)
        print()
        print("Your total is : Rs.", total_price)
        
        # Update availability status of the selected land in the file
        with open('data.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)  # Move the file pointer to the beginning
            for line in lines:  
                line_data = line.strip().split(',')
                if line_data[0] == data[0]:  
                    line_data[5] = " Unavailable" 
                    line = ','.join(line_data) + '\n'  
                file.write(line)  # Write the line back to the file
            file.truncate()  
        break
    return data

def rent_land():
    while True:
        print()
        kitta_no = input("Enter the kitta number: ")
        if  kitta_no.isdigit() == False or int(kitta_no) < 100 or int(kitta_no) > 999:
            print("------------Inavlid Kitta number. Please enter a number (100 - 999)------------.")
            continue
        with open('data.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                kitta_no = int(kitta_no)
                if int(data[0]) == kitta_no :
                    if data[5].strip().lower()== "available":
                        print()
                        print("------------Found. The land is available for renting.------------\n")
                        name, num = read.customer_details()
                        data.append(name)
                        data.append(num)
                        return data
                    else:
                        print("------------Not found. The land is not available for renting.------------")
                        break
    
def return_duration(data):
    while True:
        initial_rent_duration = input("Enter the initial duration of rent: ")
        if not initial_rent_duration.isdigit():
            print("------------Invalid input. Please enter a valid duration.------------")
            continue
        
        actual_return_duration = input("Enter the actual return duration: ")
        if not actual_return_duration.isdigit():
            print("------------Invalid input. Please enter a valid duration.------------")
            continue

        initial_rent_duration = int(initial_rent_duration)
        actual_return_duration = int(actual_return_duration)

        data.append(initial_rent_duration)
        data.append(actual_return_duration)

        total_price =  initial_rent_duration * int(data[4])
        data.append(total_price)

        if actual_return_duration > initial_rent_duration:
            late_duration = actual_return_duration - initial_rent_duration
            late_fee = late_duration * (int(data[4]) * 0.1)  # 10% fine per month
            total_price += late_fee
            print()
            print("Your total is price is : ", total_price)
            print("Your late fee is : ", late_fee)
            print()
        else:
            print()
            print("Your total is : ", total_price)
            print()

        # Update availability status of the selected land in the file
        with open('data.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)  # Move the file pointer to the beginning
            for line in lines:  
                line_data = line.strip().split(',')
                if line_data[0] == data[0]:  
                    line_data[5] = " Available" 
                    line = ','.join(line_data) + '\n'  
                file.write(line)  # Write the line back to the file
            file.truncate()  
        break
    return data


def return_land():
    while True:
        kitta_no = input("Enter the kitta number: ")          
        if not kitta_no.isdigit():
            print("------------Invalid Kitta number.------------")
            continue
        with open('data.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)  # Move the file pointer to the beginning
            for i, line in enumerate(lines):
                data = line.strip().split(',')
                if int(data[0]) == int(kitta_no):
                    if data[5].strip().lower() == "unavailable":
                        print()
                        print("------------Found. The land is available for renting.------------\n")
                        # Clear customer details and availability status
                        name, num = read.customer_details()
                        data.append(name)
                        data.append(num)
                        return data
                    else:
                        print("------------Land with this kitta number is not rented.------------")
                        break
            else:
                print("------------Kitta number not found.------------")
    
                    
            
                    
            


