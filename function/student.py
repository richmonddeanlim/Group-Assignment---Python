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
                choice = int(input("Choose your choices (1-6): "))
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
path_student = "database/student.txt"
path_module = "database/module.txt"
path_attendance = "database/attendance.txt"
path_grade = "database/student_grade.txt"

# Data Function 
# Reading data and assign it to list and make it usable
def data_reading(path):
    try:
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
    
    except FileNotFoundError:
        print("pls open with the main file directory location")

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

        input("\nPress enter to continue")

        return avaible_module,student_id

    
    except KeyboardInterrupt:
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
            
            choice = input("enter to continue (0 to stop): ")

            if choice == "0":
                break
            else:
                continue


    except FileNotFoundError:
        print('pls open from the main file directory')
    
    except KeyboardInterrupt :
        pass

    except TypeError:
        pass # passing since the error only happen if i keyboard intterupt and no input

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
            input("\nPress enter to continue")

        else:
            print("No grade are avaible\n")
            input("Press enter to continue")

    except KeyboardInterrupt:
       pass

#View Student attendance
def student_attendance():
    try:
        # Getting the data
            student_record = data_reading(path_student)
            attendance_record = data_reading(path_attendance)

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
            attendance_list = []
            for data in attendance_record:
                if student_id.upper() == data[0]:
                    attendance_list.append(float(data[2]))
                    attendance_list.append(float(data[3]))

            percentage = (attendance_list[0]/(attendance_list[1]+attendance_list[0]))*100

            print(f"Your attendance percentage is: {percentage:.2f}%\n")
            input("Press enter to continue")

    except ZeroDivisionError:
        if attendance_list[0] == 0 and attendance_list[1] == 0:
            print("You never attend or absent any classes\n")
            input("Press enter to continue")

        elif attendance_list[0] > 0 and attendance_list[1] == 0:
            print("Zero Devision Error")
    
    except KeyboardInterrupt:
        pass
    
    except IndexError:
        print("This student did not have any record")
        
#Unenroll Function
def unenroll():
    try:
        # Getting data that returned by the function
        student_record = data_reading(path_student)
        
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
        unenroll_module = []
        for student in student_record:
            if student_id == student[0]:
                for i in range (3,len(student)):
                    if len(student) == 4:
                        unenroll_module.append(student[3])
                    else: 
                        unenroll_module.append(student[i])

        if unenroll_module:
            # Print header
            print("=" * 30)
            print(f"{"No":^4} {'Module ID':^12} ")
            print("=" * 30)
            # Print each data with format string ( using ^ to make center alignment)
            num = 0
            for module_id in unenroll_module:
                num += 1
                print(f"{num:^4} {module_id:^12} ")
            print("=" * 30)

            while True:
            # Getting user input and getting validation
                while True:
                    unenroll_choice = input("Enter the module id to unenroll: ")
                    if unenroll_choice.upper() in [item for item in unenroll_module]:
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
                data[i] = data[i].replace(str(f",{unenroll_choice}"), str(f""))

                # Rewrite the updated file
                with open(path_student,"w") as file:
                    file.writelines(data)
                
                choice = input("enter to continue (0 to stop): ")

                if choice == "0":
                    break
                else:
                    continue

        else:
            print("No Module are avaible")
            input("\nPress enter to continue")
            
    except FileNotFoundError:
        print('pls open from the main file directory')
    
    except KeyboardInterrupt :
        pass

# This is the main function  of student for Uni management system
def main():
    while True:
        try:
            # Getting user Choice
            choice = menu()

            # View Module
            if choice == 1:
                print("")
                view_module()

            # Enroll to the module
            elif choice == 2:
                print("")
                enroll()

            # View Grade
            elif choice == 3:
                print("")
                view_grade()

            # View Student attendance
            elif choice == 4:
                print("")
                student_attendance()

            # Unenroll from the module
            elif choice == 5:
                print("")
                unenroll()

            #Exit 
            elif choice == 6:
                print("Thank You for using the program")
                break

            # When keyboard interrupt it will return False on the function menu()
            elif choice == False:
                break

            print("")
        
        except KeyboardInterrupt:
            pass