import random
import math

def demo_creation():
    print("\n" + "="*60)
    print("1. СТВОРЕННЯ СПИСКІВ ТА КОРТЕЖІВ")
    print("="*60)
    
    print("\n--- Створення списків ---")
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    nested = [[1, 2], [3, 4], [5, 6]]
    print(f"numbers = {numbers}")
    print(f"mixed = {mixed}")
    print(f"nested = {nested}")
    
    print("\n--- Створення кортежів ---")
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = ("apple", "banana", "cherry")
    tuple3 = (1, "text", 3.14, True)
    print(f"tuple1 = {tuple1}")
    print(f"tuple2 = {tuple2}")
    print(f"tuple3 = {tuple3}")
    
    print("\n--- Операції зі списками ---")
    numbers.append(6)
    print(f"Додали 6: {numbers}")
    numbers.insert(2, 99)
    print(f"Вставили 99 на позицію 2: {numbers}")
    numbers.remove(99)
    print(f"Видалили 99: {numbers}")
    popped = numbers.pop()
    print(f"Видалили останній елемент: {numbers}, видалений: {popped}")
    numbers[0] = 100
    print(f"Змінили перший елемент на 100: {numbers}")
    
    print("\n--- Операції з кортежами ---")
    print("Кортежі є незмінними, тому операції зміни недоступні")
    new_tuple = tuple1 + tuple2
    print(f"Конкатенація: {new_tuple}")
    
    print("\n--- Конвертація ---")
    list_to_tuple = tuple(numbers)
    tuple_to_list = list(tuple1)
    print(f"Список у кортеж: {list_to_tuple}")
    print(f"Кортеж у список: {tuple_to_list}")

def demo_indexing_slicing():
    print("\n" + "="*60)
    print("2. ІНДЕКСАЦІЯ ТА ЗРІЗИ")
    print("="*60)
    
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    tup = ("a", "b", "c", "d", "e", "f", "g", "h")
    
    print(f"\nСписок: {data}")
    print(f"Кортеж: {tup}")
    
    print("\n--- Пряма індексація ---")
    print(f"data[0] = {data[0]}")
    print(f"data[4] = {data[4]}")
    print(f"tup[2] = {tup[2]}")
    
    print("\n--- Негативна індексація ---")
    print(f"data[-1] = {data[-1]}")
    print(f"data[-3] = {data[-3]}")
    print(f"tup[-2] = {tup[-2]}")
    
    print("\n--- Зрізи (slicing) ---")
    print(f"data[2:6] = {data[2:6]}")
    print(f"data[:4] = {data[:4]}")
    print(f"data[5:] = {data[5:]}")
    print(f"data[::2] = {data[::2]}")
    print(f"data[::-1] = {data[::-1]}")
    print(f"tup[1:4] = {tup[1:4]}")
    
    print("\n--- Зрізи з кроком ---")
    print(f"data[1:8:2] = {data[1:8:2]}")
    print(f"data[::3] = {data[::3]}")
    
    print("\n--- Зміна через зрізи ---")
    nums = [1, 2, 3, 4, 5]
    print(f"Початковий: {nums}")
    nums[1:4] = [20, 30, 40]
    print(f"Після nums[1:4] = [20, 30, 40]: {nums}")
    nums[2:2] = [99, 88]
    print(f"Після вставки nums[2:2] = [99, 88]: {nums}")
    
    print("\n--- Багатовимірні структури ---")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"Матриця 3x3: {matrix}")
    print(f"matrix[1][2] = {matrix[1][2]}")
    print(f"matrix[0][:2] = {matrix[0][:2]}")

def demo_builtin_functions():
    print("\n" + "="*60)
    print("3. ВБУДОВАНІ ФУНКЦІЇ ТА МЕТОДИ")
    print("="*60)
    
    numbers = [45, 12, 89, 34, 67, 23, 78]
    words = ["яблуко", "банан", "вишня", "диня", "апельсин"]
    mixed = [3, 1, 4, 1, 5, 9, 2]
    
    print(f"\nСписок чисел: {numbers}")
    print(f"Список слів: {words}")
    print(f"Змішаний список: {mixed}")
    
    print("\n--- Основні вбудовані функції ---")
    print(f"len(numbers) = {len(numbers)}")
    print(f"sum(numbers) = {sum(numbers)}")
    print(f"min(numbers) = {min(numbers)}")
    print(f"max(numbers) = {max(numbers)}")
    print(f"sorted(numbers) = {sorted(numbers)}")
    print(f"sorted(words) = {sorted(words)}")
    
    print("\n--- Методи списків ---")
    nums = [1, 2, 3, 4, 5]
    nums.append(6)
    print(f"Після append(6): {nums}")
    nums.extend([7, 8, 9])
    print(f"Після extend([7,8,9]): {nums}")
    nums.insert(0, 0)
    print(f"Після insert(0, 0): {nums}")
    nums.remove(3)
    print(f"Після remove(3): {nums}")
    popped = nums.pop()
    print(f"Після pop(): {nums}, видалений: {popped}")
    count = nums.count(2)
    print(f"count(2) = {count}")
    nums.reverse()
    print(f"Після reverse(): {nums}")
    nums.sort()
    print(f"Після sort(): {nums}")
    copy_nums = nums.copy()
    print(f"Копія списку: {copy_nums}")
    nums.clear()
    print(f"Після clear(): {nums}")
    
    print("\n--- Операції з кортежами ---")
    tup = (1, 2, 3, 2, 4, 2, 5)
    print(f"Кортеж: {tup}")
    print(f"tup.count(2) = {tup.count(2)}")
    print(f"tup.index(4) = {tup.index(4)}")

