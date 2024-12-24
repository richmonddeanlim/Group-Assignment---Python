#path for easy access
student_grade_path="database/student_grade.txt"
attendance_path="database/attendance.txt"
lecture_module_path= "database/lecturer.txt"
administrator_path="database/module.txt"
student_list_path="database/student.txt"

def decoration(): #function to call decoration
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


'''
This function searches for module code in the Module.txt(from administrator)
The Module Code Only used by Registrar and don't have impact in Lecturer
'''
def get_module_code(module_name):
  try:
    with open(administrator_path, "r") as module_file: #opening administrator txt in read mode
      for line in module_file:
          try:
              code, name = line.strip().split(",")[0:2]  # assign row in txt file to variable
              if name.strip() == module_name:
                  return code
          except ValueError:
              print("There is Error in module file formatting")
              continue
      return None
  except FileNotFoundError: #in case file not found
    print("administrator.txt is not found")
    return None


#taking module list from administrator (this is because administrator could add new module)
def module_list():
    modules = [] #This list store all the module retrieved
    with open(administrator_path, "r") as admin_file:
        for line in admin_file: #for loop and split go get every value in the comma
            modules.append(line.strip().split(",")[1])
    print("---Module List---")
    for i, module in enumerate(modules, start=1): #for loop followed with indexing
        print(f"{i}. {module}")


#from the module txt(from administrator), I take every module in there and assign index into every one of them as dictionary
def get_module_dict():
    module_dict = {}
    try:
        with open(administrator_path, "r") as file:
            lines = file.readlines()
            for idx, row in enumerate(lines, start=1): #for  loop followed with indexing
                module_name= row.strip().split(",")[1]
                module_dict[str(idx)] = module_name
    except FileNotFoundError:
        print("Module file not found!")
    return module_dict


    # code for lecturer to see module
#open the name and module from txt provided by the administrator to the lecturer
def view_modules():
    print("---Search Lecturer---")

    while True:
        lecturer_code = input("Enter Lecturer Code: ").upper()
        if lecturer_code.startswith('L'):
            break
        else:
            print("Lecturer ID must start with L")

    try:
        with open(lecture_module_path, "r") as module: #opening lecturer lists
            for line in module:
                if line.startswith(lecturer_code): #getting value from every line of text file
                    name = line.strip().split(",")[1:2]
                    modules=line.strip().split(",")[2:]

                    decoration()
                    print("Your name: ",name[0])
                    print("Your assigned modules: ")
                    for subject in modules: #print every subject, use for loop because there might be more than one subject
                        print("-",subject)
                    input("Press any key to continue")
                    return
    except FileNotFoundError:
        print("Lecturer data file is not found, please add the data")

    print("Lecturer with that code is not found")
    input("Press any key to continue")

# This code will generate student_grade.txt and attendance.txt
# code for grade record


def record_grade():
    while True:
        print("---Record Student Grade---")

        while True:
            student_id = input("Enter Student ID: ").upper()
            if student_id.startswith('TP'): #validation for input
                break
            else:
                print("Student ID must start with TP")

        student_name = None
        found_student = False

        try:
            with open(student_list_path, "r") as student_file: #validate if the student exist
                for line in student_file: #read only student id and name from text
                    ids, names= line.strip().split(",")[0:2] #take value from the txt file
                    if ids.upper() == student_id:
                        student_name = names.title()  # Title case the name
                        found_student = True
                        break
        except FileNotFoundError: #If file not found
            print("student.txt file not found! Please ensure it exists.")

        if not found_student:
            decoration()
            print("Student with that ID is not found in student registration")
            print("Please Ask Registrar or Administrator to Add Student")
            decoration()
            input("Press any key to leave")
            break

        name=student_name
        decoration()
        print(f'Student Name : {name}')

        decoration()
        print("Module Lists: ")
        decoration()

        module_list()
        decoration()

        #getting module dictionary and using user input in number to match it with the dictionary
        module_dict = get_module_dict()
        num_module=len(module_dict)

        # used for the print so that it always in range of module in case the administrator add another module
        module_num = input(f"Enter Module(1-{num_module}) : ")
        module = module_dict.get(module_num)

        duplicate_found = False
        with open(student_grade_path, "r") as file: #check if the student already have grade in that module
            for line in file:
                subject = line.strip().split(",")
                if subject[0] == student_id and subject[2] == module:
                    duplicate_found = True

        if duplicate_found:#validate if the student already have grade in that module
            print("Student with that ID already has a grade in that module.")
            input("Press any key to leave")
            return

        while True: #input validation 1-100
            grade=input("Enter Student grade: ")
            if 0 < int(grade) <= 100:
                break
            else:
                print("Student grade must be in range 0-100")

        module_code = get_module_code(module)
        if not module_code:
            print("Module code not found!")
            continue

        with open(student_grade_path,"a")as add: #append student data into the txt file
            add.write(f'{student_id},{name},{module},{module_code},{grade}\n')
        print("Grade Recorded Successfully")
        decoration()

        print("Press 1 to leave")
        print("Press any other key to record new student")
        choice=input("> ")
        if choice == "1":
            break


