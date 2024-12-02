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
path_attendance = "database/attendance.txt"
path_grade = "database/student_grade.txt"

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
        module_list = [(module[0],module[1]) for module in module_record]

        #Getting User Tp number
        while True:
            student_id = input("Input student id (TPxxxxxx): ").strip().upper()
            # Validating input
            for student in student_record:
                if (("TP" or "Tp" or "tp" in student_id) and len(student_id) == 8) and student_id == student[0]:
                    condition = True
                    break
                else:
                    condition = False
            if condition == True:
                break
            elif condition == False:      
                print("Tp is not found")

        # Cheking student have enrool or not [preventing duplicate data]
        student_module = []
        for student in student_record:
            if student_id.lower() == student[0]:
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
    
    except KeyboardInterrupt or FileNotFoundError:
        if FileNotFoundError:
            print('pls open from the main file directory')
        pass

# Enroll in module
def enroll():
    try:
        # Getting data that returned by the function
        function_value = view_module()
        avaible_module = function_value[0]
        student_id = function_value[1]
        
        # Getting user input and getting validation
        while True:
            enroll_choice = input("Enter the module id to enroll: ")
            if enroll_choice.upper() in [item[0] for item in avaible_module]:
                break
            else:
                print("You input the wrong id")
        
        # Read the txt file data
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

    except KeyboardInterrupt or FileNotFoundError:
        if FileNotFoundError:
            print('pls open from the main file directory')
        pass

# View Grades
def view_grade():
    try:
        # Getting the data
        student_record = data_reading(path_student)
        grade_record = data_reading(path_grade)

        # #Getting User Tp number
        while True:
            student_id = input("Input student id (TPxxxxxx): ").strip().upper()
            # Validating input
            for student in student_record:
                if (("TP" or "Tp" or "tp" in student_id) and len(student_id) == 8) and student_id == student[0]:
                    condition = True
                    break
                else:
                    condition = False
            if condition == True:
                break
            elif condition == False:      
                print("Tp is not found")

        # Fetch the student module name and grade based on student id
        grade_list = []
        for data in grade_record:
            if student_id.upper() == data[0]:
                grade_list.append([data[2],data[3],data[4]])
        
        # Print the grade
        if grade_list:
            # Print header
            print("=" * 60)
            print(f"{"No":^4} {'Module Name':^32} {'Module ID':^12} {'Grade':^12}")
            print("=" * 60)
            # Print each data with format string ( using ^ to make center alignment)
            num = 0
            for item in grade_list:
                num += 1
                print(f"{num:^4} {item[0]:<32} {item[1]:^12} {item[2]:^12}")
            print("=" * 60)

        else:
            print("No Module are avaible")

    except KeyboardInterrupt or FileNotFoundError:
        if FileNotFoundError:
            print('pls open from the main file directory')
        pass

#View Student attendance
                
view_grade()
