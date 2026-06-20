import os
student_data="student_data.csv"
if not os.path.exists(student_data):
    with open(student_data,"w") as file:
        pass
class Student:
    def __init__(self,student_name,roll_no,course):
        self.student_name=student_name
        self.roll_no=roll_no
        self.course=course
    def show(self):
        print(f"===Student Record===")
        print(f"\n STUDENT NAME:{self.student_name} ROLL NUMER:{self.roll_no} COURSE:{self.course}")
class Details:
    def __init__(self):
        self.student_db=[]
    def add_student(self):
        print(f"---ADD NEW STUDENT---")
        name=input("ENTER STUDENT NAME:")
        roll_no=input("ENTER ROLL NUMBER:")
        course=input("ENTER COURSE:")
        new_student=Student(name,roll_no,course)
        self.student_db.append(new_student)
        with open(student_data,"a") as file:
            file.write(f"{new_student.student_name},{new_student.roll_no},{new_student.course}")
        print(f"SUCCESS: Record for{name} has been added successfully")
    def view_students(self):
        print(f"---DISPLAYING THE STUDENTS---")
        if not self.student_db:
            print(f"No student records found")
            return
        for student in self.student_db:
            student.show()
    def search_student(self):
        target_roll=input("enter the roll number:")
        found=False
        for student in self.student_db:
            if target_roll==self.roll_no:
                found=True
                print("MATCH FOUND")
                student.show()
                break
            if not found:
                print(f"No student found with {target_roll}number")
    def delete_student(self):
        target=input("enter the roll number:")
        student_to_remove=None
        for student in self.student_db:
            if target==self.roll_no:
                student_to_remove=student
                break
        if student_to_remove:
            self.student_db.remove(student_to_remove)
            print(f"SUCCESS: Student with roll number{target} is removed")
        else:
            print(f"ERROR: No student found")
def main():
    system=Details()
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. \nAdd Student Details")
        print("2. \nDisplay All Student Records")
        print("3. \nSearch for a Student")
        print("4. \nDelete a Student Record")
        print("5. Exit Program")
        print("=====================================")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.view_students()
        elif choice == '3':
            system.search_student()
        elif choice == '4':
            system.delete_student()
        elif choice == '5':
            print("\nThank you for using the Student Management System. Goodbye!")
            break
        else:
            print("\nInvalid selection! Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()