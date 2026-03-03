import time
import random
from developer import Developer
from manager import Manager
from intern import Intern

def load_test_creation(count=1000):
    """Тест створення великої кількості об'єктів"""
    print(f"\n--- НАВАНТАЖУВАЛЬНЕ ТЕСТУВАННЯ (створення {count} об'єктів) ---")
    
    start_time = time.time()
    
    employees = []
    for i in range(count):
        if i % 3 == 0:
            emp = Developer(f"Dev_{i}", f"DEV{i:04d}", random.randint(20000, 50000), 
                           random.choice(["Python", "Java", "C#"]), random.randint(1, 10))
        elif i % 3 == 1:
            emp = Manager(f"Man_{i}", f"MGR{i:04d}", random.randint(30000, 60000),
                         random.randint(1, 20), random.randint(1, 5))
        else:
            emp = Intern(f"Int_{i}", f"INT{i:04d}", random.randint(10000, 20000),
                        "Test University", random.randint(1, 12))
        employees.append(emp)
    
    creation_time = time.time() - start_time
    print(f"Час створення {count} об'єктів: {creation_time:.4f} сек")
    print(f"Середній час на об'єкт: {(creation_time/count)*1000:.4f} мс")
    
    return employees

def load_test_salary_calculation(employees):
    """Тест розрахунку зарплати для багатьох об'єктів"""
    print(f"\n--- ТЕСТ РОЗРАХУНКУ ЗАРПЛАТИ ({len(employees)} об'єктів) ---")
    
    start_time = time.time()
    
    total_salary = 0
    for emp in employees:
        total_salary += emp.calculate_salary()
    
    calculation_time = time.time() - start_time
    print(f"Час розрахунку: {calculation_time:.4f} сек")
    print(f"Загальна сума: {total_salary:,.0f} грн")
    print(f"Середня зарплата: {total_salary/len(employees):,.0f} грн")

def memory_test():
    """Тест використання пам'яті"""
    print("\n--- ТЕСТ ПАМ'ЯТІ ---")
    
    import psutil
    import os
    
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss / 1024 / 1024  # MB
    
    employees = load_test_creation(10000)
    
    memory_after = process.memory_info().rss / 1024 / 1024  # MB
    memory_used = memory_after - memory_before
    
    print(f"Пам'ять до: {memory_before:.2f} MB")
    print(f"Пам'ять після: {memory_after:.2f} MB")
    print(f"Використано пам'яті: {memory_used:.2f} MB")
    print(f"Середнє на об'єкт: {(memory_used * 1024 / 10000):.2f} KB")

def main():
    print("=" * 60)
    print("НАВАНТАЖУВАЛЬНЕ ТЕСТУВАННЯ СИСТЕМИ")
    print("=" * 60)
    
    # Тест 1: Малі дані (100 об'єктів)
    emp1 = load_test_creation(100)
    load_test_salary_calculation(emp1)
    
    # Тест 2: Середні дані (1000 об'єктів)
    emp2 = load_test_creation(1000)
    load_test_salary_calculation(emp2)
    
    # Тест 3: Великі дані (10000 об'єктів)
    emp3 = load_test_creation(10000)
    load_test_salary_calculation(emp3)
    
    # Тест пам'яті
    try:
        memory_test()
    except:
        print("Пропускаємо тест пам'яті (потрібна бібліотека psutil)")

if __name__ == "__main__":
    main()