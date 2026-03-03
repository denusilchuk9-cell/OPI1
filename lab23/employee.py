from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id, base_salary):
        self._name = name
        self._employee_id = employee_id
        self._base_salary = base_salary
    
    @property
    def name(self):
        return self._name
    
    @property
    def employee_id(self):
        return self._employee_id
    
    @property
    def base_salary(self):
        return self._base_salary
    
    @abstractmethod
    def calculate_salary(self):
        pass
    
    @abstractmethod
    def get_position(self):
        pass
    
    def get_info(self):
        return f"Працівник: {self._name}, ID: {self._employee_id}"