def lecturer_menu(): #lecturer menu for user to chose
    decoration()
    print("Lecturer Management Choices")
    decoration()
    print("1. View Assigned Modules\n"
          "2. Record Student Grades\n"
          "3. Update Student Grades\n"
          "4. View Student List\n"
          "5. Mark Attendance\n"
          "6. View Student Grade\n"
          "7. Terminate the program")
    decoration()


def update_grade(): #code for grade update
    while True:
        print("---Update Student Grade---")
        while True:#get and validate student id
            student_id = input("Enter Student ID: ").upper()
            if student_id.startswith('TP'):
                break
            else:
                print("Student ID must start with TP")

        decoration()
        module_list() #displaying module list
        decoration()

        module_dict = get_module_dict()#get the dictionary for the values
        len_module=len(module_dict)

        # used for the print so that it always in range of module in case the administrator add another module
        while True:
            module_num = input(f"Enter Module to View (1-{len_module}): ")
            if int(module_num) > len_module or int(module_num) <= 0:
                print(f"Invalid input. Please enter a number between 1 to {len_module}!")
            else:
                break

        module=module_dict.get(module_num) #match the student input to the module in dictionary
        if not module:
            print("Invalid Number")
            return

        is_there=False
        found=False

        try: #check if the student grade exist
            with open(student_grade_path, "r") as grades:
                for line in grades:
                    subject=line.strip().split(",")
                    if subject[0] == student_id:
                        is_there= True
                    if subject[0] == student_id and subject[2] == module:
                        found=True

                else:
                    if not found and not is_there: #if student is not found
                        decoration()
                        print("Student ID and Module Mismatch!")
                        input("Press Enter to Exit")
                        return

                    if is_there and not found: #if student is found but don't have grade in that module
                        decoration()
                        print("That Student does not have grade in that particular module")
                        input("Press Enter to Exit")
                        return

        except FileNotFoundError:
            print("student_grade.txt is not found, please do record grade")
            return

        try:
            with open(student_grade_path,"r+") as grade:
                lines=grade.readlines() #read all lines into a list
                grade.seek(0)#move pointer back to the beginning

                for i, line in enumerate(lines):
                    subject=line.strip().split(",")
                    student_name=subject[1]
                    module_code=subject[3]

                    if subject[0]==student_id and subject[2] == module:
                        new_grade = input("Enter the new grade: ")
                        decoration()
                        print(f'Student name : {student_name}')
                        #update the lines with new grade
                        lines[i]=f'{student_id},{student_name},{module},{module_code},{new_grade}\n'
                        decoration()
                        print("Grade Updated Successfully")
                        break

                grade.writelines(lines)
                grade.truncate()#truncate extra content
                                #(I used it here because sometimes there is 2 space in the end of the txt file)
        except FileNotFoundError:
            print("student_grade.txt is not found, please do record grade")

        decoration()
        print("Press 1 to leave") #leave the def function
        print("Press any other key to update new student")
        choice = input("> ")
        if choice == "1":
            break


def view_student(): #Function to view the list of student names enrolled in a selected module
    print("---View Student List---")
    module_list() #call the function to display the list of module

    module_dict = get_module_dict()#get the dictionary for the values
    num_module=len(module_dict)#look for the total number of modules

    module_lists = input(f"Which module do you want to see? (1-{num_module}): ")
    module = module_dict.get(module_lists)

    student_name = [] #Empty List to store student name

    with open(student_grade_path, "r") as lists:
        for line in lists:
            student_id,name,student_module,module_code,grade=line.strip().split(",")
            if student_module == module:
                student_name.append(name)

    #Display the results (Student Name)
    if student_name:
        decoration()
        print(f"Student enrolled in {module}: ")
        for name in student_name:
            print(f'-{name}')
    else:
        print(f"No Student found in {module}")
    input("Press any key to continue")


