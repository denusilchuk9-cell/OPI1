"""
Файл 1: Демонстрація роботи з множинами (sets) в Python
Містить створення множин, операції над ними та основні методи
"""

print("=" * 50)
print("ДЕМОНСТРАЦІЯ РОБОТИ З МНОЖИНАМИ")
print("=" * 50)

# 1. Створення множин з різноманітними типами даних
print("\n1. Створення множин:")

# Множина з цілими числами
numbers_set = {1, 2, 3, 4, 5}
print(f"Множина чисел: {numbers_set}")

# Множина з рядків
fruits_set = {"apple", "banana", "orange", "kiwi"}
print(f"Множина фруктів: {fruits_set}")

# Множина з різних типів даних
mixed_set = {1, "hello", 3.14, True, (1, 2, 3)}  # Примітка: список не може бути в множині
print(f"Змішана множина: {mixed_set}")

# Створення множини зі списку (видаляє дублікати)
duplicates_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_set = set(duplicates_list)
print(f"Множина зі списку (без дублікатів): {unique_set}")

# 2. Операції над множинами
print("\n2. Операції над множинами:")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Множина A: {set_a}")
print(f"Множина B: {set_b}")

# Об'єднання (union)
union_set = set_a.union(set_b)
print(f"Об'єднання A ∪ B: {union_set}")
print(f"Альтернативний спосіб (|): {set_a | set_b}")

# Перетин (intersection)
intersection_set = set_a.intersection(set_b)
print(f"\nПеретин A ∩ B: {intersection_set}")
print(f"Альтернативний спосіб (&): {set_a & set_b}")

# Різниця (difference)
difference_set = set_a.difference(set_b)
print(f"\nРізниця A - B: {difference_set}")
print(f"Альтернативний спосіб (-): {set_a - set_b}")

# Симетрична різниця (symmetric difference)
symmetric_diff_set = set_a.symmetric_difference(set_b)
print(f"\nСиметрична різниця A Δ B: {symmetric_diff_set}")
print(f"Альтернативний спосіб (^): {set_a ^ set_b}")

# 3. Модифікація множин
print("\n3. Модифікація множин:")

# Створення множини для модифікації
my_set = {1, 2, 3, 4}
print(f"Початкова множина: {my_set}")

# Додавання елементів
my_set.add(5)
print(f"Після додавання 5: {my_set}")

my_set.update([6, 7, 8])
print(f"Після додавання [6, 7, 8]: {my_set}")

# Видалення елементів
my_set.remove(4)  # Викидає помилку, якщо елемент не існує
print(f"Після видалення 4: {my_set}")

my_set.discard(10)  # Не викидає помилку, якщо елемент не існує
print(f"Після спроби видалити 10 (не існує): {my_set}")

popped_element = my_set.pop()  # Видаляє і повертає випадковий елемент
print(f"Видалено випадковий елемент: {popped_element}")
print(f"Множина після pop: {my_set}")

# Очищення множини
my_set.clear()
print(f"Після очищення: {my_set}")

# 4. Використання вбудованих функцій
print("\n4. Вбудовані функції для множин:")

sample_set = {10, 20, 30, 40, 50}
print(f"Тестова множина: {sample_set}")

# len() - кількість елементів
print(f"Кількість елементів (len): {len(sample_set)}")

# sum() - сума елементів (для числових множин)
print(f"Сума елементів (sum): {sum(sample_set)}")

# max() та min()
print(f"Максимальний елемент: {max(sample_set)}")
print(f"Мінімальний елемент: {min(sample_set)}")

# sorted() - повертає відсортований список
print(f"Відсортована множина (як список): {sorted(sample_set)}")

# 5. Перевірка належності
print("\n5. Перевірка належності:")

check_set = {1, 2, 3, 4, 5}
print(f"Множина: {check_set}")
print(f"Чи належить 3 множині? {3 in check_set}")
print(f"Чи не належить 10 множині? {10 not in check_set}")

# 6. Підмножини та надмножини
print("\n6. Підмножини та надмножини:")

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {2, 3, 6}

print(f"X = {set_x}")
print(f"Y = {set_y}")
print(f"Z = {set_z}")

print(f"X є підмножиною Y? {set_x.issubset(set_y)}")
print(f"Y є надмножиною X? {set_y.issuperset(set_x)}")
print(f"X і Z мають спільні елементи? {not set_x.isdisjoint(set_z)}")
print(f"X і {10, 11} не мають спільних елементів? {set_x.isdisjoint({10, 11})}")

print("\n" + "=" * 50)
print("РОБОТА З МНОЖИНАМИ ЗАВЕРШЕНА")
print("=" * 50)