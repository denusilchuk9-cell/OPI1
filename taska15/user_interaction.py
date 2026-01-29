def run_user_interaction():
    """Демонстрація взаємодії з користувачем"""
    print("\n" + "="*50)
    print("ВЗАЄМОДІЯ З КОРИСТУВАЧЕМ")
    print("="*50)
    
    # 1.введення даних
    print("\n1. Просте введення даних:")
    name = input("  Введіть ваше ім'я: ")
    age = input("  Введіть ваш вік: ")
    print(f"  Привіт, {name}! Тобі {age} років.")
    
    # 2.введення чисел та перетворення типів
    print("\n2. Введення чисел:")
    try:
        num1 = float(input("  Введіть перше число: "))
        num2 = float(input("  Введіть друге число: "))
        print(f"  Сума: {num1 + num2:.2f}")
        print(f"  Добуток: {num1 * num2:.2f}")
    except ValueError:
        print("  Помилка! Будь ласка, введіть коректні числа.")
    
    # 3.цикл для збору даних
    print("\n3. Збір декількох значень:")
    numbers = []
    while True:
        user_input = input("  Введіть число (або 'stop' для завершення): ")
        if user_input.lower() == 'stop':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("  Помилка! Введіть коректне число або 'stop'.")
    
    if numbers:
        print(f"  Введені числа: {numbers}")
        print(f"  Середнє значення: {sum(numbers)/len(numbers):.2f}")
    else:
        print("  Не введено жодного числа.")
    
    # 4.меню з вибором опцій
    print("\n4. Меню з вибором опцій:")
    
    def calculator_menu():
        """Простий калькулятор"""
        print("\n  --- КАЛЬКУЛЯТОР ---")
        print("  1. Додавання")
        print("  2. Віднімання")
        print("  3. Множення")
        print("  4. Ділення")
        print("  0. Вийти")
    
    while True:
        calculator_menu()
        choice = input("  Оберіть операцію (0-4): ")
        
        if choice == "0":
            print("  Вихід з калькулятора.")
            break
        
        if choice in ["1", "2", "3", "4"]:
            try:
                a = float(input("  Введіть перше число: "))
                b = float(input("  Введіть друге число: "))
                
                if choice == "1":
                    result = a + b
                    operation = "+"
                elif choice == "2":
                    result = a - b
                    operation = "-"
                elif choice == "3":
                    result = a * b
                    operation = "*"
                elif choice == "4":
                    if b == 0:
                        print("  Помилка: ділення на нуль!")
                        continue
                    result = a / b
                    operation = "/"
                
                print(f"  Результат: {a} {operation} {b} = {result:.2f}")
            except ValueError:
                print("  Помилка! Введіть коректні числа.")
        else:
            print("  Некоректний вибір. Спробуйте ще раз.")