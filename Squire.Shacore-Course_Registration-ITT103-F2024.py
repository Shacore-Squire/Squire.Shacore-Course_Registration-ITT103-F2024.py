class Course:

    #Creating a course using an ID, name and fee.
    def __init__(self, course_id, course_name, course_fee ):
        self.ID = course_id
        self.name = course_name
        self.fee = course_fee

#Student class to define student and the course they are enrolled in.
class Student:
    def __init__(self, student_name, student_id, student_email):
        self.name = student_name
        self.ID = student_id
        self.email = student_email
        self.list = []   # List to track courses student is enrolled in
        self.balance = 0

    #Method for enrolling students.
    def enroll (self,course):
        # Checking if student has already been enrolled.
        if course in self.list:
            print(f"Student {self.name} is already enrolled in {course.name}.")
        else:
            self.list.append(course) #Adiing the course to student's list.
            self.balance += course.fee #Adiing the course fee to student's balance.
            print(f"Student {self.name} has been enrolled in {course.name}.")

# The class RegistrationSystem if for managing courses and students.
class RegistrationSystem:
    def __init__(self):
        #Dictinaries  to store courses and students by their ID numbers.
        self.course = {}
        self.student = {}

    #Method to add a new course.
    def add_course (self, course_id, course_name, course_fee):
        #Checking if the course ID has already been taken.
        if course_id not in self.course:
            self.course [course_id] = Course (course_id, course_name, course_fee)
            print (f"Course with ID {course_name} has been added successfully.")
        else:
            print (f"Course with ID {course_id} already exist.")

    #Method to register a new student.
    def register_a_student (self, student_id, student_name,student_email):
        #Check if the student's ID has already been registered.
        if student_id not in self.student:
            self.student [student_id] = Student (student_id,student_name, student_email)
            print (f"Student with ID {student_id} has been registered successfully.")
        else:
            print (f"Student with ID {student_id} already registered.")

    #Method to enroll a student in a course.
    def enroll_in_course (self, student_id, course_id):
        # Check if the student is registered.
        if student_id not in self.student:
            print (f"Student with ID {student_id} not found.")
            return
        if course_id not in self.course:
            print (f"Course with ID {course_id} not found.")
            return
        students = self.student [student_id]
        course =  self.course [course_id]
        students.enroll (course)

    #Method to calculate the payment for students.
    def calculate_payment(self, student_id):
        if student_id not in self.student:
            print(f"Student with ID {student_id} not found.")
            return
        student = self.student[student_id]
        balance = student.balance
        if balance > 0:
            min_payment = 0.4 * balance  # 40% of the course fee
            print(f"Student {student.name} is required to pay {min_payment}.")
            payment = float(input("Enter payment amount: "))
            if payment >= min_payment:
                student.balance -= payment
                print(f"Payment was successful. Remaining balance: {student.balance}.")
            else:
                print(f"Payment insufficient. Minimum 40% is required.")
        else:
            print(f"Student {student.name} has no outstanding balance.")

    #Method to check student's balance.
    def check_student_balance (self, student_id):
        # Check if the student is registered.
        if student_id not in self.student:
            print (f"Student with ID {student_id} not found.")
            return
        student = self.student [student_id]
        print (f"The balance for {student.name} is {student.balance}.")

    #Method to show the list of available courses.
    def show_course_list(self):
        # Check if courses are available.
        if not self.course:
            print("No courses available at this time.")
        else:
            for course in self.course.values():  # Iterate through course instances, not course IDs.
                print(f"Name = {course.name}   ID = {course.ID}  Fee = ${course.fee} ")

    #Method to show all registered students.
    def show_registered_students(self):
        # Check if students are registered.
        if not self.student:
            print("No students have been registered.")
        for student in self.student.values():
            print(f"Student ID: {student.ID}, Name: {student.name}")

    #Method to show students in a specific course using the course ID number.
    def show_students_in_course(self, course_id):
        if course_id not in self.course:
            print(f"Course with ID {course_id} not found.")
        else:
            course = self.course[course_id]
            enrolled_students = [student for student in self.student.values() if course in student.list]
            if not enrolled_students:
                print(f"No students have been enrolled in this course {course.name}.")
            else:
                print(f"These are the students enrolled in {course.name}:")
                for student in enrolled_students:
                    print(f"{student.name}")

#The function to run registration system.
def main():
    system = RegistrationSystem()  # Create a new registration system

    # This is where we greet our user.
    print("Welcome to Course Registry.")

    #Loop to show menu and handle user input.
    while True:
        print("Menu, Course Registry ")
        print("1. Register a student.")
        print("2. Add a course.")
        print("3. Show courses.")
        print("4. Enroll students in courses.")
        print("5. Show registered students.")
        print("6. Show students in course.")
        print("7. Calculate Payment.")
        print("8. Check student's balance.")
        print("9. Exit")

        option = input("Please choose an option from the menu:")

        if option == "1":
            try:
                student_id = int(input("Enter Students ID number:"))
                student_name = input("Enter student's name: ")
                student_email = input("Enter student's email: ")
                system.register_a_student(student_id, student_name, student_email)
            except ValueError:
                print("Invalid ID input, please try again.")

        elif option == "2":
            try:
                course_id = int(input("Please enter Course ID number: "))
                course_name = input("Please enter name of course:")
                course_fee = float(input("Please enter cost of course: $"))
                system.add_course(course_id, course_name, course_fee)
            except ValueError:
                print("Invalid input, please try again.")

        elif option == "3":
            system.show_course_list()

        elif option == "4":
            try:
                student_id = int(input("Please enter student ID number:"))
                course_id = int(input("Please enter course ID number:"))
                system.enroll_in_course(student_id, course_id)
            except ValueError:
                print("Invalid input, please try again.")

        elif option == "5":
            system.show_registered_students()

        elif option == "6":
            try:
                course_id = int(input("Please enter course ID number:"))
                system.show_students_in_course(course_id)
            except ValueError:
                print("Invalid input, please try again.")

        elif option == "7":
            try:
                student_id = int(input("Please enter student's Id number:"))
                system.calculate_payment(student_id)
            except ValueError:
                print("Invalid input, please try again.")

        elif option == "8":
            try:
                student_id = int(input("Please enter student's Id number:"))
                system.check_student_balance(student_id)
            except ValueError:
                print("Invalid input, please try again.")

        elif option == "9":
            print("Exiting Course Registry. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid number from the menu.")
main()
#I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT.