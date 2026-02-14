from db import connect
from student import Student
print("Starting Student Management System...")
def add_student():
    db = connect()
    cursor = db.cursor()
    
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    email = input("Enter email: ")
    
    student = Student(name, age, grade, email)
    
    query = "INSERT INTO students (name, age, grade, email) VALUES (%s, %s, %s, %s)"
    values = (student.name, student.age, student.grade, student.email)
    cursor.execute(query, values)
    db.commit()
    print("Student added successfully!")

def view_students():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_student():
    db = connect()
    cursor = db.cursor()
    student_id = input("Enter student ID to search: ")
    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("Student not found.")

def update_student():
    db = connect()
    cursor = db.cursor()
    student_id = input("Enter student ID to update: ")
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    grade = input("Enter new grade: ")
    email = input("Enter new email: ")
    
    query = "UPDATE students SET name=%s, age=%s, grade=%s, email=%s WHERE id=%s"
    values = (name, age, grade, email, student_id)
    cursor.execute(query, values)
    db.commit()
    print("Student updated successfully!")

def delete_student():
    db = connect()
    cursor = db.cursor()
    student_id = input("Enter student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    db.commit()
    print("Student deleted successfully!")

# Main Menu
while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
