import task_solutions
import user_interaction
import practical_tasks
import homework

def main_menu():
    while True:
        print("\n" + "="*60)
        print("ПРАКТИЧНЕ ЗАНЯТТЯ: СПИСКИ ТА КОРТЕЖІ В PYTHON")
        print("="*60)
        print("1. Створення списків та кортежів")
        print("2. Робота з індексами та зрізами")
        print("3. Вбудовані функції та методи")
        print("4. Спискові включення")
        print("5. Функції для роботи зі списками")
        print("6. Практичні задачі")
        print("7. Взаємодія з користувачем")
        print("8. Домашнє завдання")
        print("9. Практичні завдання (40 прикладів)")
        print("0. Вихід")
        
        choice = input("\nОберіть опцію: ")
        
        if choice == "1":
            task_solutions.demo_creation()
        elif choice == "2":
            task_solutions.demo_indexing_slicing()
        elif choice == "3":
            task_solutions.demo_builtin_functions()
        elif choice == "4":
            task_solutions.demo_list_comprehensions()
        elif choice == "5":
            task_solutions.demo_functions_methods()
        elif choice == "6":
            task_solutions.demo_practical_problems()
        elif choice == "7":
            user_interaction.run_interactive_demo()
        elif choice == "8":
            homework.run_homework()
        elif choice == "9":
            practical_tasks.show_all_tasks()
        elif choice == "0":
            print("Дякую за використання програми!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()