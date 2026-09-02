# Parent Class
class Employee:

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    # Common method
    def display_info(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Child class  
class Manager(Employee):

    def __init__(self, name, employee_id, salary, team_size):
        # Calling parent class constructor
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    # Specific method for Manager
    def display_team(self):
        print("Team Size:", self.team_size)


# Creating objects
employee1 = Employee("Rahul", 101, 30000)
manager1 = Manager("Ayesha", 102, 60000, 10)

# Displaying parent class object
print("Employee Details:")
employee1.display_info()

print("\nManager Details:")
manager1.display_info()      # Inherited method
manager1.display_team()     # Child-specific method