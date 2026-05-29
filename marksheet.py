import csv
import os

file_name = "marksheet.csv"

def load_data():
    students = []
    try:
        file = open(file_name,mode='r', newline = '')
        lines = file.readlines()
        file.close()

        for line in lines[1:]:
            if line.strip() != "":
                data = line.strip().split(",")
                student = {
                    "rollno"  : data[0],
                    "name" : data[1],
                    "maths" : data[2],
                    "science" : data[3],
                    "english" : data[4]


                }

                students.append(students)
                return students
    except FileNotFoundError as e:
        print("file is not found")
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
    print("student add")


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

            print("Student edit")

def delete_student(students):

    rollno = input("Enter rollno to delete: ")

    for student in students:

        if student["rollno"] == rollno:

            students.remove(student)

            print("Student deleted")
student = load_data(
)
while True:
    print("--marsksheet---")
    print("1. add student")
    print("2. view students")
    print("3. save and exit")
    print("4. edit student")
    print("5. delete student")
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        add_student(student)
    elif choice == "2":
        view_students(student)
    elif choice == "3":
        save_data(student)
        print("save data")
        break
    elif choice == "4":
         edit_student(student)

    elif choice == "5":
      delete_student(student)
      
    
    else:
         print("wrong choice")