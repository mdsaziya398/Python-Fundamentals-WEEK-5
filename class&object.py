# Creating a class
class Student:
    # Constructor to define attributes
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
        


# Creating two objects
student1 = Student("Ayesha", 101, "Computer Science", 85)
student2 = Student("Rahul", 102, "Information Technology", 90)

# Displaying information of each object
print("Student 1 Details:")
student1.display_info()

print("Student 2 Details:")
student2.display_info()