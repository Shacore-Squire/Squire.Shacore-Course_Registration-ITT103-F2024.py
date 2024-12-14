Author:  Shacore Squire 

Date created: December 12, 2024

Course: ITT103

Github public URL to code: 


Modifications Made:
Fixing show_course_list() method:
1.Issue: The original code iterated through the course IDs (which are integers), and tried to access attributes like .name, .ID, and .fee on them, which resulted in an AttributeError because integers do not have these attributes.
2.Fix: The program now correctly iterates over the values() of the self.course dictionary, which contains instances of the Course class. Each Course object has the name, ID, and fee attributes, so we can access these correctly.
Updated Method Code:
python
Copy code
def show_course_list(self):
    # Check if courses are available.
    if not self.course:
        print("No courses available at this time.")
    else:
        for course in self.course.values():  # Iterate through course instances, not course IDs.
            print(f"Name = {course.name}   ID = {course.ID}  Fee = ${course.fee} ")
Explanation:
1.The self.course dictionary stores courses using course IDs as keys and Course objects as values.
2.self.course.values() returns the list of Course objects. Each Course object contains the attributes name, ID, and fee, which are now accessed correctly.
2.
General Program Overview:
1.The program is designed as a course registration system, allowing you to register students, add courses, enroll students in courses, track payments, and view balances. Below is a high-level overview of the classes and their functionality.
Program Classes and Their Responsibilities:
1.Class Course:
Purpose: Represents a course with attributes like course_id, course_name, and course_fee.

Attributes:
I.ID: Unique identifier for the course.
II.name: Name of the course.
III.fee: Fee for the course.
Constructor:
I.Initializes a new course object with the provided course_id, course_name, and course_fee.

2.Class Student:
Purpose: Represents a student who can enroll in courses and manage their balance.

Attributes:

i.name: Name of the student.
ii.ID: Unique identifier for the student.
iii.email: Email address of the student.
iv.list: List of courses the student is enrolled in.
v.balance: The total amount of money the student owes for their enrolled courses.
Methods:
i.Enroll(course): Enrolls the student in the given course. If the student is already enrolled, it notifies the user.

3.Class RegistrationSystem:
Purpose: Manages the registration system, including adding courses, registering students, enrolling students, and managing payments.
Attributes:
i.course: A dictionary mapping course IDs to Course objects.
ii.student: A dictionary mapping student IDs to Student objects.
Methods:
i.add_course(course_id, course_name, course_fee): Adds a new course to the system.
ii.register_a_student(student_id, student_name, student_email): Registers a new student in the system.
iii.enroll_in_course(student_id, course_id): Enrolls a student in a course.
iv.calculate_payment(student_id): Calculates and processes the payment for a student based on the total balance.
v.check_student_balance(student_id): Displays the student's current balance.
vi.show_course_list(): Displays a list of all available courses.
vii.show_registered_students(): Displays a list of all registered students.
viii.show_students_in_course(course_id): Displays a list of all students enrolled in a specific course.
1.
Main Program (main() function):
2.
1.Purpose: Provides a user interface through a text-based menu to interact with the system.
2.Flow:
1.Displays a menu of available options (register a student, add a course, enroll in courses, etc.).
2.Takes user input for the selected action and calls the corresponding method from the RegistrationSystem class.
3.Continues until the user chooses to exit.
Key Changes & Fixes:
Fixed Iteration in show_course_list Method:
oBefore: The program was iterating over the course IDs in the self.course dictionary and incorrectly trying to access attributes like .name and .fee on course IDs (integers).
oAfter: The program now correctly iterates over the values() of the self.course dictionary, which gives access to the Course objects. It then correctly accesses and prints the name, ID, and fee attributes of each Course.
Example Output:
After the modification, when a user selects option "3" to show courses, the system will correctly display the course list:
Name = Python Programming   ID = 101  Fee = $200 Name = Data Structures      ID = 102  Fee = $300 
Final Remarks:
This system is now capable of registering students, adding courses, enrolling students, calculating payments, and more.
The show_course_list method should now correctly display the courses without errors.
