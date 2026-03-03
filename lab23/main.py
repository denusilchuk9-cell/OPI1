from developer import Developer
from manager import Manager
from intern import Intern

def main():
    print("=" * 50)
    print("СИСТЕМА УПРАВЛІННЯ ПРАЦІВНИКАМИ")
    print("=" * 50)
    
    dev1 = Developer("Олександр Петренко", "DEV001", 30000, "Python", 3)
    dev2 = Developer("Марія Коваленко", "DEV002", 32000, "JavaScript", 2)
    manager = Manager("Іван Мельник", "MGR001", 40000, 5, 2)
    intern = Intern("Анна Шевченко", "INT001", 15000, "КНУ ім. Шевченка", 6)
    
    employees = [dev1, dev2, manager, intern]
    
    print("\n--- ІНФОРМАЦІЯ ПРО ПРАЦІВНИКІВ ---")
    for emp in employees:
        print(emp.get_info())
    
    print("\n--- РОЗРАХУНОК ЗАРПЛАТИ (ПОЛІМОРФІЗМ) ---")
    total_salary = 0
    for emp in employees:
        salary = emp.calculate_salary()
        total_salary += salary
        print(f"{emp.name} ({emp.get_position()}): {salary} грн")
    
    print("\n" + "=" * 50)
    print(f"ЗАГАЛЬНИЙ ФОНД ОПЛАТИ ПРАЦІ: {total_salary} грн")
    print("=" * 50)
    
    print("\n--- ДЕМОНСТРАЦІЯ ПОЛІМОРФІЗМУ ---")
    print("Всі працівники обробляються через спільний інтерфейс Employee")
    print("Метод calculate_salary() працює по-різному для кожного класу:")
    print("- Developer: базова зарплата + бонус за досвід")
    print("- Manager: базова зарплата + бонус за проєкти + бонус за команду")
    print("- Intern: 50% від базової зарплати")

if __name__ == "__main__":
    main()