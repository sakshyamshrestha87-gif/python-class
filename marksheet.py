import csv
import math
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
                    "role no"  : data[0],
                    "name" : data[1],
                    "maths" : data[2],
                    "science" : data[3],
                    "english" : data[4]


                }

                students.append(student)
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
    print("Data Saved Successfully!")
        
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

student = load_data(
)
while True:
    print("--marsksheet---")
    print("add student")
    print("view students")
    print("save and exit")
    choice = input("Choose (1-3): ")
    
    if choice == "1":
        add_student(student)
    elif choice == "2":
        view_students(student)
    elif choice == "3":
        save_data(student)
        print("Goodbye! See you later.")
        break
    else:
        print("Wrong choice! Please choose 1, 2 or 3.")