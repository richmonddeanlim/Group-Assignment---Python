import random #importing the module random
student_path = "database/student.txt" #stores student records.
enrollment_path = "database/enrollment.txt" #stores student's enrollments.
transcript_path = "database/transcript.txt" #stores student transcript.
module_path = "database/module.txt" #store modules.
student_grade_path = "database/student_grade.txt" #stores student's grades.

#function to create random student ID and avoid unavailable student ID.
def create_student_ID():
    while True:
        ID_num = ''.join(str(random.randint (0, 9))for _ in range (6)) #creating student ID (numbers).
        student_ID = f"TP{ID_num}" #student ID starting with "TP".

        #opens student_path to access/read student's informations.
        with open(student_path, 'r') as file:
            created_ID = [line.split(',')[0] for line in file]

            if student_ID not in created_ID: #to ensure that the student ID does not exist in the student_path, so there's no duplicate.
                return student_ID
            
#function to register a new student into the student_path file.
def register_new_student():
    while True: #
        student_ID = create_student_ID() #taking the available student ID from the function create_student_ID.
        print(f"\nAvailable student_ID: ", student_ID)

        confirmation = input("\nKeep this student ID? (yes or no): ").lower() #letting the users to confirm their student ID.
        if confirmation == "yes": #inputting "yes" means it's the student ID that will be saved in the student file later on.
            break
        elif confirmation == "no": #while inputting "no" will produce a new student ID.
            continue
        else:
            print("\nInvalid input, please input a valid choice (yes or no)!") #making sure the option chosen is only "yes" or "no".
    while True:
        name = input("Enter student's name: ").strip() #input student's name
        if not all(char.isalpha() or char.isspace() for char in name): #to make sure the name is valid.
            print("\nPlease input student's name with only letters and spaces!")
            continue
        break

    while True:
        available_programs = ["Computing", "Business"] #to show the available programs.
        print(f"\nAvailable programs: {', '.join(available_programs)}")
        program = input("Please choose one of the programs above: ") #prompt user to input student's program.
        program = program.title()

        if program not in available_programs: #ensuring that the program is available.
            print("\nPlease input a valid program and check spellings!")
            continue
        break

    try:
        with open(student_path, 'a') as file: #to append the student information into the file.
            file.writelines(f"{student_ID},{name},{program}\n")
        print("\nStudent has been registered.")
    except KeyboardInterrupt: #handling interruption.
        print("\nInterrupted, exiting...")

#functino to update student records/information.
def update_student_records():
    while True:
        student_ID = input("Enter student's ID: ").strip() #to ensure student ID is valid.
        if not len(student_ID) == 8 and student_ID.startswith("TP"):
            print("\nPlease input the correct student ID!")
            continue
        break

    while True:
        new_name = input("Enter student's new name (leave blank to kee current name): ") #input new student's name.
        if not all(char.isalpha() or char.isspace() for char in new_name): #ensuring it's valid.
            print("\nPlease input valid name!")
            continue
        break

    available_programs = ["Computing", "Business"] #available programs
    print(f"\nAvailable programs: {', '.join(available_programs)}")

    while True:
        new_program = input("Enter student's new program (leave blank to keep current program): ") #input new student's program.
        new_program = new_program.title()
        if new_program not in available_programs: #ensuring that the program is available.
            print("\nPlease input a valid program and check spellings!")
            continue
        break

    try:
        updated_records = []
        found = False
        with open(student_path, 'r') as file: #read the student file to search for the student ID.
            for line in file:
                record = line.strip().split(',')
                if record[0] == student_ID:
                    if new_name:
                        record[1] = new_name #rename the student.

                    if new_program:
                        record[2] = new_program #change student's program.
                found = True
            updated_records.append(",".join(record) + "\n")
    
        if found:
            with open(student_path, 'w') as file: #rewrite the student records.
                file.writelines(updated_records)
            print("\nStudent record updated successfully.")
        else:
            print("\nStudent ID doesn's exist.")
    except FileNotFoundError: #file is not found.
        print("\nStudent file not found.")
    except KeyboardInterrupt: #handling interruption.
        print("\nCancelled, exiting...")

