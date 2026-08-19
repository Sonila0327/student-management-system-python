# Student Management System (Python)

A console-based Student Management System developed in Python. This project started as a basic student record system and was improved in Version 2 by adding functions, validation, CRUD operations, and class performance statistics.

## Version 2 Features

* Add a new student record
* View all student records
* Search for a student by Roll Number
* Update student marks
* Delete student records
* Prevent duplicate Roll Numbers
* Validate marks between 0 and 100
* Calculate average marks automatically
* Assign grades based on average marks
* Generate performance comments
* Display class statistics
* Calculate class average
* Find the highest-performing student
* Find the lowest-performing student
* Menu-driven interface
* Exit option

## Technologies Used

* Python 3

## Concepts Practiced

* Variables
* User Input
* Type Conversion
* Conditional Statements (`if`, `elif`, `else`)
* `while` Loop
* `for` Loop
* Functions
* Dictionaries
* Nested Dictionaries
* Dictionary Membership (`in`)
* Dictionary Methods (`pop`)
* Data Validation
* CRUD Operations
* Data Organization
* Menu-Driven Programming
* Basic Statistics
* Problem-Solving

## Project Structure

```text
student-management-system-python/
│
├── student_management_system.py
└── README.md
```

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/student-management-system-python.git
```

2. Navigate to the project folder.

```bash
cd student-management-system-python
```

3. Run the program.

```bash
python student_management_system.py
```

## Main Menu

```text
==== Main Menu ====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Class Statistics
7. Exit
```

## Student Record Structure

Each student is stored using a nested dictionary:

```python
students[roll_no] = {
    "Name": name,
    "Marks": {
        "English": english,
        "Math": math,
        "Computer": computer,
        "Physics": physics
    },
    "Average": average,
    "Grade": grade,
    "Comment": comment
}
```

## Version Progression

### Version 1

The first version focused on Python fundamentals and basic student record management.

V1 included:

* Add student
* View students
* Search student
* Calculate average
* Assign grades
* Generate comments
* Menu-driven programming
* Nested dictionaries

### Version 2

Version 2 expanded the project into a more complete Student Management System.

New improvements include:

* Functions for grade and comment calculation
* Marks validation from 0–100
* Duplicate Roll Number prevention
* Update Student
* Delete Student
* Class Statistics
* Class average calculation
* Highest student calculation
* Lowest student calculation
* Better data management using nested dictionaries

## Learning Outcome

This project helped strengthen my understanding of Python by applying concepts in a practical console application.

Through this project, I practiced:

* Python fundamentals
* Functions
* Nested dictionaries
* Loops
* Conditional logic
* Data validation
* CRUD operations
* Data management
* Problem-solving
* Console application development

## Future Improvements

* Save student data to a file
* Load student data from a file
* Add more subjects
* Improve input error handling
* Add student ranking
* Add percentage calculation
* Create a graphical user interface (GUI)
* Connect the application to a database

## Author

**Sonila Shoukat**
