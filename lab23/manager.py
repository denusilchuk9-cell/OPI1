from employee import Employee

class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, team_size, project_count):
        super().__init__(name, employee_id, base_salary)
        self._team_size = team_size
        self._project_count = project_count
        self._bonus_per_project = 5000
        self._bonus_per_team_member = 300
    
    @property
    def team_size(self):
        return self._team_size
    
    def calculate_salary(self):
        bonus = (self._project_count * self._bonus_per_project) + (self._team_size * self._bonus_per_team_member)
        return self._base_salary + bonus
    
    def get_position(self):
        return "Менеджер"
    
    def get_info(self):
        return f"{super().get_info()}, Посада: {self.get_position()}, Команда: {self._team_size} осіб, Проєктів: {self._project_count}"