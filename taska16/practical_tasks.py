def show_all_tasks():
    print("\n" + "="*60)
    print("40 ПРАКТИЧНИХ ЗАВДАНЬ ПО СПИСКАМ ТА КОРТЕЖАМ")
    print("="*60)
    
    tasks = [
        ("1. Створити список чисел від 1 до 10", task_1),
        ("2. Знайти суму всіх елементів списку", task_2),
        ("3. Знайти максимальний елемент у списку", task_3),
        ("4. Знайти мінімальний елемент у списку", task_4),
        ("5. Знайти середнє значення списку", task_5),
        ("6. Перевернути список", task_6),
        ("7. Перевірити наявність елемента у списку", task_7),
        ("8. Видалити дублікати зі списку", task_8),
        ("9. Об'єднати два списки", task_9),
        ("10. Знайти спільні елементи двох списків", task_10),
        ("11. Знайти різницю двох списків", task_11),
        ("12. Перетворити список у кортеж", task_12),
        ("13. Розпакувати кортеж у змінні", task_13),
        ("14. Створити список квадратів чисел", task_14),
        ("15. Фільтрувати парні числа", task_15),
        ("16. Сортувати список за зростанням", task_16),
        ("17. Сортувати список за спаданням", task_18),
        ("18. Знайти індекс елемента", task_17),
        ("19. Порахувати кількість входжень", task_19),
        ("20. Розділити список на частини", task_20),
        ("21. Створити матрицю 3x3", task_21),
        ("22. Транспонувати матрицю", task_22),
        ("23. Знайти суму діагоналей матриці", task_23),
        ("24. Об'єднати список рядків в один рядок", task_24),
        ("25. Розділити рядок на список", task_25),
        ("26. Знайти найдовше слово у списку", task_26),
        ("27. Знайти найкоротше слово у списку", task_27),
        ("28. Порахувати довжину кожного слова", task_28),
        ("29. Фільтрувати слова за довжиною", task_29),
        ("30. Створити словник зі списку", task_30),
        ("31. Створити список зі словника", task_31),
        ("32. Порахувати частоту елементів", task_32),
        ("33. Знайти другий максимальний елемент", task_33),
        ("34. Знайти другий мінімальний елемент", task_34),
        ("35. Перевірити, чи є список відсортованим", task_35),
        ("36. Обернути кожне слово у списку", task_36),
        ("37. Знайти всі прості числа у діапазоні", task_37),
        ("38. Створити список чисел Фібоначчі", task_38),
        ("39. Кодування та декодування рядка", task_39),
        ("40. Симуляція кидків кубика", task_40),
    ]
    
    print("\nОберіть завдання для виконання (1-40):")
    print("Або введіть 'all' для виконання всіх завдань:")
    
    choice = input("Ваш вибір: ")
    
    if choice.lower() == 'all':
        for i, (description, func) in enumerate(tasks, 1):
            print(f"\n{'='*50}")
            print(f"ЗАВДАННЯ {i}: {description}")
            print('='*50)
            func()
    else:
        try:
            task_num = int(choice)
            if 1 <= task_num <= 40:
                description, func = tasks[task_num-1]
                print(f"\n{'='*50}")
                print(f"ЗАВДАННЯ {task_num}: {description}")
                print('='*50)
                func()
            else:
                print("Невірний номер завдання!")
        except ValueError:
            print("Невірний ввід!")

def task_1():
    numbers = list(range(1, 11))
    print(f"Список чисел від 1 до 10: {numbers}")

def task_2():
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"Список: {numbers}")
    print(f"Сума: {total}")

def task_3():
    numbers = [4, 2, 9, 7, 5]
    maximum = max(numbers)
    print(f"Список: {numbers}")
    print(f"Максимум: {maximum}")

def task_4():
    numbers = [4, 2, 9, 7, 5]
    minimum = min(numbers)
    print(f"Список: {numbers}")
    print(f"Мінімум: {minimum}")

def task_5():
    numbers = [4, 2, 9, 7, 5]
    average = sum(numbers) / len(numbers)
    print(f"Список: {numbers}")
    print(f"Середнє: {average:.2f}")

def task_6():
    numbers = [1, 2, 3, 4, 5]
    reversed_list = numbers[::-1]
    print(f"Оригінал: {numbers}")
    print(f"Перевернутий: {reversed_list}")

def task_7():
    fruits = ["apple", "banana", "cherry"]
    search = "banana"
    exists = search in fruits
    print(f"Список: {fruits}")
    print(f"Елемент '{search}' у списку: {exists}")

def task_8():
    numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    unique = list(set(numbers))
    print(f"Оригінал: {numbers}")
    print(f"Без дублікатів: {unique}")

def task_9():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")
    print(f"Об'єднаний: {combined}")

def task_10():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = list(set(list1) & set(list2))
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")
    print(f"Спільні елементи: {common}")

def task_11():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    difference = list(set(list1) - set(list2))
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")
    print(f"Елементи тільки в першому списку: {difference}")

def task_12():
    lst = [1, 2, 3, 4, 5]
    tup = tuple(lst)
    print(f"Список: {lst}")
    print(f"Кортеж: {tup}")
    print(f"Тип кортежу: {type(tup)}")

def task_13():
    person = ("Іван", "Петров", 25)
    name, surname, age = person
    print(f"Кортеж: {person}")
    print(f"Розпаковано: ім'я={name}, прізвище={surname}, вік={age}")

def task_14():
    squares = [x**2 for x in range(1, 6)]
    print(f"Квадрати чисел 1-5: {squares}")

