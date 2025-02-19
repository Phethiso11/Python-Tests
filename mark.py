student_mark_input = input("Enter the student mark: ")

if student_mark_input == "-0":
    print("Invalid Mark")
else:
    student_mark = int(student_mark_input)
    if student_mark < 0 or student_mark > 100:
        print("Invalid Mark")
    elif student_mark == 0:
        print("Fail")
    elif student_mark < 50:
        print("Fail")
    elif student_mark <= 60:
        print("Average Pass")
    else:
        print("Pass")