def mark_attendance(): #Function to mark attendance
    try: #import students ID and Name from student list file
        with open(student_list_path, "r") as student_file:
            students = [line.strip().split(",")[0:2] for line in student_file]

        try:#open attendance file to retrieve existing attendance ID
            with open(attendance_path, "r") as attendance_file:
                attendance_ids = [line.strip().split(",")[0] for line in attendance_file]
        except FileNotFoundError:
            print("attendance.txt file not found")

        #Append new student to the attendance file
        with open(attendance_path, "a") as attendance_file:
            for student_id, student_name in students:
                if student_id not in attendance_ids:  # Check if student_id already exists in attendance file
                    attendance_file.write(f'{student_id},{student_name},0,0\n')

    except FileNotFoundError:
        print("student.txt file not found.")

    while True:
        print("---Mark Student Attendance---")
        while True:
            input_studentid = input("Enter Student ID: ").upper()
            if input_studentid.startswith('TP'):
                break
            else:
                print("Student ID must start with TP")

        try:
            with open(attendance_path, "r+") as attendance: #Open Attendance FIle to Update Attendance
                lines = attendance.readlines() #Read All Lines in file
                found= False #Check if the student ID exist
                updated=[] #list to store updated attendance record

                #Iterate through the attendance file to find and update student record
                for line in lines:
                    student_id, name, present, absent = line.strip().split(',')
                    if student_id == input_studentid:
                        found=True
                        present=int(present)
                        absent=int(absent)

                        #Display the Student Details and Attendance Percentage
                        print(f"Student Name: {name}")
                        if present + absent == 0:
                            print("No attendance recorded yet for this student")
                        else:
                            print(f"Student Attendance percentage: {present/(present+absent)*100 :.2f} %")

                        #Prompt for Attendance Status
                        attendances = input("Is student Present/Absent?").lower()
                        if attendances in ['present', 'p']:
                            present+=1
                        elif attendances in ['absent', 'a']:
                            absent+=1
                        else:
                            print("Wrong Type")
                            found=False

                        #Append the updated lines into the list
                        updated.append(f'{student_id},{name},{str(present)},{str(absent)}\n')
                    else:
                        #Append the current line into the list
                        updated.append(line)

                attendance.seek(0)
                attendance.truncate()
                attendance.writelines(updated) #Write the updated content into the file

                #Notify the user about the outcome
                if found:
                    print("Attendance Recorded Successfully")
                else:
                    print("Student with that ID not found")

                #Prompt to continue or exit
                decoration()
                print("Press 1 to leave")
                print("Press any other key to record new student")
                choice = input("> ")
                decoration()
                if choice == "1": #Exit the loop
                    break

        except FileNotFoundError:
            print("Attendance file not found, please do the record grade")


def view_student_grade(): #Function to view student grade
    #Allowing two options
    print("---View Student Grade---\n"
          "1. View All Student in Module\n"
          "2. Search for Personal Student Grade")

    choice1=input("Enter Your Choice: ")

    if choice1== "1":#View All student in a specific module
        module_list()
        module_dict = get_module_dict()#Get the module dictionary for values
        num_module = len(module_dict)

        while True:#Prompt the user to select module by its number
            module_num=input(f"Enter Module to View (1-{num_module}): ")
            if int(module_num) >num_module or int(module_num)<=0:
                print(f"Invalid input. Please enter a number between 1 to {num_module}!")
            else:
                break

        module = module_dict.get(module_num)#Get the module name based on the inputted number

        decoration()
        print(f"Student Grade for {module}")
        decoration()

        found_students = False#Flag to check if any student are found

        #Open Student Grade file and search for the student in selected module
        with open(student_grade_path, "r") as lines:
            for line in lines:
                student_id,name,student_module,module_code,grade=line.strip().split(",")
                if student_module==module:
                    print(f"{name} : {grade}")
                    found_students = True

        if not found_students:
            decoration()
            print("No students found in this module")
            decoration()

        decoration()
        input("Press any key to continue")

    elif choice1== "2":#Search for Specific Student Grade
        while True:
            stdnt_id = input("Enter Student ID: ").upper()
            if stdnt_id.startswith('TP'):
                break
            else:
                print("Student ID must start with TP")

        module_list()
        module_dict = get_module_dict()
        num_module=len(module_dict)

        module_num = input(f"Enter Module to View (1-{num_module}): ")
        module = module_dict.get(module_num)
        decoration()

        found=False

        #Open student grade file and search for specific student grade
        with open(student_grade_path, "r") as lines:
            for line in lines:
                student_id,name,student_module,module_code,grade=line.strip().split(",")
                if student_module==module and student_id==stdnt_id:
                    print(f"{name} : {grade}")
                    decoration()
                    found=True
                    input("Press any key to continue")
                    break

        if not found:
            print("Student with that ID and Module was not found")
            decoration()
            input("Press any key to continue")

    else:
        print("Wrong Choice, Try Again!")
        return


#Function for user interaction and menu
def lecturer_interface():
    try:
        while True: #Mail loop to display the menu and process user input
            lecturer_menu()
            while True:#menu input validation
                choice = input("Enter your choice: ")
                if not choice.isdigit():
                    print("Error, choice must be a number")
                    continue
                if int(choice)>7:
                    print("Error Choice")
                    continue
                break
            #Process the User Menu Choice
            if choice=="1":
                view_modules()
            elif choice=="2":
                record_grade()
            elif choice=="3":
                update_grade()
            elif choice=="4":
                view_student()
            elif choice=="5":
                mark_attendance()
            elif choice=="6":
                view_student_grade()
            elif choice=="7":
                print("Thank You for using lecturer system:)")
                break
    except KeyboardInterrupt:#In case user interrupts the program
        print("\nKeyboard Interrupt Error")
lecturer_interface() #Call the Lecturer Interface Function to start the program
