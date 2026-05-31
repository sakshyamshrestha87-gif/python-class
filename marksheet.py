import csv
import os

file_name = "marksheet.csv"

def load_data():
    students = []
    if not os.path.exists(file_name):
    
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["rollno", "name", "maths", "science", "english"])
        return students
    try:

        with open(file_name, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row:
                    student = {
                        "rollno": row["rollno"],
                        "name": row["name"],
                        "maths": int(row["maths"]),
                        "science": int(row["science"]),
                        "english": int(row["english"])
                    }
                    students.append(student)
    except:
        print("Error loading")
    return students
def save_data(students):
    f = open(file_name, mode="w")
    f.write("rollno,name,maths,science,english\n")
    for student in students:
        
          line = (
            student["rollno"] + "," +
            student["name"] + "," +
            student["maths"] + "," +
            student["science"] + "," +
            student["english"] + "\n"
        )
          f.write(line)
    f.close()
    print("data saved")
        
def add_student(students):
    print("\n--add_student--")
    rollno = input("enter rollno: ")
    name= input("enter name: ")
    maths = input("enter maths marks: ")
    science = input("enter science mark:")
    english= input("enter english mark: ")

    student = {
    "rollno": rollno,
    "name": name,
    "maths": maths,
    "science": science,
    "english": english

}
    students.append(student)
    save_data(students)
    print("succeful add")

def view_students(students):

    print("\n--- Student List ---")

    for student in students:

        print("Roll No:", student["rollno"])
        print("Name:", student["name"])
        print("Maths:", student["maths"])
        print("Science:", student["science"])
        print("English:", student["english"])

        print("viewed")

def edit_student(students):

    rollno = input("enter rollno to edit: ")

    for student in students:

        if student["rollno"] == rollno:

            student["name"] = input("new name: ")
            save_data(students)
            print("Student edit")

def delete_student(students):

    rollno = input("Enter rollno to delete: ")

    for student in students:

        if student["rollno"] == rollno:

            students.remove(student)
            save_data(students)
            print("Student deleted")
students = load_data()
while True:
    print("--marsksheet---")
    print("1. add student")
    print("2. view students")
   
    print("3. edit student")
    print("4. delete student")
    print("5. save and exit")
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        save_data(students)
        print("save data")
        break
    elif choice == "4":
         edit_student(students)

    elif choice == "5":
      delete_student(students)
      
    
    else:
         print("wrong choice")