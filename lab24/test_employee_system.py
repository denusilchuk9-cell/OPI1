import unittest
from employee import Employee
from developer import Developer
from manager import Manager
from intern import Intern

class TestEmployeeSystem(unittest.TestCase):
    
    def setUp(self):
        """Підготовка даних перед кожним тестом"""
        self.dev = Developer("Олександр Петренко", "DEV001", 30000, "Python", 3)
        self.manager = Manager("Іван Мельник", "MGR001", 40000, 5, 2)
        self.intern = Intern("Анна Шевченко", "INT001", 15000, "КНУ", 6)
        self.employees = [self.dev, self.manager, self.intern]
    
    # TC-01: Тест створення розробника
    def test_developer_creation(self):
        self.assertEqual(self.dev.name, "Олександр Петренко")
        self.assertEqual(self.dev.employee_id, "DEV001")
        self.assertEqual(self.dev.base_salary, 30000)
        self.assertEqual(self.dev.programming_language, "Python")
        self.assertEqual(self.dev.get_position(), "Розробник")
    
    # TC-02: Тест створення менеджера
    def test_manager_creation(self):
        self.assertEqual(self.manager.name, "Іван Мельник")
        self.assertEqual(self.manager.employee_id, "MGR001")
        self.assertEqual(self.manager.base_salary, 40000)
        self.assertEqual(self.manager.team_size, 5)
        self.assertEqual(self.manager.get_position(), "Менеджер")
    
    # TC-03: Тест створення стажера
    def test_intern_creation(self):
        self.assertEqual(self.intern.name, "Анна Шевченко")
        self.assertEqual(self.intern.employee_id, "INT001")
        self.assertEqual(self.intern.base_salary, 15000)
        self.assertEqual(self.intern.university, "КНУ")
        self.assertEqual(self.intern.get_position(), "Стажер")
    
    # TC-04: Тест розрахунку зарплати розробника
    def test_developer_salary(self):
        expected_salary = 30000 + (3 * 1000)  # base + experience_years * 1000
        self.assertEqual(self.dev.calculate_salary(), expected_salary)
    
    # TC-05: Тест розрахунку зарплати менеджера
    def test_manager_salary(self):
        expected_salary = 40000 + (2 * 5000) + (5 * 300)  # base + projects*5000 + team*300
        self.assertEqual(self.manager.calculate_salary(), expected_salary)
    
    # TC-06: Тест розрахунку зарплати стажера
    def test_intern_salary(self):
        expected_salary = 15000 * 0.5  # 50% від базової
        self.assertEqual(self.intern.calculate_salary(), expected_salary)
    
    # TC-07: Тест поліморфної обробки
    def test_polymorphism(self):
        salaries = [emp.calculate_salary() for emp in self.employees]
        
        # Перевіряємо, що кожен тип рахує по-різному
        self.assertNotEqual(salaries[0], salaries[1])
        self.assertNotEqual(salaries[1], salaries[2])
        self.assertNotEqual(salaries[0], salaries[2])
        
        # Перевіряємо загальну суму
        total = sum(salaries)
        expected_total = (30000 + 3000) + (40000 + 10000 + 1500) + (7500)
        self.assertEqual(total, expected_total)
    
    # TC-08: Тест get_info методу
    def test_get_info(self):
        dev_info = self.dev.get_info()
        self.assertIn("Олександр Петренко", dev_info)
        self.assertIn("DEV001", dev_info)
        self.assertIn("Розробник", dev_info)
        self.assertIn("Python", dev_info)
    
    # TC-09: Тест валідації (якщо додамо в майбутньому)
    @unittest.expectedFailure
    def test_validation(self):
        # Цей тест очікувано провалиться, бо валідації поки немає
        invalid_dev = Developer("", -5, -1000, "", -1)

if __name__ == "__main__":
    unittest.main(verbosity=2)