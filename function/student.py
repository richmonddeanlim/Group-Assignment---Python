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

# File Path 
path_student = "database/Student.txt"
path_module = "database/module.txt"

# Data Function 
# Reading data and assign it to list and make it usable
def data_reading(path):
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
            record_data.append(usable_data)

        return record_data

# View Avaible Module
# the value return the avible module and student id index(0,1)
def view_module():
    try:
        # getting all data from txt to the list
        module_record = data_reading(path_module)
        student_record = data_reading(path_student)

        #Getting list for avaible module
        # indexing 4 to above will show student module
        student_record = [student for student in student_record]
        module_list = [(module[0],module[1]) for module in module_record]

        #Getting User Tp number
        while True:
            student_id = input("Input student id (TPxxxxxx): ").strip()
            # Validating input
            if ("TP" or "Tp" or "tp" in student_id) and len(student_id) == 8:
                break
            else:
                print("Pls try again")

        # Cheking student have enrool or not [preventing duplicate data]
        student_module = []
        for student in student_record:
            if student_id == student[0]:
                for i in range (3,len(student)):
                    if len(student) == 4:
                        student_module.append(student[3])
                    else: 
                        student_module.append(student[i])
    
        # filtering the data only display the module that student haven't enroll
        avaible_module = [module for module in module_list if module[0] not in student_module]

        if avaible_module:
            # Print header
            print("=" * 60)
            print(f"{"No":^4} {'Module ID':^12} {'Module Name':^12}")
            print("=" * 60)
            # Print each data with format string ( using ^ to make center alignment)
            num = 0
            for module in avaible_module:
                num += 1
                print(f"{num:^4} {module[0]:^12} {module[1]:^12}")
            print("=" * 60)

        else:
            print("No Module are avaible")

        return avaible_module,student_id
    
    except KeyboardInterrupt:
        pass

# Enroll in module
def enroll():
    try:
        avaible_module = view_module()
        avaible_module = avaible_module[0]
        student_id = avaible_module[1]

        while True:
            enroll_choice = input("Enter the module id to enroll: ")
            if enroll_choice.upper() in [item[0] for item in avaible_module]:
                break
            else:
                print("You input the wrong id")
                
        with open(path_student,"r") as file:
            data = file.readlines()
        
        # finding the index of tp number
        i = 0
        for item in student_id:
            if item in student_id:
                break
            else:
                i += 1

        # Replacing the line in certain index
        data[i] = data[i].replace(str(f"\n"), str(f",{enroll_choice}\n"))

        # Rewrite the updated file
        with open(path_student,"w") as file:
            file.writelines(data)
        
        print("\nData have been updated\n")

    except KeyboardInterrupt:
        pass

enroll()