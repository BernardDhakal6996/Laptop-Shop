def read_lands():
    with open('data.txt', 'r') as file:
        data = file.read()
        return data

def customer_details():
    isvalid= False
    while not isvalid:
        user_name = str(input("Enter your name: "))
        print()
        if not user_name.isalpha():
            print()
            print("------------Please enter a valid name!------------\n")
        else:
            isvalid = True     
    isvalid = False
    while not isvalid:
        user_number = input("Enter your contact number : ")
        print()
        if not user_number.isnumeric() or len(user_number) != 10:
            print()
            print("------------Please enter a valid number------------\n")
            continue
        else:
            isvalid = True
    return user_name, user_number
        