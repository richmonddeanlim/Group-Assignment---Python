from datetime import datetime

# Need to be like this because when running in diff directory it could cause module not found
# so whenever running from this directory or in main directory will not cause module error
try:
    from function.student import data_reading as read
    from function.student import path_student
except ModuleNotFoundError:
    from student import data_reading as read
    from student import path_student

# Creating menu for user to choose 
def menu():
    try:
        # Displaying menu for usern
        print("=" * 32)
        print(f"{"Accountant Menu":^32}")
        print("=" * 32)
        print("1.Tuition Fee Record")
        print("2.Outstanding Tuition Fee List")
        print("3.Update Payment")
        print("4.Tuition Fee Receipts")
        print("5.Financial Summary")
        print("6.Exit")
        print("=" * 32)

        while(True):
            try:
                # Getting User Choice
                choice = int(input("Choose your choices (1-5): "))
                # Validating user input
                if choice in range(1,7):
                    # Returning value to the function
                    return choice
                else:
                    print("There is an error pls try again")
            except ValueError:
                print("Pls input integer")
                
            
    # Showing error display
    except KeyboardInterrupt:
        print("\n\nExiting")
        return False

#File Path 
path = "database/accountant.txt"

# Data Function 
# Reading data and assign it to list and make it usable
def data_reading():
        # Making the txt file to variable
        with open(path, "r") as file:
            raw_data = file.readlines()

        # Checking how much data inside the txt files
        txt_data = len(raw_data)

        # Cleaning the data and this is the record data
        record_data = []

        for x in range(0,txt_data):
            usable_data = raw_data[x].replace("\n","").split(",")
            # Change the data type to integer
            usable_data[3] = int(usable_data[3])
            record_data.append(usable_data)

        return record_data

# Fee record function
def fee_record():
    try:
        # Giving the option
        print("=" * 30)
        print(f"{"Fee record":^30}")
        print("=" * 30)
        print("1.View Record")
        print("2.Add Record")
        print("3.Reset Record")
        print("4.Exit")
        print("=" * 30)

        while True:
            choice = int(input("Select the option: "))

            # View the record
            if choice == 1:
                print("\n")
                try:
                    record_data = data_reading()
                    
                    # Print the record data
                    if record_data:
                            # Print header
                            print(f"{"Record Fee":^70}")
                            print("=" * 70)
                            print(f"{"No":^4} {'Date':^12} {'Student ID':^12} {'Name':^15} {'Fee_Amount':^12} {'Status':^10}")
                            print("=" * 70)
                            # Print each data with format string ( using ^ to make center alignment)
                            num = 0
                            for data in record_data:
                                num += 1
                                print(f"{num:^4} {data[0]:^12} {data[1]:^12} {data[2]:^15} {data[3]:^12} {data[4]:^10}")
                            print("=" * 70)
                    else:
                        print("No record found")

                    input("Press enter to continue")

                except KeyboardInterrupt:
                    print("\n\nExiting")

                break
                
            # Adding Record
            elif choice == 2:
                while True:
                    try:
                        # Getting user input
                        while True:
                            format  ="%d-%m-%Y"
                            date = input("Input the date (dd-mm-yyyy): ")

                            try:
                                # The datetime.strptime will returm boolean value
                                if bool(datetime.strptime(date, format)):
                                   break

                            except ValueError:
                                print("Date format incorect")
                                

                        while True:
                            student_record = read(path_student)
                            student_id = input("Input student id (TPxxxxxx): ").strip().upper()
                            # Validating input
                            for Student in student_record:
                                if (("TP" or "Tp" or "tp" in student_id) and len(student_id) == 8) and student_id == Student[0]:
                                    condition = True
                                    break
                                else:
                                    condition = False
                            if condition == True:
                                break
                            elif condition == False:      
                                print("Tp is not found")


                        student_name = input("Input Student name: ")

                        while True:
                            # Getting an input with value error handling
                            try:
                                fee = int(input("Input the total amount of fee: ").strip())
                                break
                            except ValueError:
                                print("Pls enter a integer")

                        while True:
                            # Validating input
                            fee_status = input("Input the status (Paid/Unpaid): ").strip()
                            lowercase_str = fee_status.lower()
                            if lowercase_str in ["unpaid","paid"]:
                                break
                            else:
                                print("Pls try again")

                        # list variable
                        # The title make sure all is Capital in the first word or in Name writing
                        fee_data = [info for info in [date,student_id.upper(),student_name.title(),fee,fee_status.title()]]

                        # Adding new file in the last text file
                        with open(path, "a") as file:
                            # Write the list to the txt file
                            file.write(",".join(map(str,fee_data)).strip())
                            file.write("\n")

                        # creating a certain condition to stop looping of add data record 
                        choice = input("\nPress enter to continue (0 to stop): ")
                        if choice == "0":
                            break
                        else:
                            continue

                    # Clarify if any error occur
                    except KeyboardInterrupt or FileNotFoundError:
                        if KeyboardInterrupt:
                            print("\n\nExiting The Program")
                            break
                        elif FileNotFoundError:
                            print("Make sure you run from the Group Assignment folder")
                            break
                break
            
            # Reset the record
            elif choice == 3:
                with open(path, "w") as file :
                    file.write("")

                print("\nThe File has been reset")
                input("Press enter to exit")
                break

            #exit
            elif choice == 4:
                break
            
            # Telling user input there is no that option
            else:
                print("That option is not available")

    except KeyboardInterrupt:
        print("\n\nExiting")


