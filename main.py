from function import accountant
from function import student
from function import lecture

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
            print("\n")
            lecture.main()
            

        elif function_choice == 3:
            print("\n")
            student.main()
                
        elif function_choice == 4:
            # copy paste the main here
            pass
        
        elif function_choice == 5:
            print("\n")
            accountant.main()
        
        elif function_choice == 6:
            print("\nExiting the program")
            break

        else:
            print("That option is not available")

except KeyboardInterrupt:
    exit