def demo_list_comprehensions():
    print("\n" + "="*60)
    print("4. СПИСКОВІ ВКЛЮЧЕННЯ")
    print("="*60)
    
    print("\n--- Базові спискові включення ---")
    squares = [x**2 for x in range(1, 11)]
    print(f"Квадрати чисел 1-10: {squares}")
    
    even_numbers = [x for x in range(1, 21) if x % 2 == 0]
    print(f"Парні числа 1-20: {even_numbers}")
    
    words = ["apple", "banana", "cherry", "date"]
    lengths = [len(word) for word in words]
    print(f"Довжини слів {words}: {lengths}")
    
    print("\n--- Спискові включення з умовами ---")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered = [x for x in numbers if x > 5]
    print(f"Числа більше 5: {filtered}")
    
    transformed = [x**2 if x % 2 == 0 else x**3 for x in numbers]
    print(f"Квадрат парних, куб непарних: {transformed}")
    
    print("\n--- Вкладені спискові включення ---")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Матриця {matrix}")
    print(f"Сплощений список: {flattened}")
    
    pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
    print(f"Усі пари (x,y) для x,y=1..3: {pairs}")
    
    print("\n--- Словникові та множинні включення ---")
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"Словник квадратів: {squares_dict}")
    
    even_set = {x for x in range(10) if x % 2 == 0}
    print(f"Множина парних чисел: {even_set}")

def demo_functions_methods():
    print("\n" + "="*60)
    print("5. ФУНКЦІЇ ДЛЯ РОБОТИ ЗІ СПИСКАМИ")
    print("="*60)
    
    def find_max_min(lst):
        if not lst:
            return None, None
        return max(lst), min(lst)
    
    def calculate_average(lst):
        if not lst:
            return 0
        return sum(lst) / len(lst)
    
    def remove_duplicates(lst):
        seen = []
        result = []
        for item in lst:
            if item not in seen:
                seen.append(item)
                result.append(item)
        return result
    
    def flatten_list(nested_list):
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(flatten_list(item))
            else:
                result.append(item)
        return result
    
    def rotate_list(lst, k):
        if not lst:
            return []
        k = k % len(lst)
        return lst[-k:] + lst[:-k]
    
    numbers = [5, 2, 8, 1, 9, 2, 5, 7]
    nested = [[1, 2], [3, [4, 5]], 6, [7, 8]]
    
    print(f"\nПочатковий список: {numbers}")
    max_val, min_val = find_max_min(numbers)
    print(f"Максимум: {max_val}, Мінімум: {min_val}")
    
    avg = calculate_average(numbers)
    print(f"Середнє значення: {avg:.2f}")
    
    unique = remove_duplicates(numbers)
    print(f"Список без дублікатів: {unique}")
    
    print(f"\nВкладений список: {nested}")
    flat = flatten_list(nested)
    print(f"Сплощений список: {flat}")
    
    rotated = rotate_list(numbers, 3)
    print(f"Обернений на 3 позиції: {rotated}")
    
    print("\n--- Сортування ---")
    words = ["яблуко", "Банан", "вишня", "диня"]
    print(f"Слова: {words}")
    words.sort()
    print(f"Після sort(): {words}")
    words.sort(key=lambda x: len(x))
    print(f"Сортування за довжиною: {words}")
    words.sort(key=str.lower)
    print(f"Сортування без урахування регістру: {words}")

def demo_practical_problems():
    print("\n" + "="*60)
    print("6. ПРАКТИЧНІ ЗАДАЧІ")
    print("="*60)
    
    def task1_merge_sorted_lists(list1, list2):
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result
    
    def task2_find_common_elements(list1, list2):
        return list(set(list1) & set(list2))
    
    def task3_list_to_dict(lst):
        result = {}
        for i, value in enumerate(lst):
            result[i] = value
        return result
    
    def task4_matrix_transpose(matrix):
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    def task5_rotate_matrix(matrix):
        return [[matrix[j][i] for j in range(len(matrix)-1, -1, -1)] 
                for i in range(len(matrix[0]))]
    
    print("\n--- Задача 1: Об'єднання відсортованих списків ---")
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    merged = task1_merge_sorted_lists(list1, list2)
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")
    print(f"Об'єднаний: {merged}")
    
    print("\n--- Задача 2: Спільні елементи ---")
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 6, 7, 8]
    common = task2_find_common_elements(a, b)
    print(f"Список A: {a}")
    print(f"Список B: {b}")
    print(f"Спільні елементи: {common}")
    
    print("\n--- Задача 3: Список у словник ---")
    lst = ["a", "b", "c", "d"]
    dct = task3_list_to_dict(lst)
    print(f"Список: {lst}")
    print(f"Словник: {dct}")
    
    print("\n--- Задача 4: Транспонування матриці ---")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = task4_matrix_transpose(matrix)
    print(f"Матриця: {matrix}")
    print(f"Транспонована: {transposed}")
    
    print("\n--- Задача 5: Обертання матриці ---")
    rotated = task5_rotate_matrix(matrix)
    print(f"Матриця: {matrix}")
    print(f"Обернута на 90°: {rotated}")
    
    print("\n--- Задача 6: Обробка студентів ---")
    students = [
        ("Іван", "Петров", 4.5),
        ("Марія", "Іваненко", 4.8),
        ("Петро", "Сидоров", 3.9),
        ("Олена", "Коваль", 4.2)
    ]
    
    top_students = [f"{name} {surname}" for name, surname, grade in students if grade > 4.0]
    print(f"Всі студенти: {students}")
    print(f"Студенти з середнім балом > 4.0: {top_students}")