#function to get available modules.
def available_modules():
        available_modules = [] #list of available modules.
        try:
            with open("module.txt", 'r') as file: #opens and reads the module.txt.
                for line in file:
                    module_id, module_name, credits = line.strip().split(",")
                    available_modules.append((module_id, module_name, credits))
        except FileNotFoundError: #file not found.
            print("The module file was not found.")
            return []
        return available_modules

#function to display available modules.
def display_available_modules():
    available_modules = {}
    try:
        with open('module.txt', 'r') as file: #opens and reads module.txt.
            for line in file:
                column = line.strip().split(',')
                if len(column) < 2:  
                    continue
                module_id = column[0]
                module_name = column[1]
                available_modules[module_id] = module_name
        return available_modules
    
    except FileNotFoundError: #file not found.
        print("\nModule file not found.")
        return {}

#function to manage student's enrollments.
def manage_enrollment():
    while True:
        student_ID = input("Enter student's ID: ").strip() # input student ID.
        if not len(student_ID) == 8: #validating the student ID.
            print("\nPlease input the correct student ID!")
            continue
        break

    available_programs = ["Computing", "Business"] #display available programs.
    print(f"\nAvailable programs: {', '.join(available_programs)}")
    
    with open(student_path, 'r') as file: #reads student.txt.
        for line in file:
            record = line.strip().split(',')
            if record[0] == student_ID: #ensuring the first index contains student ID.
                program = record[2]
                if program in available_programs:
                    available_modules = display_available_modules()  #display availlable modules if student's chosen program exist.
                    if not available_modules:  
                        print("\nNo available modules to display.")
                        return
                    
                    print("\nAvailable modules:")
                    print("=" * 16)
                    for module_id in available_modules: #looping through the dictionary.
                        module_name = available_modules[module_id] 
                        print(f"{module_id}: {module_name}")
                    
                    moduleID = input("Enter a module ID to enroll or unenroll: ").strip()   #input desired module ID.
                    if moduleID not in available_modules:
                        print("\nInvalid module, please choose from the available modules.")
                        return
                else:
                    print("\nPlease input a valid program and check spellings!")
                    continue
                break
        else:
            print("\nStudent ID doesn't exist.")
            return

    change = input("Type 'enroll' or 'unenroll': ").lower().strip() #to enroll or unenroll.

    if change not in ['enroll', 'unenroll']: #to make sure the choice is either enroll or unenroll.
        print("\nInvalid, please type 'enroll' or 'unenroll'!")
        return

    module = available_modules[moduleID] #declaring module chose with moduleID.

    try:
        updated_records = [] #listing the updated change on student's module(s).
        enrolled = False
        found = False

        with open(enrollment_path, 'r') as file: #read enrollment.txt to apply change made earlier.
            for line in file:
                record = line.strip().split(',')  
                if record[0] == student_ID:
                    found = True
                    if change == 'enroll' and module not in record[1:]: 
                        record.append(module)  #append the module into enrollment.txt.
                        print(f"\nSuccessfully enrolled in {module}!")
                    elif change == 'unenroll' and module in record: 
                        record.remove(module) #remove the module from enrollment.txt.
                        print(f"\nSuccessfully unenrolled from {module}!")
                    enrolled = True
                updated_records.append(",".join(record) + "\n")  

        if not enrolled and change == 'enroll': #enroll student into the module.
            updated_records.append(f"{student_ID},{module}\n")  
            print(f"\nCongratulations, student has enrolled in {module} for the first time.")
        
        elif not enrolled and change == 'unenroll': #unenroll student from the module.
            print(f"\nStudent is not enrolled in {module}.")
            return

        elif not found and change == 'unenroll': #student is not found.
            print(f"\nStudent ID not found, can't unenroll from {module}.")
            return

        with open(enrollment_path, 'w') as file: #write the change into the enrollment.txt.
            file.writelines(updated_records) 
        print("\nEnrollment updated successfully.")

    except FileNotFoundError: #file not found
        print("\nEnrollment file not found.")
    
    except KeyboardInterrupt: #handling interruption.
        print("\nCancelled, exiting...")

