# Creating a class
class Student:

    # Constructor
    def __init__(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    # Method to display student information
    def display_info(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("------------------------")


# Creating objects with different values
student1 = Student("Ayesha", 101, "Computer Science", 85)
student2 = Student("Rahul", 102, "Information Technology", 90)

# Accessing initialized attributes
print("Student 1 Name:", student1.name)
print("Student 1 Marks:", student1.marks)

print()

print("Student 2 Name:", student2.name)
print("Student 2 Marks:", student2.marks)

print("\nStudent 1 Details:")
student1.display_info()

print("Student 2 Details:")
student2.display_info()