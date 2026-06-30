students = [
    {"name": "Lakshit", "marks": 95},
    {"name": "Rahul", "marks": 80},
    {"name": "Aman", "marks": 90}
]
while True:
    print("-" * 5, "Student Management", "-" * 5, "\n1. View Students\n2. Add Student\n3. Search Student\n4. Update marks\n5. Delete Student\n6 .Find Topper\n7. Find Average\n8. Exit")
    user = input("What You Want To Do? =")
    if user == "1":
        for student in students:
            print("Name :", student["name"], " "*5, "Marks :", student["marks"])
    elif user == "8":
        print("Program Closed")
        break
    elif user == "2":
        name = input("Enter Name:").title()
        if not name.strip():
            print("Invalid Name")
            continue
        marks = int(input("Enter Marks:"))
        if marks <= 0:
            print("Invalid Marks")
        else:
            students.append({"name": name, "marks": marks})
            print("Student Added Successfully")
    elif user == "3":
        name = input("Enter Name:").title()
        if not name.strip():
            print("Invalid Name")
            continue
        found = False
        for student in students:
            if name == student["name"]:
                print("Name :", student["name"])
                print("Marks :", student["marks"])
                found = True
                break
        if not found:
            print("Student Not Found")
    elif user == "4":
        name = input("Enter Name:").title()
        if not name.strip():
            print("Invalid Name")
            continue
        found = False
        for student in students:
            if name == student["name"]:
                found = True
                marks = int(input("Enter New Mark:"))
                if marks <= 0:
                    print("Invalid Marks")
                    break
                else:
                    student["marks"] = marks        
                    print("Marks Updated Successfully")
                    break
        if not found:
            print("Student Not Found")
    elif user == "5":
        name = input("Enter Name:").title()
        if not name.strip():
            print("Invalid Name")
            continue
        found = False
        for student in students:
            if name == student["name"]:
                students.remove(student)
                print("Student Removed Successfully")
                found = True
                break
        if not found:
            print("Student Not Found")
    elif user == "6":
        top_marks = 0
        topper = ""
        for student in students:
            if student["marks"]>top_marks:
                top_marks = student["marks"]
                topper = student["name"]
        print("Topper = ", topper)
        print("Marks = ", top_marks)
    elif user == "7":
        total = 0
        for student in students:
            total+=student["marks"]
        average = total/len(students)
        print("Average = ", round(average,2))
    else:
        print("Invalid Command")
            
