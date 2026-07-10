students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Lakshit", "marks": 95},
    {"name": "Aman", "marks": 45},
    {"name": "Rohit", "marks": 72},
    {"name": "Karan", "marks": 30}
]

def show_all_students():
    for student in students:
        print(student["name"], ":", student["marks"])

def show_passed_students():
    for student in students:
        if student["marks"]>=50:
            print(student["name"], ":", student["marks"])

def show_failed_students():
    for student in students:
        if student["marks"]<50:
            print(student["name"], ":", student["marks"])

def show_topper():
    topper = students[0]
    for student in students:
        if student["marks"]>topper["marks"]:
            topper = student
    print(topper["name"], ":", topper["marks"])

def sort_by_marks():
    sorted_students = sorted(students, key=lambda x:x["marks"] )
    for student in sorted_students:
        print(student["name"], ":", student["marks"])

def search_student():
    name = input("Enter Name:").title()
    found = False
    for student in students:
        if name == student["name"]:
            print(student["name"], ":", student["marks"])
            found = True
            break
    if not found:
        print("student not found")
def add_student():
    name = input("enter name:").title()
    marks = int(input("enter marks:"))
    students.append({"name":name, "marks":marks})
    print("Student Added Successfully")
def delete_student():
    name = input("enter name of student which you want to remove:").title()
    for i, student in enumerate(students):
        if student["name"] == name:
            removed_student = students.pop(i)
            print("Student Removed Successfully")
            break
    else:
        print("Student Not Found")
def update_marks():
    name = input("enter name of student:").title()
    for student in students:
        if student["name"] == name:
            new_marks = int(input("enter new marks:"))
            student["marks"] = new_marks
            print("Marks Updated Successfully")
            break
    else:
        print("Student Not Found")
def average_marks():
    total = 0
    for student in students:
        total += student["marks"]
    average = total/len(students)     
    print("Average Of Marks = ", average)
def highest_lowest_marks():
    topper = students[0]
    lower = students[0]
    for student in students:
        if student["marks"]>topper["marks"]:
            topper = student
        if student["marks"]<lower["marks"]:
            lower = student
    print("Topper = ", topper["name"], "-", topper["marks"])
    print("Lower = ", lower["name"], "-", lower["marks"])      
def menu():
    while True:
        print("="*5, "STUDENT RESULT ANALYZER", "="*5)
        print("1. Show All Student")
        print("2. Show Passed Student")
        print("3. Show Failed Student")
        print("4. Show Topper")
        print("5. Sort By Marks")
        print("6. Search Student")
        print("7. Add Student")
        print("8. Delete Student")
        print("9. Update Marks")
        print("10. Show Average Marks")
        print("11. Show Highest & Lowest Marks")
        print("12. Exit")
        user = input("What You Want To Do ? =")
        if user == "1":
            show_all_students()
        elif user == "2":
            show_passed_students()
        elif user == "3":
            show_failed_students()
        elif user == "4":
            show_topper()
        elif user == "5":
            sort_by_marks()
        elif user == "6":
            search_student()
        elif user == "7":
            add_student()
        elif user == "8":
            delete_student()
        elif user == "9":
            update_marks()
        elif user == "10":
            average_marks()
        elif user == "11":
            highest_lowest_marks()
        elif user == "12":
            print("Thank You")
            break
        else:
            print("Invalid Command")
menu()