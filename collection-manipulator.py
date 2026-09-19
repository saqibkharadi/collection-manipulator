# PR 3 - Collection Manipulation
# Student Data Organizer

students = []   # list of all student records


def find_student(sid):
    for s in students:
        if s["info"][0] == sid:
            return s
    return None


def add_student():
    print()
    print("Enter student details:")
    sid = input("Student ID: ")

    # check if id is already used
    if find_student(sid) != None:
        print("This Student ID already exists!")
        return

    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    sub_text = input("Subjects (comma-separated): ")

    # id and dob in a tuple
    info = (sid, dob)

    # subjects in a set
    subjects = set()
    for sub in sub_text.split(","):
        sub = sub.strip()
        if sub != "":
            subjects.add(sub)

    student = {
        "info": info,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }
    students.append(student)

    print()
    print("Student added successfully!")


def display_students():
    print()
    print("--- Display All Students ---")

    if len(students) == 0:
        print("No students found.")
    else:
        for s in students:
            subs = ", ".join(sorted(s["subjects"]))
            print("Student ID:", s["info"][0], "| Name:", s["name"],
                  "| Age:", s["age"], "| Grade:", s["grade"],
                  "| Subjects:", subs)


def update_student():
    print()
    sid = input("Enter Student ID to update: ")
    s = find_student(sid)

    if s == None:
        print("Student not found!")
        return

    print("1. Update Age")
    print("2. Update Subjects")
    ch = input("Enter your choice: ")

    if ch == "1":
        s["age"] = int(input("Enter new age: "))
        print("Age updated successfully!")
    elif ch == "2":
        sub_text = input("Enter new subjects (comma-separated): ")
        new_subjects = set()
        for sub in sub_text.split(","):
            sub = sub.strip()
            if sub != "":
                new_subjects.add(sub)
        s["subjects"] = new_subjects
        print("Subjects updated successfully!")
    else:
        print("Invalid choice!")


def delete_student():
    print()
    sid = input("Enter Student ID to delete: ")

    for i in range(len(students)):
        if students[i]["info"][0] == sid:
            del students[i]
            print("Student deleted successfully!")
            return

    print("Student not found!")


def display_subjects():
    print()
    print("--- Subjects Offered ---")

    all_subjects = set()
    for s in students:
        for sub in s["subjects"]:
            all_subjects.add(sub)

    if len(all_subjects) == 0:
        print("No subjects yet.")
    else:
        for sub in sorted(all_subjects):
            print("-", sub)


# main program starts here
print("Welcome to the Student Data Organizer!")
print("You can add, display, update and delete students,")
print("and also see all the subjects offered.")

while True:
    print()
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_subjects()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
