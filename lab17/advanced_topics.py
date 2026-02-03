"""
Файл 4: Розширені теми - конфлікти, складність, оптимізація
"""

print("=" * 50)
print("РОЗШИРЕНІ ТЕМИ: КОНФЛІКТИ ТА СКЛАДНІСТЬ")
print("=" * 50)

# 1. Конфлікти у словниках
print("\n1. КОНФЛІКТИ У СЛОВНИКАХ")

# Приклад потенційного конфлікту: перезапис значення
print("Конфлікт через перезапис значення:")
data = {}

# Перший запис
data["key"] = "перше значення"
print(f"Після першого запису: {data}")

# Другий запис з тим самим ключем (конфлікт!)
data["key"] = "друге значення"
print(f"Після другого запису (перезапис): {data}")

# Рішення: перевірка перед записом
print("\nРішення конфлікту - перевірка перед записом:")
data = {"existing_key": "початкове значення"}

new_key = "existing_key"
new_value = "нове значення"

if new_key in data:
    print(f"Ключ '{new_key}' вже існує! Поточне значення: '{data[new_key]}'")
    # Запитати користувача, що робити
    response = "skip"  # Може бути "overwrite" або "merge"
    
    if response == "overwrite":
        data[new_key] = new_value
        print(f"Значення перезаписано: '{data[new_key]}'")
    elif response == "merge":
        # Якщо значення - списки, їх можна об'єднати
        if isinstance(data[new_key], list) and isinstance(new_value, list):
            data[new_key].extend(new_value)
            print(f"Списки об'єднано: {data[new_key]}")
        else:
            print("Неможливо об'єднати несумісні типи даних")
    else:
        print("Значення не змінено")
else:
    data[new_key] = new_value
    print(f"Додано новий ключ: '{new_key}' = '{new_value}'")

# 2. Колізії хеш-функцій
print("\n2. КОЛІЗІЇ ХЕШ-ФУНКЦІЙ")

# Демонстрація хеш-значень
print("Хеш-значення для різних об'єктів:")
print(f"  Хеш для 'hello': {hash('hello')}")
print(f"  Хеш для 123: {hash(123)}")
print(f"  Хеш для 3.14: {hash(3.14)}")

# Важливо: не всі об'єкти можуть бути ключами
try:
    # Список не може бути ключем (нехешований тип)
    invalid_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"\nПомилка при спробі використати список як ключ: {e}")

# Кортеж може бути ключем, якщо всі його елементи незмінні
valid_dict = {(1, 2, 3): "кортеж як ключ"}
print(f"\nСловник з кортежем як ключем: {valid_dict}")

# 3. Часова складність операцій
print("\n3. ЧАСОВА СКЛАДНІСТЬ ОПЕРАЦІЙ")

print("Асимптотична складність для множин та словників:")
print("""
| Операція          | Множини | Словники | Примітки                          |
|-------------------|---------|----------|-----------------------------------|
| Пошук (in)        | O(1)    | O(1)     | В середньому                      |
| Вставка           | O(1)    | O(1)     | В середньому                      |
| Видалення         | O(1)    | O(1)     | В середньому                      |
| Об'єднання        | O(n+m)  | -        | Де n, m - розміри множин          |
| Перетин           | O(min(n,m)) | -     | Залежить від реалізації           |
| Копіювання        | O(n)    | O(n)     | Лінійна залежність від розміру    |
| Ітерація          | O(n)    | O(n)     | Лінійна залежність від розміру    |
""")

# 4. Практичне порівняння продуктивності
print("\n4. ПРАКТИЧНЕ ПОРІВНЯННЯ ПРОДУКТИВНОСТІ")

import time

def measure_performance():
    """Функція для вимірювання продуктивності операцій"""
    
    # Створення великих структур даних
    size = 10000
    test_list = list(range(size))
    test_set = set(range(size))
    test_dict = {i: f"value_{i}" for i in range(size)}
    
    print(f"Розмір структур: {size} елементів")
    
    # Тест пошуку елемента
    print("\nПошук елемента:")
    
    # Пошук у списку
    start = time.time()
    _ = size-1 in test_list  # Пошук останнього елемента
    list_time = time.time() - start
    
    # Пошук у множині
    start = time.time()
    _ = size-1 in test_set
    set_time = time.time() - start
    
    # Пошук у словнику (за ключем)
    start = time.time()
    _ = size-1 in test_dict
    dict_time = time.time() - start
    
    print(f"  Список: {list_time:.6f} сек")
    print(f"  Множина: {set_time:.6f} сек")
    print(f"  Словник: {dict_time:.6f} сек")
    
    # Тест видалення елемента
    print("\nВидалення елемента (середнього):")
    
    # Для списку - видалення з середини
    mid = size // 2
    list_copy = test_list.copy()
    
    start = time.time()
    list_copy.pop(mid)  # O(n) операція для списку
    list_remove_time = time.time() - start
    
    # Для множини
    set_copy = test_set.copy()
    
    start = time.time()
    set_copy.discard(mid)  # O(1) операція в середньому
    set_remove_time = time.time() - start
    
    # Для словника
    dict_copy = test_dict.copy()
    
    start = time.time()
    dict_copy.pop(mid)  # O(1) операція в середньому
    dict_remove_time = time.time() - start
    
    print(f"  Список: {list_remove_time:.6f} сек")
    print(f"  Множина: {set_remove_time:.6f} сек")
    print(f"  Словник: {dict_remove_time:.6f} сек")

# Виконати вимірювання продуктивності
measure_performance()

# 5. Оптимізація з використанням множин
print("\n5. ОПТИМІЗАЦІЯ ЗА ДОПОМОГОЮ МНОЖИН")

# Приклад: швидкий пошук спільних друзів у соціальній мережі
def find_common_friends_optimized(user1_friends, user2_friends):
    """Оптимізована версія пошуку спільних друзів"""
    # Конвертуємо списки у множини для швидкого перетину
    set1 = set(user1_friends)
    set2 = set(user2_friends)
    
    # Знаходимо перетин множин
    return set1 & set2

# Приклад: швидка перевірка наявності елементів
def filter_allowed_items(all_items, allowed_set):
    """Фільтрація елементів з використанням множини для швидкої перевірки"""
    return [item for item in all_items if item in allowed_set]

# Демонстрація
print("\nПриклад оптимізації:")
all_products = ["apple", "banana", "orange", "grape", "kiwi", "mango", "pear"]
available_products = {"apple", "orange", "kiwi", "pear"}

filtered = filter_allowed_items(all_products, available_products)
print(f"Всі продукти: {all_products}")
print(f"Доступні продукти: {available_products}")
print(f"Відфільтровані продукти: {filtered}")

print("\n" + "=" * 50)
print("РОЗШИРЕНІ ТЕМИ ЗАВЕРШЕНІ")
print("=" * 50)