student_grade_path="student_grade.txt"
attendance_path="attendance.txt"
lecture_module_path="lecturer_modules.txt"
administrator_path="administrator.txt"
student_list_path="student.txt"
def decoration(): #function to call decoration
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def get_module_code(module_name):
  try:
    with open(administrator_path, "r") as module_file:
      for line in module_file:
        code, name = line.strip().split(",")[0:2]
        if name.strip() == module_name:
          return code
      return None  # Module code not found
  except FileNotFoundError:
    print("administrator.txt is not found")
    return None
def module_list():
    modules = []
    with open(administrator_path, "r") as admin_file:
        for line in admin_file:
            modules.append(line.strip().split(",")[1])
    print("---Module List---")
    for i, module in enumerate(modules, start=1):
        print(f"{i}. {module}")
def get_module_dict():
    module_dict = {}
    try:
        with open(administrator_path, "r") as file:
            lines = file.readlines()
            for idx, row in enumerate(lines, start=1):
                module_name= row.strip().split(",")[1]
                module_dict[str(idx)] = module_name
    except FileNotFoundError:
        print("Module file not found!")
    return module_dict
    # code for lecturer to see module
def view_modules():
    print("---Search Lecturer---")
    while True:
        lecturer_code = input("Enter Lecturer Code: ").upper()
        if lecturer_code.startswith('L'):
            break
        else:
            print("Lecturer ID must start with L")
    try:
        with open(lecture_module_path, "r") as module:
            for line in module:
                if line.startswith(lecturer_code):
                    name = line.strip().split(",")[1:2]
                    modules=line.strip().split(",")[2:]
                    decoration()
                    print("Your name: ",name[0])
                    print("Your assigned modules: ")
                    for subject in modules:
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
            if student_id.startswith('TP'):
                break
            else:
                print("Student ID must start with TP")
        student_name = None
        found_student = False
        try:
            with open(student_list_path, "r") as student_file:
                for line in student_file:
                    ids, names= line.strip().split(",")[0:2]
                    if ids.upper() == student_id:
                        student_name = names.title()  # Title case the name
                        found_student = True
                        break
        except FileNotFoundError:
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
        module_dict = get_module_dict()
        num_module=len(module_dict)
        module_num = input(f"Enter Module(1-{num_module}) : ")
        module = module_dict.get(module_num)
        duplicate_found = False
        with open(student_grade_path, "r") as file:
            for line in file:
                subject = line.strip().split(",")
                if subject[0] == student_id and subject[2] == module:
                    duplicate_found = True
        if duplicate_found:
            print("Student with that ID already has a grade in that module.")
            input("Press any key to leave")
        while True:
            grade=input("Enter Student grade: ")
            if 0 < int(grade) <= 100:
                break
            else:
                print("Student grade must be in range 0-100")
        module_code = get_module_code(module)
        if not module_code:
            print("Module code not found!")
            continue
        #record input into the "write" which will be appended to student_grade.txt
        with open(student_grade_path,"a")as add:
            add.write(f'{student_id},{name},{module},{module_code},{grade}\n')
        print("Grade Recorded Successfully")
        decoration()
        print("Press 1 to leave")
        print("Press any other key to record new student")
        choice=input("> ")
        with open(attendance_path,"a") as add_name:
            add_name.write(f'{student_id},{name},0,0\n')
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
        while True:
            student_id = input("Enter Student ID: ").upper()
            if student_id.startswith('TP'):
                break
            else:
                print("Student ID must start with TP")
        decoration()
        module_list()
        decoration()
        module_dict = get_module_dict()
        len_module=len(module_dict)
        while True:
            module_num = input(f"Enter Module to View (1-{len_module}): ")
            if int(module_num) > len_module or int(module_num) <= 0:
                print(f"Invalid input. Please enter a number between 1 to {len_module}!")
            else:
                break
        module=module_dict.get(module_num)
        if not module:
            print("Invalid Number")
            return
        found=False
        is_there=False
        try:
            with open(student_grade_path,"r+") as grade:
                lines=grade.readlines()
                grade.seek(0)
                for i, line in enumerate(lines):
                    subject=line.strip().split(",")
                    student_name=subject[1]
                    module_code=subject[3]
                    if subject[0]==student_id:
                        is_there=True
                    if subject[0]==student_id and subject[2] == module:
                        found=True
                        new_grade = input("Enter the new grade: ")
                        decoration()
                        print(f'Student name : {student_name}')
                        lines[i]=f'{student_id},{student_name},{module},{module_code},{new_grade}\n'
                        decoration()
                        print("Grade Updated Successfully")
                        break
                if not found and not is_there:
                    decoration()
                    print("Student ID and Module Mismatch!")
                if is_there and not found:
                    decoration()
                    print("That Student does not have grade in that module")
                grade.writelines(lines)
                grade.truncate()
        except FileNotFoundError:
            print("student_grade.txt is not found, please do record grade")
        decoration()
        print("Press 1 to leave")
        print("Press any other key to update new student")
        choice = input("> ")
        if choice == "1":
            break

