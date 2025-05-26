class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours = None, rest_days = None, email = None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days 
        self.email = email 

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None and rest_days is not  None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
        
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{self.name}@email.com"
        return cls(name, hours, rest_days, email)
               
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    
    def salary(self):
        return self.hours * self.hourly_payment


# Пример использования класса:
employee1 = EmployeeSalary("Иванов", rest_days=2)
print("Имя сотрудника:", employee1.name, "количество выходных:", employee1.rest_days, "зарплата:", employee1.salary())

employee2 = EmployeeSalary("Петров", hours=35, email="petrov@example.com")
print("Имя сотрудника:", employee2.name, "количество рабочих часов:", employee2.hours, "зарплата:", employee2.salary())

EmployeeSalary.set_hourly_payment(450)
employee3 = EmployeeSalary("Сидоров")
print("Имя сотрудника:", employee3.name, "количество рабочих часов:", employee3.hourly_payment, "зарплата:", employee3.salary())
