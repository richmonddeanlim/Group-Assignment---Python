# Read Data From A File And Return It As Lists, If The File Doesn't Exist If Creates One And Returns It
def read(path):
    try:
        with open(path, 'r') as file:
            raw_data = file.readlines()
        return [line.strip().split(",") for line in raw_data]
    except FileNotFoundError:
        print(f"Error: {path} not found. Creating a new file...")
        with open(path, 'w') as file:
            pass
        return []


# File Paths
s_path = "database/student.txt"
l_path = "database/lecturer.txt"
m_path = "database/module.txt"

# Global Data Initialization
students = read(s_path)
modules = read(m_path)
lecturers = read(l_path)

# Updates All Files After Changes Have Been Made Such As Add/Delete So Files Any Synced
def update_files():
    global students, modules, lecturers, big
    students = read(s_path)
    modules = read(m_path)
    lecturers = read(l_path)

# Adds A New Module
def add_module():
    print("\n")
    print("=" * 70)
    print(f"{'Module Information':^70}")
    print("=" * 70)

    # Ensures Data Entered Meets The Correct Format
    while True:
        M_code = input("Please enter Module code (M followed by 3 digits): ").strip().upper()
        if len(M_code) != 4 or M_code[0] != 'M' or not M_code[1:].isdigit():
            print("Invalid Module Code. Code must be 'M' followed by 3 digits.")
        elif any(module[0] == M_code for module in modules):
            print("Module code already exists! Please enter a new code.")
        else:
            break

    # Ensures Data Entered Meets The Correct Format
    while True:
        M_name = input("Please enter Module Name: ").strip()
        if not M_name.replace(" ", "").isalpha():
            print("Invalid Name. The name should only contain letters.")
        else:
            break

    # Ensures Data Entered Meets The Correct Format
    while True:
        try:
            M_credits = int(input("Please enter number of Credit Hours (Enter a positive number): ").strip())
            if M_credits > 0:
                break
            else:
                print("Invalid Hours. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Adds The New Module To Main File And Module File
    with open(m_path, 'a') as m_a:
        m_a.write(f"{M_code},{M_name},{M_credits}\n")

    print("Module Added Successfully!")
    update_files()

# Adds A New Student
def add_student():
    print("\n")
    print("=" * 70)
    print(f"{'Student Information':^70}")
    print("=" * 70)

    # Ensures Data Entered Meets The Correct Format
    while True:
        S_ID = input("Please enter student ID (TP followed by 6 digits): ").strip().upper()
        if len(S_ID) != 8 or S_ID[:2] != "TP" or not S_ID[2:].isdigit():
            print("Invalid Student ID. Please enter a valid ID in the format 'TP######'.")
        elif any(student[0] == S_ID for student in students):
            print("Student ID already exists. Please enter a different ID.")
        else:
            break

    # Ensures Data Entered Meets The Correct Format
    while True:
        S_name = input("Please enter student name: ").strip()
        if not S_name.replace(" ", "").isalpha():
            print("Invalid Name. Please enter a valid name without numbers or special characters.")
        else:
            break

    # Ensures Data Entered Meets The Correct Format
    while True:
        Department = input("Please enter Department name: ").strip()
        if not Department.replace(" ", "").isalpha():
            print("Invalid Department Name. Please enter a valid department name.")
        else:
            break

    # Adds The New Student To Main File And Student File
    with open(s_path, 'a') as s_a:
        s_a.write(f"{S_ID},{S_name},{Department}\n")

    print("Student Added Successfully!")
    update_files()

# Removes An Entity
def remove_function(file_path, identifier, entity_type):
    removed = False
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            if identifier not in line:
                file.write(line)
            else:
                removed = True

    if removed:
        print(f"{entity_type} Removed Successfully!")
    else:
        print(f"{entity_type} ID not found.")

    update_files()

# Removes A Student
def remove_student():
    print("\n")
    print("=" * 85)
    print(f"{'Student Deletion Information':^85}")
    print("=" * 85)
    S_ID = input("Please enter student ID you want to remove (TP followed by 6 digits): ").strip().upper()
    remove_function(s_path, S_ID, "Student")

# Adds A Lecturer
def add_lecturer():
    print("\n")
    print("=" * 70)
    print(f"{'Lecturer Information':^70}")
    print("=" * 70)

    # Ensures Data Entered Meets The Correct Format
    while True:
        L_ID = input("Please enter lecturer ID (L followed by 2 digits): ").strip().upper()
        if len(L_ID) != 3 or L_ID[0] != "L" or not L_ID[1:].isdigit():
            print("Invalid Lecturer ID. Please enter a valid ID in the format 'L##'.")
        elif any(lecturer[0] == L_ID for lecturer in lecturers):
            print("Lecturer ID already exists. Please enter a different ID.")
        else:
            break

    # Ensures Data Entered Meets The Correct Format
    while True:
        L_name = input("Please enter lecturer name: ").strip()
        if not L_name.replace(" ", "").isalpha():
            print("Invalid Name. Please enter a valid name without numbers or special characters.")
        else:
            break

    # Ensures Data Entered Meets The Correct Format
    module_list = []
    while True:
        module = input("Please enter Module name: ").strip()                             
        if module.replace(" ", "").isalpha() and module in registered_module:
            module_list.append(module)
            choice = input("Input 0 to stop (enter to continue): ")
            if choice == "0":
                break
            else:
                continue
        else:
            print("Invalid Module Name. Please enter a valid module name.")

    data = []
    
    # inserting all data into list
    for item in [L_ID,L_name]:
        data.append(item)

    for module in module_list:
        data.append(module)
    i = 1
    lenoflist = len(data) 
    while i < lenoflist:
        data.insert(i,",")
        lenoflist += 1
        i += 2

    data.append("\n")

    # Adds The New Lecturer To Main File And Lecturer File
    with open(l_path, 'a') as l_a:
        l_a.writelines(data)

    print("Lecturer Added Successfully!")
    update_files()

# Removes A Lecturer
def remove_lecturer():
    print("=" * 85)
    print(f"{'Lecturer Deletion Information':^85}")
    print("=" * 85)
    L_ID = input("Please enter Lecturer ID you want to remove (L followed by 2 digits): ").strip().upper()
    remove_function(l_path, L_ID, "Lecturer")

# Updates Lecturer Information
def update_lecturer():
    print("=" * 85)
    print(f"{'Update Lecturer Information':^85}")
    print("=" * 85)

    L_ID = input("Please enter the Lecturer ID you want to update (L followed by 2 digits): ").strip().upper()

    found = False
    with open(l_path, 'r') as l_r:
        lines = l_r.readlines()
    with open(l_path, 'w') as l_w:
        for line in lines:
            if L_ID == line.split(",")[0]:
                found = True
                # Asks For New Information
                new_name = input("New Name: ").strip()
                new_module = input("New Department: ").strip()
                l_w.write(f"{L_ID},{new_name},{new_module}\n")
            else:
                l_w.write(line)

    if found:
        print("Lecturer information updated successfully!")
    else:
        print("Lecturer ID not found.")
    update_files()

# Generates A Report On Students, Lecturers and Modules
def generate_report():
    print("\n")
    print("=" * 50)
    print(f"{'Report Summary':^50}")
    print("=" * 50)

    print(f"Total number of students: {len(students)}")
    print(f"Total number of active courses: {len(modules)}")
    print(f"Total number of faculty: {len(lecturers)}")

# Displays All Date For Students, Lecturers and Modules
def view_all_data():
    print("\n")
    print("=" * 60)
    print(f"{'All Data':^60}")
    print("=" * 60)

    print("Students:")
    for student in students:
        print(f"- {student[0]}: {student[1]} ({student[2]})")

    print("\nCourses:")
    for course in modules:
        print(f"- {course[0]}: {course[1]} ({course[2]} credits)")

    print("\nLecturers:")
    for lecturer in lecturers:
        print(f"- {lecturer[0]}: {lecturer[1]}")

# Menu, Allows User To Choose
def main():
    while True:
        print("=" * 32)
        print(f"{'Administrator Menu':^32}")
        print("=" * 32)
        print("1 - Add New Module")
        print("2 - Add New Student")
        print("3 - Remove Student")
        print("4 - Add Lecturer")
        print("5 - Remove Lecturer")
        print("6 - Update Lecturer")
        print("7 - Generate Report")
        print("8 - View All Data")
        print("9 - Exit")
        print("=" * 32)

        try:
            option = int(input("Please enter a number: ").strip())
        except ValueError:
            print("Invalid input. Please enter wa number.")
            continue

        if option == 1:
            add_module()
        elif option == 2:
            add_student()
        elif option == 3:
            remove_student()
        elif option == 4:
            add_lecturer()
        elif option == 5:
            remove_lecturer()
        elif option == 6:
            update_lecturer()
        elif option == 7:
            generate_report()
        elif option == 8:
            view_all_data()
        elif option == 9:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 9.")