students = {}

while True:
    # Print Menu
    print("==== Student Management System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    # User Choice
    choice = int(input("Enter Your Choice: "))
    # Add Student
    if choice == 1:
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")

        # Subject Marks
        english = int(input("Enter English Marks: "))
        math = int(input("Enter Math Marks: "))
        computer = int(input("Enter Computer Marks: "))
        physics = int(input("Enter Physics Marks: "))


        marks = {
            "English" : english,
            "Math"    : math,
            "Computer": computer,
            "Physics" : physics
            }


        # Calculate Average
        average = (english + math + computer + physics) / 4

        # Assign Grade
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        elif average >= 50:
            grade = "E" 
        else: 
             grade = "F"


        # Giving Comments Based on Grades
        if grade == "A":
            comment = "Excellent"
        elif grade == "B":
             comment = "Very Good"
        elif grade == "C":
             comment = "Good"
        elif grade == "D":
              comment = "Average"
        elif grade == "E":
             comment = "Needs Improvement"
        else:
             comment = "Needs more effort. Don't give up!"


        #Add Student Record
        students[roll_no] = {
            "Name"   : name,
            "Marks"  : marks,
            "Average": round(average, 2),
            "Grade"  : grade,
            "Comment": comment
            }
    # View All Students
    elif choice == 2: 
        for roll_no in students:
            print("--------------------------------")
            student = students[roll_no]
            print("Roll_no", roll_no)
            print("Name:",student["Name"])
            print("Marks:",student["Marks"])
            print("Average:",student["Average"])
            print("Grade:",student["Grade"])
            print("Comment:",student["Comment"])
            print("--------------------------------")
    # Search Student
    elif choice == 3: 
        search_roll = int(input("Enter Roll Number: "))
        if search_roll in students:
            student = students[search_roll]
            print("--------------------------------")
            print("Roll No:", search_roll)
            print("Name:",student["Name"])
            print("Marks:",student["Marks"])
            print("Average:",student["Average"])
            print("Grade:",student["Grade"])
            print("Comment:",student["Comment"])
            print("--------------------------------")
        else: 
            print("Roll Number does not exist.")
    # Exist or end 
    elif choice == 4:
        break 
    # If Enter Wrong Choice 
    else: 
        print("Invalid choice.")
            
