print("=== ЗАВДАННЯ 5: ВВЕДЕННЯ ТА ОБРОБКА ДАНИХ ===\n")

# 1. Базове введення даних
print("1. БАЗОВЕ ВВЕДЕННЯ:")

# Введення рядка
name = input("Введіть ваше ім'я: ")
print(f"   Привіт, {name}!")

# Введення числа
age = input("Введіть ваш вік: ")
# Перевірка, чи введено число
if age.isdigit():
    age = int(age)
    print(f"   Вам {age} років")
else:
    print("   Помилка: вік має бути числом!")

# 2. Обробка різних типів даних
print("\n2. ОБРОБКА РІЗНИХ ТИПІВ:")

# Введення дробового числа
height = input("Введіть ваш зріст (у метрах): ")
try:
    height = float(height)
    print(f"   Ваш зріст: {height} м")
except ValueError:
    print("   Помилка: некоректний формат числа!")

# Введення булевого значення
student_input = input("Ви студент? (так/ні): ")
is_student = student_input.lower() == "так"
print(f"   Статус студента: {is_student}")

# 3. Практичний приклад: калькулятор з перевірками
print("\n" + "="*50)
print("РОЗШИРЕНИЙ КАЛЬКУЛЯТОР")

def get_number(prompt):
    """Функція для безпечного введення числа"""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Помилка! Будь ласка, введіть число.")

def get_operation():
    """Функція для введення операції"""
    while True:
        op = input("Виберіть операцію (+, -, *, /): ")
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("Помилка! Оберіть одну з операцій: +, -, *, /")

# Отримання даних від користувача
num1 = get_number("Введіть перше число: ")
num2 = get_number("Введіть друге число: ")
operation = get_operation()

# Виконання обчислення
if operation == "+":
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Помилка: ділення на нуль!")

# 4. Практичний приклад: система реєстрації
print("\n" + "="*50)
print("СИСТЕМА РЕЄСТРАЦІЇ КОРИСТУВАЧА")

print("Заповніть форму реєстрації:")
username = input("Ім'я користувача: ")
email = input("Електронна пошта: ")
password = input("Пароль: ")
confirm_password = input("Підтвердіть пароль: ")

# Перевірка введених даних
errors = []

if len(username) < 3:
    errors.append("Ім'я користувача занадто коротке (мінімум 3 символи)")

if "@" not in email or "." not in email:
    errors.append("Некоректна електронна пошта")

if len(password) < 6:
    errors.append("Пароль занадто короткий (мінімум 6 символів)")

if password != confirm_password:
    errors.append("Паролі не співпадають")

# Виведення результатів
if len(errors) == 0:
    print("\n✅ Реєстрація успішна!")
    print(f"   Ім'я: {username}")
    print(f"   Email: {email}")
else:
    print("\n❌ Помилки реєстрації:")
    for error in errors:
        print(f"   - {error}")

# 5. Практичний приклад: опитування
print("\n" + "="*50)
print("ОПИТУВАННЯ ПРО ЗДОРОВИЙ СПОСІБ ЖИТТЯ")

questions = [
    "Скільки годин ви спите вночі? ",
    "Скільки склянок води випиваєте за день? ",
    "Скільки хвилин фізичних вправ робите щодня? "
]

answers = []
for question in questions:
    while True:
        answer = input(question)
        if answer.isdigit():
            answers.append(int(answer))
            break
        else:
            print("Будь ласка, введіть число!")

# Аналіз відповідей
sleep_hours, water_glasses, exercise_minutes = answers

print("\nРЕЗУЛЬТАТИ ОПИТУВАННЯ:")

if sleep_hours >= 7 and sleep_hours <= 9:
    print("✅ Відпочинок: оптимальна тривалість сну")
elif sleep_hours < 7:
    print("⚠️ Відпочинок: недостатньо сну")
else:
    print("⚠️ Відпочинок: занадто багато сну")

if water_glasses >= 8:
    print("✅ Гідратація: достатньо води")
else:
    print("⚠️ Гідратація: потрібно пити більше води")

if exercise_minutes >= 30:
    print("✅ Активність: достатньо фізичних вправ")
else:
    print("⚠️ Активність: потрібно більше рухатися")

# Загальна оцінка
score = 0
if 7 <= sleep_hours <= 9:
    score += 1
if water_glasses >= 8:
    score += 1
if exercise_minutes >= 30:
    score += 1

print(f"\nЗАГАЛЬНА ОЦІНКА: {score}/3")
if score == 3:
    print("Відмінно! Ви ведете здоровий спосіб життя!")
elif score == 2:
    print("Добре! Але є простір для покращення.")
else:
    print("Потрібно уважніше ставитися до здоров'я.")