#function to issue student's transcripts.
def issue_transcript():
    while True:
        student_ID = input("Enter student ID: ").strip() #input student ID.
        if len(student_ID) != 8 and student_ID.startswith("TP"): #to check if it's valid.
            print("\nPlease input the correct student ID!")
            continue
        break 
    
    try:
        found = False
        name = ""  
        program = ""

        with open(student_path, 'r') as file: #read the student file to search for their records.
            for line in file:
                if line.startswith(student_ID): #searching for the matching student ID.
                    found = True
                    stud_information = line.strip().split(",")
                    name = stud_information[1].strip()
                    program = stud_information[2].strip()
                    break

        if not found:
            print("\nStudent ID not found for transcript generation.")
            return

        enrolled_modules = []
        with open(enrollment_path, 'r') as file: #read the enrollemnt file to search for their enrollments.
            for line in file:
                record = line.strip().split(",")
                if record[0] == student_ID: 
                    enrolled_modules.append(record[1].strip()) 

        if not enrolled_modules:
            print("\nNo enrolled modules found for the student.")
            return

        module_grades = []
        with open(student_grade_path, 'r') as file: #read the student grade file to search for the grades they scored for their modules.
            for line in file.readlines():
                grade_records = line.strip().split(",")
                if grade_records[0] == student_ID:  #to match the student ID.
                    module_name = grade_records[2].strip()
                    try:
                        grade = int(grade_records[4].strip())
                        if 0 <= grade <= 100:
                            module_grades.append((module_name, grade)) #append the grade information.
                        else:
                            module_grades.append((module_name, "N/A")) #if there's no grade available.
                    except ValueError:
                        module_grades.append((module_name, "N/A"))  

        transcript = [student_ID, name, program] #formatting the transcript.
        for module, grade in module_grades:
            if module in enrolled_modules:
                transcript.append([module, grade]) #adding module and grades to the formatting.

        print("\nTranscript generated successfully.")
        print(transcript)
        return transcript

    except FileNotFoundError: #file is not found.
        print("\nStudent file or transcript file not found.")
    except KeyboardInterrupt: #handling interruption.
        print("\nCancelled, exiting...")

#function to view student's information.
def view_student_information():
    while True:
        student_ID = input("Enter student ID: ").strip() #input the student ID.
        if len(student_ID) != 8 and student_ID.startswith("TP"): #to check if it's valid.
            print("\nPlease input the correct student ID!")
            continue
        break
    
    try:
        found = False
        with open(student_path, 'r') as file: #read the student file to search for the student's information.
            for line in file:
                if line.startswith(student_ID): 
                    print("Student Information: ", line.strip())
                    found = True
                    break
        if not found: #if student ID is not found in the file.
            print("\nStudent ID is not found.")

    except FileNotFoundError: #file is not found
        print("\nStudent file is not found.")
    except KeyboardInterrupt: #handling interruption.
        print("\nCancelled, exiting...")

#function to display registration menu.
def main():
    while True: 
        print("""
---------------------Registration Menu--------------------
1. Register New Student
2. Update Student Records
3. Manage Enrollments
4. Issue Transcript
5. View Student Information
6. Exit Menu
""")

        choice = input("Enter your choice (1-6): ") #inpu the choice 1-6 based on the menu.

        if choice == "1":
            register_new_student() #directing to the function to register new students.
        elif choice == "2":
            update_student_records()  #directing to the function to update student's records.
        elif choice == "3":
            manage_enrollment() #directing to the function to manage student's enrollment.
        elif choice == "4":
            issue_transcript() #directing to the function to issue student's transcript.
        elif choice == "5":
            view_student_information() #directing the function to vie3w student's information.
        elif choice == "6": 
            break #exit the menu.
        elif not choice not in "123456" and choice.isdigit: #ensuring the choice is valid.
            print("\nInvalid choice, please input your choice again (1-6).")

