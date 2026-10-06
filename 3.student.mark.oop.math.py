import math
import numpy as np
import curses

students = []
courses = []
marks = {}

def ask(stdscr, text):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(1, 2, text)
    stdscr.refresh()
    res = stdscr.getstr(2, 2).decode('utf-8').strip()
    curses.noecho()
    return res

def input_courses(stdscr):
    num = int(ask(stdscr, "Enter number of courses: "))
    for _ in range(num):
        c_id = ask(stdscr, "Enter course ID: ")
        c_name = ask(stdscr, "Enter course name: ")
        credits = float(ask(stdscr, "Enter credits: "))
        courses.append((c_id, c_name, credits))

def input_students(stdscr):
    num = int(ask(stdscr, "Enter number of students: "))
    for _ in range(num):
        s_id = ask(stdscr, "Enter student ID: ")
        s_name = ask(stdscr, "Enter student name: ")
        dob = ask(stdscr, "Enter DoB: ")
        students.append((s_id, s_name, dob))

def input_marks(stdscr):
    if not courses or not students:
        ask(stdscr, "Add courses and students first! (Press Enter)")
        return

    c_id = ask(stdscr, "Enter course ID to input marks: ")
    if not any(c[0] == c_id for c in courses):
        ask(stdscr, "Invalid course ID! (Press Enter)")
        return

    for s_id, s_name, _ in students:
        raw_mark = float(ask(stdscr, f"Enter mark for {s_name} ({s_id}): "))
        marks[(c_id, s_id)] = math.floor(raw_mark * 10.0) / 10.0

def calculate_gpa(s_id):
    c_list, m_list = [], []
    for c_id, _, credits in courses:
        if (c_id, s_id) in marks:
            c_list.append(credits)
            m_list.append(marks[(c_id, s_id)])
            
    if not c_list:
        return 0.0
        
    c_arr = np.array(c_list)
    m_arr = np.array(m_list)
    return float(np.sum(c_arr * m_arr) / np.sum(c_arr))

def list_courses(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "--- COURSES ---", curses.A_BOLD)
    row = 3
    for c_id, name, credits in courses:
        stdscr.addstr(row, 2, f"ID: {c_id} | Name: {name} | Credits: {credits}")
        row += 1
    ask(stdscr, "\nPress Enter to return...")

def list_students_sorted(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 2, "--- STUDENTS (SORTED BY GPA) ---", curses.A_BOLD)
    
    data = [(s_id, name, dob, calculate_gpa(s_id)) for s_id, name, dob in students]
    data.sort(key=lambda x: x[3], reverse=True)

    row = 3
    for s_id, name, dob, gpa in data:
        stdscr.addstr(row, 2, f"ID: {s_id} | Name: {name} | DoB: {dob} | GPA: {gpa:.2f}")
        row += 1
    ask(stdscr, "\nPress Enter to return...")

def show_marks(stdscr):
    if not courses:
        ask(stdscr, "No courses available! (Press Enter)")
        return

    c_id = ask(stdscr, "Enter course ID to view marks: ")
    stdscr.clear()
    stdscr.addstr(1, 2, f"--- MARKS FOR COURSE {c_id} ---", curses.A_BOLD)
    
    row = 3
    for s_id, name, _ in students:
        if (c_id, s_id) in marks:
            stdscr.addstr(row, 2, f"{name} ({s_id}): {marks[(c_id, s_id)]}")
            row += 1
    ask(stdscr, "\nPress Enter to return...")

def main(stdscr):
    curses.curs_set(0)
    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "=== STUDENT SYSTEM ===", curses.A_BOLD)
        stdscr.addstr(3, 2, "1. Input Courses")
        stdscr.addstr(4, 2, "2. Input Students")
        stdscr.addstr(5, 2, "3. Input Marks")
        stdscr.addstr(6, 2, "4. List Courses")
        stdscr.addstr(7, 2, "5. List Students (By GPA)")
        stdscr.addstr(8, 2, "6. Show Marks")
        stdscr.addstr(9, 2, "7. Exit")
        stdscr.addstr(11, 2, "Choice (1-7): ")
        stdscr.refresh()

        choice = stdscr.getkey()

        if choice == '1': input_courses(stdscr)
        elif choice == '2': input_students(stdscr)
        elif choice == '3': input_marks(stdscr)
        elif choice == '4': list_courses(stdscr)
        elif choice == '5': list_students_sorted(stdscr)
        elif choice == '6': show_marks(stdscr)
        elif choice == '7': break

if __name__ == "__main__":
    curses.wrapper(main)