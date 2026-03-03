from employee import Employee

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, programming_language, experience_years):
        super().__init__(name, employee_id, base_salary)
        self._programming_language = programming_language
        self._experience_years = experience_years
        self._bonus_per_year = 1000
    
    @property
    def programming_language(self):
        return self._programming_language
    
    def calculate_salary(self):
        bonus = self._experience_years * self._bonus_per_year
        return self._base_salary + bonus
    
    def get_position(self):
        return "Розробник"
    
    def get_info(self):
        return f"{super().get_info()}, Посада: {self.get_position()}, Мова: {self._programming_language}, Досвід: {self._experience_years} років"