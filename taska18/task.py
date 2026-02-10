def safe_divide():
    try:
        a = int(input("Введіть чисельник: "))
        b = int(input("Введіть знаменник: "))
        result = a / b
    except ZeroDivisionError:
        print("Помилка: ділення на нуль!")
    except ValueError:
        print("Помилка: введіть коректні числа!")
    else:
        print(f"Результат ділення: {result}")
        print("Операція виконана без помилок!")
    finally:
        print("Завершення операції ділення.")

def validate_number():
    data = input("Введіть число: ")
    try:
        num = float(data)
    except ValueError:
        print("Це не число!")
        return None
    else:
        print(f"Коректне число: {num}")
        return num

def process_list():
    my_list = [1, 2, 3, 4, 5]
    try:
        index = int(input(f"Введіть індекс (0-{len(my_list)-1}): "))
        value = my_list[index]
    except IndexError:
        print("Помилка: некоректний індекс!")
    except ValueError:
        print("Помилка: введіть ціле число!")
    else:
        print(f"Значення: {value}")

def dictionary_access():
    data = {"a": 1, "b": 2, "c": 3}
    try:
        key = input("Введіть ключ: ")
        value = data[key]
    except KeyError:
        print("Помилка: ключ не знайдено!")
    else:
        print(f"Значення: {value}")

def calculator():
    try:
        x = float(input("Введіть перше число: "))
        op = input("Введіть операцію (+, -, *, /): ")
        y = float(input("Введіть друге число: "))
        
        if op == '+':
            result = x + y
        elif op == '-':
            result = x - y
        elif op == '*':
            result = x * y
        elif op == '/':
            result = x / y
        else:
            print("Невідома операція!")
            return
    except ZeroDivisionError:
        print("Помилка: ділення на нуль!")
        return
    except ValueError:
        print("Помилка: некоректні числа!")
        return
    else:
        print(f"Результат: {result}")

