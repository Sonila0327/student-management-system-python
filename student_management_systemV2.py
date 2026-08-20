students = {} 

# Calculating grades based on average
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"

# Calculate comment based on grade
def calculate_comment(grade):
    if grade == "A":
        return "Excellent"
    elif grade == "B":
        return "Very Good"
    elif grade == "C":
        return "Good"
    elif grade == "D":
        return "Average"
    elif grade == "E":
        return "Needs Improvement"
    else: 
        return "Needs more effort. Don't give up!"

# Getting marks function
def get_marks(subject):
    while True:

        marks = int(input(f"Enter {subject} Marks: "))

        if marks >= 0 and marks <=100:
            return marks

        print("Marks must be between 0 to 100")

while True:
    print("==== Main Manu ====")
    print("1. Add Student")  
    print("2. View Students")                
    print("3. Search Student")                
    print("4. Update Student")                
    print("5. Delete Student")                
    print("6. Class Statistics")                
    print("7. Exit")    

    # Taking user's choice
    choice = int(input("Enter Your choice: "))
    # 1. Add Student
    if choice == 1:  
        roll_no = int(input("Enter Roll No: ")) 
        if roll_no in students: # If student already exist prevent dupliacte entries
            print("The entered Roll No. already exists.") 
            continue    # skip current iteration       

        name = input("Enter student name: ")

        # Get marks of subjects 
        english  = get_marks("English")
        math     = get_marks("Math")
        computer = get_marks("Computer")
        physics  = get_marks("Physics")

        # Marks Dic
        marks = {
            "English" : english,
            "Math"    : math,
            "Computer": computer,
            "Physics" : physics
        }

        # Calculate Average
        average = (english + math + computer + physics) / 4

        # Grade 
        grade = calculate_grade(average)
        #comment
        comment = calculate_comment(grade)

        # Adding record in Students dic
        students[roll_no] = {
            "Name"    : name,
            "Marks"   : marks,
            "Average" : round(average, 2),
            "Grade"   : grade,
            "Comment" : comment
        }
    # View Students
    elif choice == 2:
        if len(students) == 0:
            print("No students available.")
            continue

        for roll_no in students: # If student exist in Students dic
            student = students[roll_no]
            print("--------------------------------")
            print("Roll No:", roll_no)
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])
            print("Average:", student["Average"])
            print("Grade:", student["Grade"])
            print("Comment:", student["Comment"])
            print("--------------------------------")
    # 3. Search Student

    elif choice == 3:
        search_roll = int(input("Enter Roll No: "))
        if search_roll in students:
            student = students[search_roll]
            print("--------------------------------")
            print("Roll NO: ", search_roll)
            print("Name: ",    student["Name"])
            print("Marks: ",   student["Marks"])
            print("Average: ", student["Average"])
            print("Grade: ",   student["Grade"])
            print("Comment: ", student["Comment"])
            print("--------------------------------")

        else:
            print("Entered Roll No does not exist")
    # 4. Udate student
    elif choice == 4:
        roll_no = int(input("Enter Roll No: "))
        if roll_no in students:
            student = students[roll_no]

            # Taking updated Marks
            english = get_marks("English")
            math = get_marks("Math")
            computer = get_marks("Computer")        
            physics = get_marks("Physics")

            # update Marks
            student["Marks"]["English"] = english
            student["Marks"]["Math"] = math
            student["Marks"]["Computer"] = computer
            student["Marks"]["Physics"] = physics

            # Calculate Updated Average 
            average = (english + math + computer + physics)/ 4

            # Calculate Grades and Comments
            grade = calculate_grade(average)
            comment = calculate_comment(grade)
            
            student["Average"] = round(average, 2)
            student["Grade"] = grade
            student["Comment"] = comment
        else:
            print("Entered Roll NO does not exist")

    # 5. Delete Student
    elif choice == 5:
        roll_no = int(input("Enter Roll No: "))
        if roll_no in students:
            students.pop(roll_no)
            print("Student successfully deleted.")
        else:
            print("Entered Roll No does not exist")

    # 6. Class Statistics 
    elif choice == 6:
        total_students = len(students)
        print("Total Students: ", total_students)

        if total_students == 0:
            print("No student available")
            continue

        total_average = 0
        for roll_no in students:
            student = students[roll_no]

            total_average += student["Average"]

        class_average = total_average / total_students
        print("Class Average: ", round(class_average, 2))

        # Find Maximum

        highest_average = 0
        highest_student = ""

        for roll_no in students:
            student = students[roll_no]

            if student["Average"] > highest_average:
                highest_average = student["Average"]
                highest_student = student["Name"]

        print("Highest student: ", highest_student)
        print("Highest Average: ", highest_average)


    # Find Minimum

        lowest_average = 100
        lowest_student = ""

        for roll_no in students:
            student = students[roll_no]

            if student["Average"] < lowest_average:
                lowest_average = student["Average"]
                lowest_student = student["Name"]

        print("Lowhest student: ", lowest_student)
        print("Lowest Average: ", lowest_average)

    # 7. Exit(End)
    elif choice == 7:
        print("Exit")
        break
    # if entered wrong choice
    else:
        print("Invalid choice")