# Outstanding Fee View Function
def outstanding_fee():
    try:
        record_data = data_reading()

        # Using list comprehension to find and append the data that have unpaid status
        unpaid_record = [record for record in record_data if record[4].lower() == "unpaid"]
        
        # Print the unpaid_record table ( when the list is empty it will return False )
        if unpaid_record:
                # Print header
                print(f"{"Outstanding Fee":^70}")
                print("=" * 70)
                print(f"{"No":^4} {'Date':^12} {'Student ID':^12} {'Name':^15} {'Fee_Amount':^12} {'Status':^10}")
                print("=" * 70)
                # Print each data with format string ( using ^ to make center alignment)
                num = 0
                for data in unpaid_record:
                    num += 1
                    print(f"{num:^4} {data[0]:^12} {data[1]:^12} {data[2]:^15} {data[3]:^12} {data[4]:^10}")
                print("=" * 70)
        else:
            print("No outstanding fees found.")
        
        input("Press enter to continue")

    except KeyboardInterrupt:
        print("\n\nExiting")

# Update payment status
def update_fee():
    try:
        # Taking the data list into the variable
        record_data = data_reading()

        # Print the record data
        if record_data:
            # Print header
            print("=" * 70)
            print(f"{"No":^4} {'Date':^12} {'Student ID':^12} {'Name':^15} {'Fee_Amount':^12} {'Status':^10}")
            print("=" * 70)
            # Print each data with format string ( using ^ to make center alignment)
            num = 0
            for data in record_data:
                num += 1
                print(f"{num:^4} {data[0]:^12} {data[1]:^12} {data[2]:^15} {data[3]:^12} {data[4]:^10}")
            print("=" * 70)

        else:
            print("No record data is found")

        # Validating input
        while True:
            try:
                update = int(input("Input the number of data that want to be update: "))
                if update in range(1,len(record_data)):
                    break
                else:
                    print(f"There is no data on num {update}")
            except ValueError:
                print("Pls input a integer")

        # Open and read the data
        with open(path, "r") as file:
            data = file.readlines()
        
        # Change the payment status for the txt file
        print(" ")
        print("=" * 20)
        print(f"{"Change option":^20}")
        print("=" * 20)
        print("1.Total pay amount")
        print("2.Payment status")
        print("3.Exit")
        print("=" * 20)

        # Validating input
        while True:
            try:
                change_choice = int(input("Input the number of option: "))
                break
                
            except ValueError:
                print("Pls input a integer")
        
        # Choice 1
        if change_choice == 1:
            while True:
                try:
                    value = int(input("Input the fee amount: "))
                    break
                    
                except ValueError:
                    print("Pls input a integer")

            old_value = record_data[update-1][3]
            data[update-1] = data[update - 1].replace(str(old_value),str(value))

            with open(path,"w") as file:
                file.writelines(data)
            
            input("Press enter to continue")


        # Choice 2
        elif change_choice == 2:
            while True:
                try:
                    status = input("Change payment status(Paid/Unpaid): ")

                    if status.lower() in ["paid","unpaid"] :
                        input("Press enter to continue")
                        break

                    else:
                        print("Pls try again")
                    
                except ValueError:
                    print("Pls input a integer")

            if status.lower() == "paid":
                data[update-1] = data[update - 1].replace("Unpaid","Paid")
                
                with open(path,"w") as file:
                    file.writelines(data)

            elif status.lower() == "unpaid":
                data[update-1] = data[update - 1].replace("Paid","Unpaid")
            
                with open(path,"w") as file:
                    file.writelines(data)
            else:
                print("Pls try again")
        
        # Choice 3
        elif change_choice == 3:
            exit

        # Write the modified text 

    except KeyboardInterrupt:
        print("\n\nExiting the program")

