"""
Файл 2: Демонстрація роботи з словниками (dictionaries) в Python
Містить створення словників, операції над ними та основні методи
"""

print("=" * 50)
print("ДЕМОНСТРАЦІЯ РОБОТИ З СЛОВНИКАМИ")
print("=" * 50)

# 1. Створення словників з різноманітними типами даних
print("\n1. Створення словників:")

# Простий словник студентів (ім'я: оцінка)
students = {
    "Іван Петренко": 85,
    "Марія Коваль": 92,
    "Олексій Сидоренко": 78,
    "Анна Бойко": 95
}
print(f"Словник студентів: {students}")

# Словник з різними типами даних як значення
employee = {
    "ім'я": "Олег Василенко",
    "вік": 35,
    "посада": "розробник",
    "навички": ["Python", "JavaScript", "SQL"],
    "активний": True,
    "зарплата": 45000.50
}
print(f"\nСловник співробітника: {employee}")

# Вкладений словник
company = {
    "назва": "Tech Solutions",
    "заснована": 2010,
    "співробітники": {
        "розробники": 15,
        "менеджери": 5,
        "дизайнери": 3
    },
    "локації": ["Київ", "Львів", "Одеса"]
}
print(f"\nВкладений словник компанії: {company}")

# Створення словника за допомогою dict()
new_dict = dict(name="Test", value=123)
print(f"\nСловник створений через dict(): {new_dict}")

# 2. Доступ до значень словника
print("\n2. Доступ до значень словника:")

# Доступ за ключем
print(f"Оцінка Івана Петренка: {students['Іван Петренко']}")
print(f"Посада співробітника: {employee['посада']}")
print(f"Кількість розробників у компанії: {company['співробітники']['розробники']}")

# Безпечний доступ через get() - не викликає помилку при відсутності ключа
print(f"\nОцінка неіснуючого студента (get): {students.get('Неіснуючий Студент')}")
print(f"Оцінка неіснуючого студента з значенням за замовчуванням: {students.get('Неіснуючий Студент', 'Не знайдено')}")

# 3. Модифікація словників
print("\n3. Модифікація словників:")

# Створення копії для модифікації
student_grades = students.copy()
print(f"Початковий словник оцінок: {student_grades}")

# Додавання нового елемента
student_grades["Наталія Шевченко"] = 88
print(f"Після додавання нового студента: {student_grades}")

# Оновлення значення
student_grades["Олексій Сидоренко"] = 82
print(f"Після оновлення оцінки Олексія: {student_grades}")

# Оновлення декількох значень
student_grades.update({
    "Марія Коваль": 94,
    "Новий Студент": 76
})
print(f"Після оновлення декількох записів: {student_grades}")

# Видалення елементів
removed_grade = student_grades.pop("Новий Студент")
print(f"\nВидалено студента з оцінкою: {removed_grade}")
print(f"Після видалення: {student_grades}")

# Видалення останнього доданого елемента (Python 3.7+)
last_key, last_value = student_grades.popitem()
print(f"\nВидалено останній елемент: {last_key} = {last_value}")
print(f"Після popitem: {student_grades}")

# 4. Використання вбудованих функцій та методів
print("\n4. Вбудовані функції та методи словників:")

# keys(), values(), items()
print(f"Ключі словника: {list(students.keys())}")
print(f"Значення словника: {list(students.values())}")
print(f"Пари ключ-значення: {list(students.items())}")

# len() - кількість пар ключ-значення
print(f"\nКількість студентів: {len(students)}")

# Перевірка наявності ключа
print(f"\nЧи є 'Марія Коваль' у словнику? {'Марія Коваль' in students}")
print(f"Чи є 'Неіснуючий' у словнику? {'Неіснуючий' in students}")

# 5. Ітерація по словнику
print("\n5. Ітерація по словнику:")

print("Імена та оцінки студентів:")
for name, grade in students.items():
    print(f"  {name}: {grade}")

print("\nТільки імена студентів:")
for name in students.keys():
    print(f"  {name}")

print("\nТільки оцінки:")
for grade in students.values():
    print(f"  {grade}")

# 6. Створення словника зі списків
print("\n6. Створення словника зі списків:")

keys = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]

# За допомогою zip()
zipped_dict = dict(zip(keys, values))
print(f"Словник зі списків (zip): {zipped_dict}")

# Словникове включення (dictionary comprehension)
squares = {x: x**2 for x in range(1, 6)}
print(f"Словник квадратів (comprehension): {squares}")

# 7. Об'єднання словників (Python 3.9+)
print("\n7. Об'єднання словників:")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Спосіб 1: update()
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(f"Об'єднання через update(): {dict1_copy}")

# Спосіб 2: unpacking (Python 3.5+)
merged_dict = {**dict1, **dict2}
print(f"Об'єднання через unpacking: {merged_dict}")

# Спосіб 3: | оператор (Python 3.9+)
merged_dict_v3 = dict1 | dict2
print(f"Об'єднання через | оператор: {merged_dict_v3}")

print("\n" + "=" * 50)
print("РОБОТА З СЛОВНИКАМИ ЗАВЕРШЕНА")
print("=" * 50)