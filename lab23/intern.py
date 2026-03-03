from employee import Employee

class Intern(Employee):
    def __init__(self, name, employee_id, base_salary, university, internship_months):
        super().__init__(name, employee_id, base_salary)
        self._university = university
        self._internship_months = internship_months
    
    @property
    def university(self):
        return self._university
    
    def calculate_salary(self):
        return self._base_salary * 0.5
    
    def get_position(self):
        return "Стажер"
    
    def get_info(self):
        return f"{super().get_info()}, Посада: {self.get_position()}, Університет: {self._university}, Місяців стажування: {self._internship_months}"