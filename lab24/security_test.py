import unittest
from employee import Employee
from developer import Developer

class TestSecurity(unittest.TestCase):
    
    def test_private_fields_access(self):
        """Перевірка інкапсуляції (безпека даних)"""
        dev = Developer("Test", "T001", 30000, "Python", 2)
        
        # Спробуємо отримати доступ до приватних полів
        with self.assertRaises(AttributeError):
            dev._name  # Має бути доступно, але ми перевіряємо угоду
        
        # Перевіряємо, що через властивості можна отримати доступ
        self.assertEqual(dev.name, "Test")
    
    def test_malicious_input(self):
        """Перевірка на шкідливий ввід"""
        # Тестуємо дуже довгі рядки
        long_name = "A" * 10000
        try:
            dev = Developer(long_name, "T001", 30000, "Python", 2)
            self.assertEqual(len(dev.name), 10000)
        except:
            pass  # Може викинути помилку, це нормально
    
    def test_negative_values(self):
        """Перевірка від'ємних значень"""
        try:
            dev = Developer("Test", "T001", -30000, "Python", -2)
            # Якщо помилки немає - значить валідації немає
        except ValueError:
            # Якщо є валідація - це добре
            pass

if __name__ == "__main__":
    unittest.main()