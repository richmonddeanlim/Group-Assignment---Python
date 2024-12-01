# Diplaying student module
def menu():
    try:
        # Displaying menu for user
        print("=" * 32)
        print(f"{"Student Menu":^32}")
        print("=" * 32)
        print("1.View Avaible Modules")
        print("2.Enrol in Module")
        print("3.View Gradces")
        print("4.Acess Attendance Record")
        print("5.Unenroll from Module")
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
    
# For View Avaible module for student
def view_module(path):
    with open(path,'r') as file:
        pass
