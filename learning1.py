def grade_calculator(name,maths,science,english):
    student = {
        "name": name,
        "science" : science,
        "maths" : maths,
        "english": english
        }
    total_marks = student["maths"] + student["science"] + student["english"]
    total_percentage = (total_marks/300)*100
    if total_percentage >= 90:
       grade = "A+"
    elif total_percentage >= 80:
       grade = "A"
    elif total_percentage >= 70:
       grade = "B"
    elif total_percentage >= 60:
       grade = "C"
    else:
       grade = "failed"

    print(f"my name is {student['name']}")
    print(f"Total_marks:,{total_marks}")
    print(f"total_percentage",{total_percentage})

       
grade_calculator("sakshyam shrestha", 90, 92, 96)