def file_operations():
    filename = input("Введіть ім'я файлу: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("Помилка: файл не знайдено!")
    except PermissionError:
        print("Помилка: недостатньо прав!")
    else:
        print("Файл успішно прочитано!")
        print(f"Перші 100 символів: {content[:100]}")
    finally:
        print("Операція з файлом завершена.")

def multiple_exceptions():
    import random
    try:
        num = random.choice(["10", "abc", "5.5", "0"])
        converted = int(num)
        result = 100 / converted
    except (ValueError, TypeError):
        print("Помилка перетворення!")
    except ZeroDivisionError:
        print("Ділення на нуль!")
    else:
        print(f"Успіх: {result}")

def average_calculation():
    numbers = input("Введіть числа через пробіл: ").split()
    try:
        nums = [float(x) for x in numbers]
        avg = sum(nums) / len(nums)
    except ValueError:
        print("Деякі значення не є числами!")
    except ZeroDivisionError:
        print("Не введено жодного числа!")
    else:
        print(f"Середнє: {avg}")

def retry_input():
    while True:
        try:
            value = int(input("Введіть ціле число: "))
            break
        except ValueError:
            print("Некоректне число, спробуйте ще!")
    print(f"Введено: {value}")

def nested_try():
    my_data = [10, 20, 30, 40, 50]
    try:
        index_input = input("Введіть індекс: ")
        index = int(index_input)
        try:
            value = my_data[index]
        except IndexError:
            print("Індекс поза межами списку!")
        else:
            print(f"Значення: {value}")
    except ValueError:
        print("Індекс має бути цілим числом!")

def without_exception():
    value = "abc"
    number = int(value)
    print(f"Число: {number}")

def with_exception():
    try:
        value = "abc"
        number = int(value)
        print(f"Число: {number}")
    except ValueError:
        print("Помилка перетворення рядка в число!")

def divide_zero():
    try:
        x = 10
        y = 0
        result = x / y
        print(result)
    except ZeroDivisionError:
        print("Не можна ділити на нуль!")

def string_to_int():
    try:
        text = "123abc"
        number = int(text)
        print(number)
    except ValueError:
        print("Рядок не містить числа!")

def list_by_index():
    my_list = [1, 2, 3]
    try:
        index = int(input("Індекс: "))
        print(my_list[index])
    except IndexError:
        print("Індекс поза діапазоном!")

def dict_by_key():
    my_dict = {"name": "John", "age": 25}
    try:
        key = input("Ключ: ")
        print(my_dict[key])
    except KeyError:
        print("Ключ не знайдений!")

def calculator_extended():
    try:
        x = float(input("Перше число: "))
        y = float(input("Друге число: "))
        op = input("Операція: ")
        if op == '+':
            result = x + y
        elif op == '-':
            result = x - y
        elif op == '*':
            result = x * y
        elif op == '/':
            result = x / y
        else:
            print("Невірна операція")
            return
        print(f"Результат: {result}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"Помилка: {type(e).__name__}")

def else_block():
    try:
        num = int(input("Число: "))
    except ValueError:
        print("Не число!")
    else:
        print(f"Ви ввели: {num}")

def finally_block():
    try:
        file = open("test.txt", "r")
        data = file.read()
        print(data)
    except FileNotFoundError:
        print("Файл не знайдено")
    finally:
        print("Блок finally виконано")

def open_user_file():
    try:
        filename = input("Ім'я файлу: ")
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Файл не існує")

def permission_check():
    try:
        with open("/root/test.txt", "r") as f:
            print(f.read())
    except PermissionError:
        print("Немає доступу")

def multiple_in_one():
    try:
        x = input("Введіть число: ")
        y = int(x) / 2
    except (ValueError, TypeError):
        print("Помилка типу")

def catch_all():
    try:
        x = 1 / 0
    except Exception:
        print("Сталася помилка")

def custom_type_error():
    try:
        x = "hello"
        y = x + 5
    except TypeError:
        print("Невірний тип даних")

def average_validation():
    try:
        nums = list(map(float, input("Числа через пробіл: ").split()))
        avg = sum(nums) / len(nums)
        print(avg)
    except (ValueError, ZeroDivisionError):
        print("Помилка в даних")

def safe_convert():
    def convert(x):
        try:
            return int(x)
        except ValueError:
            return None
    print(convert("123"))
    print(convert("abc"))

def repeat_until_valid():
    while True:
        try:
            n = int(input("Ціле число: "))
            break
        except ValueError:
            continue
    print(f"Введено: {n}")

def convert_list_items():
    items = ["1", "2", "three", "4"]
    numbers = []
    for item in items:
        try:
            numbers.append(int(item))
        except ValueError:
            print(f"Пропускаю: {item}")
    print(numbers)

def nested_exceptions():
    lst = [10, 20, 30]
    try:
        idx = int(input("Індекс: "))
        try:
            print(lst[idx])
        except IndexError:
            print("Невірний індекс")
    except ValueError:
        print("Не число")

def separate_errors():
    try:
        x = int(input("Число: "))
        y = int(input("Дільник: "))
        print(x / y)
    except ValueError:
        print("Невірне число")
    except ZeroDivisionError:
        print("Ділення на нуль")

def crash_example():
    x = input("Введіть число: ")
    y = 10 / int(x)
    print(y)

def safe_crash_example():
    try:
        x = input("Введіть число: ")
        y = 10 / int(x)
        print(y)
    except (ValueError, ZeroDivisionError):
        print("Помилка обробки")

def read_config():
    try:
        with open("config.txt", "r") as f:
            print(f.read())
    except IOError:
        print("Помилка читання файлу")

def database_simulation():
    class DatabaseError(Exception):
        pass
    
    try:
        raise DatabaseError("Не вдалося підключитися")
    except DatabaseError:
        print("Помилка бази даних")

def handle_os_error():
    import os
    try:
        os.remove("nonexistent.txt")
    except OSError:
        print("Файл не знайдено")

def check_age():
    try:
        age = int(input("Вік: "))
        if age < 0:
            raise ValueError("Вік не може бути від'ємним")
        print(f"Вік: {age}")
    except ValueError as e:
        print(e)

def process_numbers():
    numbers = []
    while len(numbers) < 3:
        try:
            n = float(input(f"Число {len(numbers)+1}: "))
            numbers.append(n)
        except ValueError:
            print("Введіть число!")
    print(f"Сума: {sum(numbers)}")

def main():
    print("Обробка виключень - варіант 7")
    
    tasks = [
        ("1. Безпечне ділення", safe_divide),
        ("2. Валідація числа", validate_number),
        ("3. Робота зі списком", process_list),
        ("4. Робота зі словником", dictionary_access),
        ("5. Калькулятор", calculator),
        ("6. Робота з файлами", file_operations),
        ("7. Множинні виключення", multiple_exceptions),
        ("8. Обчислення середнього", average_calculation),
        ("9. Повторний ввід", retry_input),
        ("10. Вкладені try/except", nested_try),
        ("11. Без обробки виключень", without_exception),
        ("12. З обробкою виключень", with_exception),
        ("13. Ділення на нуль", divide_zero),
        ("14. Рядок у ціле", string_to_int),
        ("15. Елемент списку", list_by_index),
        ("16. Значення словника", dict_by_key),
        ("17. Калькулятор розширений", calculator_extended),
        ("18. Блок else", else_block),
        ("19. Блок finally", finally_block),
        ("20. Відкриття файлу", open_user_file),
        ("21. Перевірка прав", permission_check),
        ("22. Декілька помилок", multiple_in_one),
        ("23. Всі помилки", catch_all),
        ("24. Помилка типу", custom_type_error),
        ("25. Валідація середнього", average_validation),
        ("26. Безпечне перетворення", safe_convert),
        ("27. Повтор до успіху", repeat_until_valid),
        ("28. Перетворення списку", convert_list_items),
        ("29. Вкладені виключення", nested_exceptions),
        ("30. Розділення помилок", separate_errors),
        ("31. Приклад падіння", crash_example),
        ("32. Стабільна версія", safe_crash_example),
        ("33. Читання конфігурації", read_config),
        ("34. Симуляція бази даних", database_simulation),
        ("35. Помилка ОС", handle_os_error),
        ("36. Перевірка віку", check_age),
        ("37. Обробка чисел", process_numbers)
    ]
    
    for i, (name, func) in enumerate(tasks, 1):
        print(f"\n{'-'*50}")
        print(f"Завдання {i}: {name}")
        print(f"{'-'*50}")
        try:
            func()
        except Exception as e:
            print(f"Помилка виконання: {e}")

if __name__ == "__main__":
    main()