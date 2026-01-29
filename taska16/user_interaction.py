def run_interactive_demo():
    print("\n" + "="*60)
    print("7. ВЗАЄМОДІЯ З КОРИСТУВАЧЕМ")
    print("="*60)
    
    print("\n--- Система управління завданнями ---")
    tasks = []
    
    while True:
        print("\nМеню:")
        print("1. Додати завдання")
        print("2. Переглянути завдання")
        print("3. Позначити виконаним")
        print("4. Видалити завдання")
        print("5. Сортувати завдання")
        print("6. Пошук завдання")
        print("0. Вийти")
        
        choice = input("Оберіть опцію: ")
        
        if choice == "1":
            task_name = input("Введіть назву завдання: ")
            priority = input("Введіть пріоритет (високий/середній/низький): ")
            tasks.append({"назва": task_name, "пріоритет": priority, "виконано": False})
            print(f"Завдання '{task_name}' додано!")
        
        elif choice == "2":
            if not tasks:
                print("Список завдань порожній")
            else:
                print("\nСписок завдань:")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["виконано"] else "✗"
                    print(f"{i}. {task['назва']} [{task['пріоритет']}] {status}")
        
        elif choice == "3":
            if not tasks:
                print("Список завдань порожній")
            else:
                print("\nСписок завдань:")
                for i, task in enumerate(tasks, 1):
                    if not task["виконано"]:
                        print(f"{i}. {task['назва']}")
                
                try:
                    task_num = int(input("Номер завдання для позначення виконаним: "))
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num-1]["виконано"] = True
                        print("Завдання позначено виконаним!")
                    else:
                        print("Невірний номер")
                except ValueError:
                    print("Введіть число")
        
        elif choice == "4":
            if not tasks:
                print("Список завдань порожній")
            else:
                print("\nСписок завдань:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task['назва']}")
                
                try:
                    task_num = int(input("Номер завдання для видалення: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num-1)
                        print(f"Завдання '{removed['назва']}' видалено!")
                    else:
                        print("Невірний номер")
                except ValueError:
                    print("Введіть число")
        
        elif choice == "5":
            if not tasks:
                print("Список завдань порожній")
            else:
                sort_by = input("Сортувати за (назва/пріоритет): ")
                if sort_by == "назва":
                    tasks.sort(key=lambda x: x["назва"])
                    print("Відсортовано за назвою")
                elif sort_by == "пріоритет":
                    priority_order = {"високий": 1, "середній": 2, "низький": 3}
                    tasks.sort(key=lambda x: priority_order.get(x["пріоритет"], 4))
                    print("Відсортовано за пріоритетом")
                else:
                    print("Невірний параметр сортування")
        
        elif choice == "6":
            if not tasks:
                print("Список завдань порожній")
            else:
                search_term = input("Введіть текст для пошуку: ")
                results = [task for task in tasks if search_term.lower() in task["назва"].lower()]
                
                if results:
                    print(f"\nЗнайдено {len(results)} завдання:")
                    for i, task in enumerate(results, 1):
                        status = "✓" if task["виконано"] else "✗"
                        print(f"{i}. {task['назва']} [{task['пріоритет']}] {status}")
                else:
                    print("Завдань не знайдено")
        
        elif choice == "0":
            print("Вихід з системи управління завданнями")
            break
        
        else:
            print("Невірний вибір")
    
    print("\n--- Калькулятор статистики ---")
    numbers = []
    while True:
        value = input("Введіть число (або 'stop' для завершення): ")
        if value.lower() == 'stop':
            break
        try:
            numbers.append(float(value))
        except ValueError:
            print("Введіть коректне число або 'stop'")
    
    if numbers:
        print(f"\nВведені числа: {numbers}")
        print(f"Кількість: {len(numbers)}")
        print(f"Сума: {sum(numbers)}")
        print(f"Середнє: {sum(numbers)/len(numbers):.2f}")
        print(f"Мінімум: {min(numbers)}")
        print(f"Максимум: {max(numbers)}")
        print(f"Відсортовані: {sorted(numbers)}")
    else:
        print("Не введено жодного числа")