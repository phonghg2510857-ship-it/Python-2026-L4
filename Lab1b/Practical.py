students = []
courses = []
marks = {}
def input_student():
    num_student = int(input("Enter number of students: "))
    for _ in range(num_student):
        id_student = input("Enter student ID: ")
        name_student = input("Enter student name: ")
        dob = input("Enter Date of Birth: ")
        students.append((id_student, name_student, dob))

def input_courses():
    num_courses = int(input("\nEnter number of courses: "))
    for _ in range(num_courses):
        id_course = input("Enter course ID: ")
        name_course = input("Enter course name: ")
        courses.append((id_course, name_course))
def input_marks():
    if not courses:
        print("\nNo course available.")
        return
    if not students:
        print("\nNo student available.")
        return
    list_courses()
    selected_course_id = input("Enter course ID to enter marks: ")
    if not any(c[0] == selected_course_id for c in courses):
        print("Invalid course ID!")
        return
    print(f"\nEnter marks for course: {selected_course_id}")
    for id_student, name_student, _ in students:
        mark = float(input(f"Enter mark for {name_student} {id_student}: "))
        marks[(selected_course_id, id_student)] = mark

def list_courses():
    print("\n List of Courses")
    if not courses:
        print("No course available.")
        return
    for id_course, name_course in courses: 
        print(f"ID: {id_course} | Name: {name_course}")

def list_student():
    print("\nList of Student")
    if not students:
        print("No student available.")
        return
    for id_student, name_student, dob in students:
        print(f"ID: {id_student} | Name: {name_student} | Date of Birth: {dob}")

def show_mark_for_course():
    if not courses:
        print("\nNo course available.")
        return
    list_courses()
    selected_course_id = input("\nEnter course ID to show marks: ")
    print(f"\nMarks for Course {selected_course_id}")
    found = False
    for s_id, name, _ in students:
        key = (selected_course_id, s_id)
        if key in marks:
            print(f"Student: {name} ({s_id}) | Mark: {marks[key]}")
            found = True
            
    if not found:
        print("No marks recorded for this course.") 

def main():
    input_courses()
    input_student()
    while True:
        print("\n==============================")
        print("  STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. List Courses")
        print("2. List Students")
        print("3. Input Marks for a Course")
        print("4. Show Student Marks for a Course")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            list_courses()
        elif choice == '2':
            list_student()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            show_mark_for_course()
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()   