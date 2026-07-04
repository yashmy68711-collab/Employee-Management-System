class EmployeeManagement:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        emp_id = input("Enter Employee ID: ").strip()

        if emp_id in self.employees:
            print("Employee ID already exists!")
            return

        name = input("Enter Name: ").strip()
        department = input("Enter Department: ").strip()

        try:
            salary = float(input("Enter Salary: "))
        except:
            print("Invalid salary!")
            return

        self.employees[emp_id] = {
            "Name": name,
            "Department": department,
            "Salary": salary
        }

        print("Employee added successfully!")

    def view_employees(self):
        if len(self.employees) == 0:
            print("No employee records found.")
            return

        print("\n------ Employee Records ------")

        for emp_id, data in self.employees.items():
            print(f"\nEmployee ID : {emp_id}")
            print(f"Name        : {data['Name']}")
            print(f"Department  : {data['Department']}")
            print(f"Salary      : ₹{data['Salary']}")

    def search_employee(self):
        emp_id = input("Enter Employee ID: ")

        if emp_id in self.employees:
            data = self.employees[emp_id]

            print("\nEmployee Found")
            print(f"Name       : {data['Name']}")
            print(f"Department : {data['Department']}")
            print(f"Salary     : ₹{data['Salary']}")
        else:
            print("Employee not found!")

    def update_employee(self):
        emp_id = input("Enter Employee ID: ")

        if emp_id not in self.employees:
            print("Employee not found!")
            return

        name = input("Enter New Name: ").strip()
        department = input("Enter New Department: ").strip()

        try:
            salary = float(input("Enter New Salary: "))
        except:
            print("Invalid salary!")
            return

        self.employees[emp_id] = {
            "Name": name,
            "Department": department,
            "Salary": salary
        }

        print("Employee updated successfully!")

    def delete_employee(self):
        emp_id = input("Enter Employee ID: ")

        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")


system = EmployeeManagement()

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_employee()

    elif choice == "2":
        system.view_employees()

    elif choice == "3":
        system.search_employee()

    elif choice == "4":
        system.update_employee()

    elif choice == "5":
        system.delete_employee()

    elif choice == "6":
        print("Thank you for using Employee Management System!")
        break

    else:
        print("Invalid choice!")