def task_15():
    numbers = list(range(1, 11))
    even = [x for x in numbers if x % 2 == 0]
    print(f"Всі числа: {numbers}")
    print(f"Парні числа: {even}")

def task_16():
    numbers = [5, 2, 8, 1, 9]
    sorted_asc = sorted(numbers)
    print(f"Оригінал: {numbers}")
    print(f"Відсортовано за зростанням: {sorted_asc}")

def task_17():
    numbers = [5, 2, 8, 1, 9]
    idx = numbers.index(8)
    print(f"Список: {numbers}")
    print(f"Індекс числа 8: {idx}")

def task_18():
    numbers = [5, 2, 8, 1, 9]
    sorted_desc = sorted(numbers, reverse=True)
    print(f"Оригінал: {numbers}")
    print(f"Відсортовано за спаданням: {sorted_desc}")

def task_19():
    numbers = [1, 2, 3, 2, 4, 2, 5]
    count_2 = numbers.count(2)
    print(f"Список: {numbers}")
    print(f"Число 2 зустрічається {count_2} рази")

def task_20():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    chunk_size = 3
    chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
    print(f"Список: {numbers}")
    print(f"Розділено на частини по {chunk_size}: {chunks}")

def task_21():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Матриця 3x3:")
    for row in matrix:
        print(row)

def task_22():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print("Оригінальна матриця:")
    for row in matrix:
        print(row)
    print("\nТранспонована матриця:")
    for row in transposed:
        print(row)

def task_23():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    main_diag = sum(matrix[i][i] for i in range(len(matrix)))
    anti_diag = sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix)))
    print("Матриця:")
    for row in matrix:
        print(row)
    print(f"Сума головної діагоналі: {main_diag}")
    print(f"Сума побічної діагоналі: {anti_diag}")

def task_24():
    words = ["Hello", "world", "from", "Python"]
    sentence = " ".join(words)
    print(f"Список слів: {words}")
    print(f"Речення: {sentence}")

def task_25():
    sentence = "Hello world from Python"
    words = sentence.split()
    print(f"Речення: {sentence}")
    print(f"Список слів: {words}")

def task_26():
    words = ["apple", "banana", "kiwi", "strawberry", "orange"]
    longest = max(words, key=len)
    print(f"Список слів: {words}")
    print(f"Найдовше слово: {longest}")

def task_27():
    words = ["apple", "banana", "kiwi", "strawberry", "orange"]
    shortest = min(words, key=len)
    print(f"Список слів: {words}")
    print(f"Найкоротше слово: {shortest}")

def task_28():
    words = ["apple", "banana", "kiwi", "strawberry"]
    lengths = [len(word) for word in words]
    print(f"Слова: {words}")
    print(f"Довжини: {lengths}")

def task_29():
    words = ["apple", "banana", "kiwi", "strawberry", "pear"]
    long_words = [word for word in words if len(word) > 4]
    print(f"Всі слова: {words}")
    print(f"Слова довші за 4 символи: {long_words}")

def task_30():
    keys = ["name", "age", "city"]
    values = ["Іван", 25, "Київ"]
    person = dict(zip(keys, values))
    print(f"Ключі: {keys}")
    print(f"Значення: {values}")
    print(f"Словник: {person}")

def task_31():
    person = {"name": "Іван", "age": 25, "city": "Київ"}
    keys = list(person.keys())
    values = list(person.values())
    print(f"Словник: {person}")
    print(f"Ключі: {keys}")
    print(f"Значення: {values}")

def task_32():
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    print(f"Список: {numbers}")
    print(f"Частота: {frequency}")

def task_33():
    numbers = [5, 2, 8, 1, 9, 8]
    unique = sorted(set(numbers), reverse=True)
    second_max = unique[1] if len(unique) > 1 else None
    print(f"Список: {numbers}")
    print(f"Другий максимальний: {second_max}")

def task_34():
    numbers = [5, 2, 8, 1, 9, 1]
    unique = sorted(set(numbers))
    second_min = unique[1] if len(unique) > 1 else None
    print(f"Список: {numbers}")
    print(f"Другий мінімальний: {second_min}")

def task_35():
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [5, 3, 1, 4, 2]
    is_sorted1 = numbers1 == sorted(numbers1)
    is_sorted2 = numbers2 == sorted(numbers2)
    print(f"Список 1 {numbers1} відсортований: {is_sorted1}")
    print(f"Список 2 {numbers2} відсортований: {is_sorted2}")

def task_36():
    words = ["hello", "world", "python"]
    reversed_words = [word[::-1] for word in words]
    print(f"Оригінал: {words}")
    print(f"Обернені: {reversed_words}")

def task_37():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = [x for x in range(1, 31) if is_prime(x)]
    print(f"Прості числа від 1 до 30: {primes}")

def task_38():
    n = 10
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    print(f"Перші {n} чисел Фібоначчі: {fib}")

def task_39():
    text = "Hello Python"
    encoded = [ord(char) for char in text]
    decoded = "".join(chr(code) for code in encoded)
    print(f"Оригінал: {text}")
    print(f"Закодовано (ASCII): {encoded}")
    print(f"Декодовано: {decoded}")

def task_40():
    import random
    rolls = [random.randint(1, 6) for _ in range(10)]
    frequency = {i: rolls.count(i) for i in range(1, 7)}
    print(f"Кидання кубика (10 разів): {rolls}")
    print("Частота:")
    for num, count in frequency.items():
        print(f"  {num}: {count} разів")