import math
import itertools
from task_solutions import *
from user_interaction import *
from practical_tasks import *

def main():
    """Головна функція програми"""
    print("=" * 50)
    print("ПРАКТИЧНЕ ЗАНЯТТЯ: ЦИКЛИ ТА ФУНКЦІЇ В PYTHON")
    print("=" * 50)
    
    while True:
        print("\nМЕНЮ:")
        print("1. Демонстрація основних циклів")
        print("2. Демонстрація функцій")
        print("3. Комбінація циклів та функцій")
        print("4. Використання бібліотек")
        print("5. Реальна задача: калькулятор статистики")
        print("6. Взаємодія з користувачем")
        print("7. Перегляд практичних завдань")
        print("8. Виконання домашнього завдання")
        print("0. Вийти з програми")
        
        choice = input("\nОберіть опцію (0-8): ")
        
        if choice == "1":
            demonstrate_basic_loops()
        elif choice == "2":
            demonstrate_functions()
        elif choice == "3":
            demonstrate_loops_and_functions()
        elif choice == "4":
            demonstrate_libraries()
        elif choice == "5":
            run_statistics_calculator()
        elif choice == "6":
            run_user_interaction()
        elif choice == "7":
            show_practical_tasks()
        elif choice == "8":
            run_homework()
        elif choice == "0":
            print("Дякую за використання програми!")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()