def view_student(): #Code to see student name in each module
    print("---View Student List---")
    module_list()
    module_dict = get_module_dict()
    num_module=len(module_dict)
    module_lists = input(f"Which module do you want to see? (1-{num_module}): ")
    module = module_dict.get(module_lists)
    student_name = []
    with open(student_grade_path, "r") as lists:
        for line in lists:
            student_id,name,student_module,module_code,grade=line.strip().split(",")
            if student_module == module:
                student_name.append(name)
    if student_name:
        decoration()
        print(f"Student enrolled in {module}: ")
        for name in student_name:
            print(f'-{name}')
    else:
        print(f"No Student found in {module}")
    input("Press any key to continue")

def mark_attendance(): #code to mark attendance
    while True:
        print("---Mark Student Attendance---")
        while True:
            input_studentid = input("Enter Student ID: ").upper()
            if input_studentid.startswith('TP'):
                break
            else:
                print("Student ID must start with TP")
        try:
            with open(attendance_path, "r+") as attendance:
                lines = attendance.readlines()
                found= False
                updated=[]
                for line in lines:
                    student_id, name, present, absent = line.strip().split(',')
                    if student_id == input_studentid:
                        found=True
                        present=int(present)
                        absent=int(absent)
                        print(f"Student Name: {name}")
                        if present + absent == 0:
                            print("No attendance recorded yet for this student")
                        else:
                            print(f"Student Attendance percentage: {present/(present+absent)*100 :.2f} %")
                        attendances = input("Is student Present/Absent?").lower()
                        if attendances in ['present', 'p']:
                            present+=1
                        elif attendances in ['absent', 'a']:
                            absent+=1
                        else:
                            print("Wrong Type")
                            found=False
                        updated.append(f'{student_id},{name},{str(present)},{str(absent)}\n')
                    else:
                        updated.append(line)
                attendance.seek(0)
                attendance.truncate()
                attendance.writelines(updated)
                if found:
                    print("Attendance Recorded Successfully")
                else:
                    print("Student with that ID not found")
                decoration()
                print("Press 1 to leave")
                print("Press any other key to record new student")
                choice = input("> ")
                decoration()
                if choice == "1":
                    break
        except FileNotFoundError:
            print("Attendance file not found, please do the record grade")


def view_student_grade(): #code to view student grade
    print("---View Student Grade---\n"
          "1. View All Student in Module\n"
          "2. Search for Personal Student Grade")
    choice1=input("Enter Your Choice: ")
    if choice1== "1":
        module_list()
        module_dict = get_module_dict()
        num_module = len(module_dict)
        while True:
            module_num=input(f"Enter Module to View (1-{num_module}): ")
            if int(module_num) >num_module or int(module_num)<=0:
                print(f"Invalid input. Please enter a number between 1 to {num_module}!")
            else:
                break
        module = module_dict.get(module_num)
        decoration()
        print(f"Student Grade for {module}")
        decoration()
        found_students = False
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
    elif choice1== "2":
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
    
def main():
    try:
        while True:
            lecturer_menu()
            while True:
                choice = input("Enter your choice: ")
                if not choice.isdigit():
                    print("Error, choice must be a number")
                    continue
                if int(choice)>7:
                    print("Error Choice")
                    continue
                break
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
            elif choice=="6":
                view_student_grade()
            elif choice=="7":
                print("Thank You for using lecturer system:)")
                break
            else:
                print("Wrong Input")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt Error")
lecturer_interface()