# Print Receipt
def receipt():
    try:
        # Getting the data
        record_data = data_reading()   

        # Filtering the data
        paid_data = [data for data in record_data if data[4] == "Paid"]

        # Print the available data to print the receipt
        print(f"{"Available receipt":^70}")
        if paid_data:
            # Print header
            print("=" * 70)
            print(f"{"No":^4} {'Date':^12} {'Student ID':^12} {'Name':^15} {'Fee_Amount':^12} {'Status':^10}")
            print("=" * 70)
            # Print each data with format string ( using ^ to make center alignment)
            num = 0
            for data in paid_data:
                num += 1
                print(f"{num:^4} {data[0]:^12} {data[1]:^12} {data[2]:^15} {data[3]:^12} {data[4]:^10}")
            print("=" * 70)

        else:
            print("No student have paid can't print receipt")

        # Validating input
        while True:
            try:
                choice = int(input("Input the number of data that want to be print: "))
                if choice in range(1,(len(paid_data) + 1)):
                    break
                else:
                    print(f"There is no data on num {choice}")
            except ValueError:
                print("Pls input a integer")
        
        # Put the list into a variable that want to print
        receipt_data = paid_data[choice - 1]

        print("\n")
        # Print the receipt
        print("=" * 30)
        print(f"{"receipt":^30}")
        print("=" * 30)
        print(f"Student ID   : {receipt_data[1]}")
        print(f"Student Name : {receipt_data[2]}")
        print(f"Fee Amount   : {receipt_data[3]}")
        print(f"Pay Amount   : {receipt_data[3]}")
        print("=" * 30)
        input("Press enter to continue")

        print("\n")
        # Saving the receipt
        with open("receipt.txt", "r") as file :
            file.writelines("=" * 30)
            file.writelines(f"\n{"receipt":^30}\n")
            file.writelines("=" * 30)
            file.writelines(f"\nStudent ID   : {receipt_data[1]}")
            file.writelines(f"\nStudent Name : {receipt_data[2]}")
            file.writelines(f"\nFee Amount   : {receipt_data[3]}")
            file.writelines(f"\nPay Amount   : {receipt_data[3]}\n")
            file.writelines("=" * 30)

        print("The receipt have been saved in receipt.txt")
        input("Press enter to continue")
    
    except KeyboardInterrupt:
        print("\n\nExiting")


# View Financial Summary
def financial_summary():
    try:
        # getting the data
        record_data = data_reading()

        # Categorized the data
        unpaid_data = [fee[3] for fee in record_data if fee[4] == "Unpaid"]
        paid_data = [fee[3] for fee in record_data if fee[4] == "Paid"]

        # Sum all the fee
        unpaid_fee = sum(unpaid_data)
        paid_fee = sum(paid_data)
        total = paid_fee - unpaid_fee

        #Print the Financial Summary
        print("=" * 30)
        print(f"{"Financial Summary":^30}")
        print("=" * 30)
        print(f"Paid Fee   : {paid_fee}")
        print(f"Unpaid Fee : {unpaid_fee}")
        print("=" * 30)
        print(f"Total       : {total}")
        input("Press enter to continue")

    except KeyboardInterrupt:
        print("\n\nExiting")

# This is the main function program for Uni management system
def main():
    while True:
        try:
            # Getting user Choice
            choice = menu()

            # Open record menu
            if choice == 1:
                print("\n")
                fee_record()

            # View Outstanding fee
            elif choice == 2:
                print("\n")
                outstanding_fee()

            # Update payment information
            elif choice == 3:
                print("\n")
                update_fee()

            # Print receipt
            elif choice == 4:
                print("\n")
                receipt()

            # Viewing Financial Summary
            elif choice == 5:
                print("\n")
                financial_summary()

            #Exit 
            elif choice == 6:
                break

            # When keyboard interrupt it will return False on the function
            elif choice == False:
                break

            print("\n")
        
        except KeyboardInterrupt:
            print("\n\nExiting")