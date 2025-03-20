class Student:
    def __init__(self, student_name: str, student_id: str):
        self.student_name = student_name
        self.student_id = student_id
        self.courses = []  # List of tuples (course_name, grade)

    def enroll_course(self, course_name: str, grade: str):
        self.courses.append((course_name, grade))

    def display_details(self):
        print("\n")
        print(f"Student Name: {self.student_name}")
        print("\n")
        print(f"Student ID: {self.student_id}")
        print("\n")
        print("Enrolled Courses:")
        for course, grade in self.courses:
            print("\n")
            print(f"  - {course}: {grade}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []  # List of Student objects

    def add_student(self, student_name: str, student_id: str):
        # Ensure student_id is unique
        if any(student.student_id == student_id for student in self.students):
            print("\n")
            print("Error: A student with this ID already exists.")
            return
        new_student = Student(student_name, student_id)
        self.students.append(new_student)
        print("\n")
        print(f"Student {student_name} added successfully.")

    def enroll_student(self, student_id: str, course_name: str, grade: str):
        student = self._find_student_by_id(student_id)
        if student:
            student.enroll_course(course_name, grade)
            print("\n")
            print(f"Student {student_id} enrolled in {course_name} with grade {grade}.")
        else:
            print("\n")
            print("Error: Student not found.")

    def view_student_details(self, student_id: str):
        student = self._find_student_by_id(student_id)
        if student:
            student.display_details()
        else:
            print("\n")
            print("Error: Student not found.")

    def list_all_students(self):
        if not self.students:
            print("\n")
            print("No students registered.")
            return
        print("\n")
        print("List of all students:")
        for student in self.students:
            print("\n")
            print(f"  - {student.student_name} (ID: {student.student_id})")

    def _find_student_by_id(self, student_id: str):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Record Management System")
        print("1. Add a new student")
        print("2. Enroll a student in a course")
        print("3. View a student's details")
        print("4. List all students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\n")
                student_name = input("Enter student name: ")
                student_id = input("Enter student ID: ")
                system.add_student(student_name, student_id)
            case "2":
                print("\n")
                student_id = input("Enter student ID: ")
                course_name = input("Enter course name: ")
                grade = input("Enter grade: ")
                system.enroll_student(student_id, course_name, grade)
            case "3":
                print("\n")
                student_id = input("Enter student ID: ")
                system.view_student_details(student_id)
            case "4":
                system.list_all_students()
            case "5":
                print("\n")
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("\n")
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()