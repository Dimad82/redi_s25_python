class Employee:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def calculate_pay(self):
        return 0

    def employee_attributes(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nId: {self.id}"

    def __str__(self):
        return f"Employee:\n{self.employee_attributes()}"
    
class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, id, salary):
        self.salary = salary
        Employee.__init__(self, first_name, last_name, id)
    
    def calculate_pay(self):
        return self.salary / 12

    def __str__(self):
        return f"\nSalariedEmployee:\n{self.employee_attributes()}\nSalary: {self.salary}"
    
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, id, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        Employee.__init__(self, first_name, last_name, id)
    
    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"\nHourlyEmployee:\n{self.employee_attributes()}\nHourly Rate: {self.hourly_rate}\nHours worked: {self.hours_worked}"

def calculate_employee_pay(obj):
    if(not isinstance(obj, Employee)):
        print("Cant calculate pay of a non-employee!!")
        return
    print(f"Pay: {obj.calculate_pay()}")

salaried_employee = SalariedEmployee("John", "Smith", 51425719, 30000)
hourly_employee = HourlyEmployee("Jake", "Schmidt", 9821335, 10, 40)

print(salaried_employee)
calculate_employee_pay(salaried_employee)

print(hourly_employee)
calculate_employee_pay(hourly_employee)