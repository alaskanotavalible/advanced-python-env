class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._salary * 0.2


def print_employees(employees):
    for emp in employees:
        print(f"Role: {emp.get_role()}, Salary: {emp.get_salary()}")


staff = [
    Employee(1000),
    Manager(2000)
]

print_employees(staff)