class StudentNode:
    def __init__(self, roll, name, dept, cgpa):
        self.roll = roll
        self.name = name
        self.dept = dept
        self.cgpa = cgpa
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name, dept, cgpa):
        new_student = StudentNode(roll, name, dept, cgpa)
        if self.head is None:
            self.head = new_student
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_student
        print(f"Student {name} (Roll: {roll}) added successfully.")

    def delete_student(self, roll):
        temp = self.head
        if temp is not None and temp.roll == roll:
            self.head = temp.next
            print(f"Student with Roll {roll} deleted successfully.")
            return
        prev = None
        while temp is not None and temp.roll != roll:
            prev = temp
            temp = temp.next
        if temp is None:
            print(f"No student found with Roll {roll}.")
            return
        prev.next = temp.next
        print(f"Student with Roll {roll} deleted successfully.")

    def search_student(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"Found: Roll: {temp.roll}, Name: {temp.name}, Dept: {temp.dept}, CGPA: {temp.cgpa}")
                return temp
            temp = temp.next
        print(f"No student found with Roll {roll}.")
        return None

    def display_students(self):
        temp = self.head
        if not temp:
            print("No student records found.")
            return
        print("\nStudent Records:")
        while temp:
            print(f"Roll: {temp.roll}, Name: {temp.name}, Dept: {temp.dept}, CGPA: {temp.cgpa}")
            temp = temp.next


if __name__ == "__main__":
    records = StudentLinkedList()
    records.add_student(24001, "Kaniksha", "CSE", 9.5)
    records.add_student(24002, "Lakshmi", "IT", 9.4)
    records.add_student(24003, "Kritika", "CSE", 9.6)
    records.add_student(24004, "Krishna", "IT", 9.3)
    records.add_student(24005, "Aparna", "CSE", 9.7)
    records.add_student(24006, "Vihaan", "IT", 9.8)

    records.display_students()
    records.search_student(24003)
    records.search_student(24010)
    records.delete_student(24002)
    records.delete_student(24010)
    records.display_students()
