print("=== ЗАВДАННЯ 4: РОБОТА ЗІ ЗМІННИМИ ===\n")

# 1. Базове присвоєння та зміна значень
print("1. БАЗОВІ ОПЕРАЦІЇ:")
counter = 0
print(f"   Початкове значення лічильника: {counter}")

# Збільшення значення
counter = counter + 1
print(f"   Після counter = counter + 1: {counter}")

# Скорочений запис
counter += 1
print(f"   Після counter += 1: {counter}")

# Інші оператори
counter -= 2
print(f"   Після counter -= 2: {counter}")

counter *= 3
print(f"   Після counter *= 3: {counter}")

counter //= 2
print(f"   Після counter //= 2: {counter}")

# 2. Зміна типів змінних
print("\n2. ЗМІНА ТИПІВ ЗМІННИХ:")
value = "10"
print(f"   Початкове значення: {value}, тип: {type(value)}")

# Перетворення рядка в число
value = int(value)
print(f"   Після int(value): {value}, тип: {type(value)}")

# Перетворення числа в рядок
value = str(value) + "0"
print(f"   Після str(value) + '0': {value}, тип: {type(value)}")

# 3. Змінні в умовах
print("\n3. ЗМІННІ В УМОВАХ:")
balance = 1000
withdrawal_amount = 500

print(f"   Початковий баланс: {balance} грн")
print(f"   Сума зняття: {withdrawal_amount} грн")

if balance >= withdrawal_amount:
    balance -= withdrawal_amount
    print(f"   Операція успішна! Новий баланс: {balance} грн")
else:
    print("   Недостатньо коштів на рахунку!")

# 4. Обмін значень між змінними
print("\n4. ОБМІН ЗНАЧЕНЬ:")
a = 5
b = 10
print(f"   До обміну: a = {a}, b = {b}")

# Традиційний спосіб з допоміжною змінною
temp = a
a = b
b = temp
print(f"   Після обміну (традиційно): a = {a}, b = {b}")

# Сучасний спосіб (Python)
a, b = b, a
print(f"   Після обміну (Python): a = {a}, b = {b}")

# 5. Практичний приклад: система нарахування балів
print("\n" + "="*50)
print("СИСТЕМА НАРАХУВАННЯ БАЛІВ")

student_points = 75
print(f"   Початкові бали студента: {student_points}")

# Нарахування балів за різні дії
attended_lecture = True
completed_homework = False
extra_activity = True

if attended_lecture:
    student_points += 10
    print("   +10 балів за відвідування лекції")

if completed_homework:
    student_points += 20
    print("   +20 балів за виконане домашнє завдання")
else:
    student_points -= 15
    print("   -15 балів за невиконане домашнє завдання")

if extra_activity:
    student_points += 5
    print("   +5 балів за додаткову активність")

print(f"   Фінальні бали студента: {student_points}")

# Визначення статусу
if student_points >= 80:
    status = "Відмінник"
elif student_points >= 60:
    status = "Добре"
else:
    status = "Потрібно покращити"

print(f"   Статус студента: {status}")

# 6. Практичний приклад: конвертер валют
print("\n" + "="*50)
print("КОНВЕРТЕР ВАЛЮТ")

exchange_rate = 36.5  # USD to UAH
amount_uah = float(input("Введіть суму в гривнях: "))

# Конвертація
amount_usd = amount_uah / exchange_rate
print(f"   {amount_uah} грн = {amount_usd:.2f} USD")

# Зміна курсу в залежності від суми
if amount_uah > 10000:
    exchange_rate = 36.7  # Кращий курс для великих сум
    amount_usd = amount_uah / exchange_rate
    print(f"   Застосовано пільговий курс!")
    print(f"   {amount_uah} грн = {amount_usd:.2f} USD")