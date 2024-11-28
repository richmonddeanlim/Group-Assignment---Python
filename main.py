from function import accountant

try:
    while True:
        print("="*50)
        print(f"{"University Management System":^50}")
        print("="*50)
        print("1.Administrator")
        print("2.Lecturer")
        print("3.Student")
        print("4.Registrar")
        print("5.Accountant")
        print("6.Exit")
        print("="*50)

        while True:
            try:
                function_choice = int(input("Input your option: "))
                break
            except ValueError:
                print("Pls Input an Interger")

        if function_choice == 1:
            # copy paste the main here
            pass 

        elif function_choice == 2:
            # copy paste the main here
            pass

        elif function_choice == 3:
            # copy paste the main here
            pass
        
        elif function_choice == 4:
            # copy paste the main here
            pass
        
        elif function_choice == 5:
            while True:
                try:
                    # Getting user Choice
                    choice = accountant.menu()

                    # Open record menu
                    if choice == 1:
                        print("\n")
                        accountant.fee_record()

                    # View Outstanding fee
                    elif choice == 2:
                        print("\n")
                        accountant.outstanding_fee()

                    # Update payment information
                    elif choice == 3:
                        print("\n")
                        accountant.update_fee()

                    # Print receipt
                    elif choice == 4:
                        print("\n")
                        accountant.receipt()

                    # Viewing Financial Summary
                    elif choice == 5:
                        print("\n")
                        accountant.financial_summary()

                    #Exit 
                    elif choice == 6:
                        print("Thank You for using the program")
                        break

                    # When keyboard interrupt it will return False on the function
                    elif choice == False:
                        break

                    print("\n")
                
                except KeyboardInterrupt:
                    print("\n\nExiting")
        
        elif function_choice == 6:
            break

        else:
            print("That option is not available")

except KeyboardInterrupt:
    exit