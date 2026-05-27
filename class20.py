student = {
    "name": "sakshyam",
    "roll-no": 18,
    "address": "ktm",
    "age": 16,
    "contact": {
        "email": "ram.123@gmail.com",
        "phone_number": [1234567890, 9087654321]
    },
    "subject": {
        "maths": 20,
        "science": 50,
        "computer": 60
    }
}

try:

    name = student["name"]
    if not isinstance(name, str) or not name.isalpha():
        raise ValueError("Invalid name")

    roll = student["roll-no"]
    if not isinstance(roll, int) or roll <= 0:
        raise ValueError("Invalid roll number")

    phones = student["contact"]["phone_number"]
    for phone in phones:
        if not isinstance(phone, int) or len(str(phone)) != 10:
            raise ValueError("Invalid phone number")

    subjects = student["subject"]
    total_marks = 0

    for subject, marks in subjects.items():
        if not isinstance(marks, int) or marks < 0 or marks > 100:
            raise ValueError(f"Invalid marks in {subject}")
        total_marks += marks

    print("Name:", name)
    print("Roll No:", roll)
    print("Phone:", phones)
    print("Total Marks:", total_marks)

except KeyError as e:
    print("Missing key:", e)

except ValueError as e:
    print("Validation error:", e)

except Exception as e:
    print("Unexpected error:", e)