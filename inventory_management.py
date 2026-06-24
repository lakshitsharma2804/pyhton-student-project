students = []
while True:
    user = input("\nMENU: add/view/search/delete/update_marks/average/topper/exit = ").lower()
    if user == "add":
        name = input("what is your name = ")
        marks = int(input("what is your marks = "))
        students.append([name, marks])
        print("student added successfully")
    
    elif user == "view":
        for name, marks in students:
            print("name = ", name)
            print("marks = ", marks)
            print()
        if len(students) == 0:
            print("no students were addded")

    elif user == "search":
        enter = input("enter student name = ")
        found = False
        for name, marks in students:
            if name.lower() == enter.lower():
                print("name = ", name)
                print("marks = ", marks)
                found = True
                break
        if not found:
            print("student not found")
        
    elif user == "delete":
        delete = input("which name you want to delete = ")
        found = False
        for student in students:
            if student[0].lower() == delete.lower():
                students.remove(student)
                found = True
                print(delete, "successfully removed from the list")
        if not found:
            print(delete, "is not in list")



    elif user == "average":
        if len(students) == 0:
            print("no student were added")
        else:
            count = 0
            for name, marks in students:
                count += marks
            avg = count/len(students)
            print(avg)
                
    elif user == "topper":
      if len(students) == 0:
          print("no students were added")
      else:
        topper_name = students[0][0]
        max_marks = students[0][1]
        for name, marks in students:
            if marks>max_marks:
                max_marks = marks
                topper_name = name
        print("name = ", topper_name)
        print("marks = ", max_marks)
    
    elif user == "exit":
        print("thankyou \nprogram closed!")
        break

    else:
        print("invalid command")