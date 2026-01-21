print("=== ЗАВДАННЯ 3: УМОВНІ ВИРАЗИ ===\n")

# 1. Простий if
print("1. ПРОСТИЙ IF:")
number = 10

if number > 0:
    print(f"   Число {number} є додатним")

# 2. if-else
print("\n2. IF-ELSE:")
temperature = 25

if temperature > 30:
    print(f"   Температура {temperature}°C: гарячо")
else:
    print(f"   Температура {temperature}°C: комфортно")

# 3. if-elif-else
print("\n3. IF-ELIF-ELSE:")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"   Бал: {score}, Оцінка: {grade}")

# 4. Вкладений if
print("\n4. ВКЛАДЕНИЙ IF:")
age = 17
has_permission = True

if age >= 18:
    print("   Доступ дозволено")
else:
    if has_permission:
        print("   Доступ дозволено з дозволу батьків")
    else:
        print("   Доступ заборонено")

# 5. switch (реалізація через match у Python 3.10+)
print("\n5. SWITCH (MATCH):")

day_number = 3

match day_number:
    case 1:
        day_name = "Понеділок"
    case 2:
        day_name = "Вівторок"
    case 3:
        day_name = "Середа"
    case 4:
        day_name = "Четвер"
    case 5:
        day_name = "П'ятниця"
    case 6:
        day_name = "Субота"
    case 7:
        day_name = "Неділя"
    case _:
        day_name = "Невідомий день"

print(f"   День номер {day_number}: {day_name}")

# 6. Практичний приклад: калькулятор
print("\n" + "="*50)
print("ПРОСТИЙ КАЛЬКУЛЯТОР")

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Виберіть операцію (+, -, *, /): ")

result = 0

if operation == "+":
    result = num1 + num2
    print(f"   Результат: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"   Результат: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"   Результат: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"   Результат: {num1} / {num2} = {result}")
    else:
        print("   Помилка: ділення на нуль!")
else:
    print("   Помилка: невідома операція!")

# 7. Практичний приклад: перевірка пароля
print("\n" + "="*50)
print("ПЕРЕВІРКА ПАРОЛЯ")

correct_password = "password123"
entered_password = input("Введіть пароль: ")

if entered_password == correct_password:
    print("   Пароль вірний! Доступ дозволено.")
else:
    print("   Пароль невірний! Спробуйте ще раз.")