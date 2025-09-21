"""
Student Grade Management System using Tuples
--------------------------------------------
This project manages student details (name, roll number, marks).
Features:
1. Add new students
2. Display all students
3. Find topper
4. Calculate class average
"""

# List to hold student tuples
students = []

def add_student(name, roll_no, marks):
    """Add a new student as a tuple"""
    student = (name, roll_no, marks)
    students.append(student)
    print(f" Student {name} added successfully!")

def display_students():
    """Display all students"""
    if not students:
        print(" No students available!")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s[0]}, Roll No: {s[1]}, Marks: {s[2]}")

def find_topper():
    """Find the student with the highest marks"""
    if not students:
        print(" No students available!")
        return
    topper = max(students, key=lambda x: x[2])
    print(f"\n Topper: {topper[0]} (Roll: {topper[1]}) with {topper[2]} marks")

def calculate_average():
    """Calculate class average marks"""
    if not students:
        print(" No students available!")
        return
    avg = sum(s[2] for s in students) / len(students)
    print(f"\n Class Average Marks: {avg:.2f}")

# ---------- Demo Run ----------
if __name__ == "__main__":
    # Sample data
    add_student("Ravi", 1, 85)
    add_student("Sita", 2, 92)
    add_student("John", 3, 78)
    add_student("Ali", 4, 88)

    display_students()
    find_topper()
    calculate_average()
