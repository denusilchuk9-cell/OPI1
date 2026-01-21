print("=== ЗАВДАННЯ 1: ТИПИ ДАНИХ ===\n")

# 1. Оголошення змінних різних типів
# Цілі числа (int)
age = 20
students_count = 30
temperature = -5

# Дробові числа (float)
price = 19.99
pi_value = 3.14159
average_score = 85.5

# Рядки (string)
name = "Анна"
course = "Програмування"
message = "Hello, World!"

# Булеві значення (bool)
is_student = True
has_passed = False
is_raining = True

# 2. Виведення значень та їх типів
print("1. ЦІЛІ ЧИСЛА:")
print(f"   Вік: {age} (тип: {type(age)})")
print(f"   Кількість студентів: {students_count} (тип: {type(students_count)})")
print(f"   Температура: {temperature} (тип: {type(temperature)})")

print("\n2. ДРОБОВІ ЧИСЛА:")
print(f"   Ціна: {price} (тип: {type(price)})")
print(f"   Число Пі: {pi_value} (тип: {type(pi_value)})")
print(f"   Середній бал: {average_score} (тип: {type(average_score)})")

print("\n3. РЯДКИ:")
print(f"   Ім'я: {name} (тип: {type(name)})")
print(f"   Курс: {course} (тип: {type(course)})")
print(f"   Повідомлення: {message} (тип: {type(message)})")

print("\n4. БУЛЕВІ ЗНАЧЕННЯ:")
print(f"   Студент: {is_student} (тип: {type(is_student)})")
print(f"   Складено іспит: {has_passed} (тип: {type(has_passed)})")
print(f"   Йде дощ: {is_raining} (тип: {type(is_raining)})")

# 3. Введення даних від користувача
print("\n" + "="*50)
print("ВВЕДЕННЯ ДАНИХ ВІД КОРИСТУВАЧА")

# Введення різних типів даних
user_name = input("Введіть ваше ім'я: ")
user_age = int(input("Введіть ваш вік: "))
user_height = float(input("Введіть ваш зріст (у метрах): "))
user_is_student = input("Ви студент? (так/ні): ").lower() == "так"

# Виведення введених даних
print("\nВВЕДЕНІ ДАНІ:")
print(f"   Ім'я: {user_name} (тип: {type(user_name)})")
print(f"   Вік: {user_age} (тип: {type(user_age)})")
print(f"   Зріст: {user_height} м (тип: {type(user_height)})")
print(f"   Студент: {user_is_student} (тип: {type(user_is_student)})")

print("\n" + "="*50)