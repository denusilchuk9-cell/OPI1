print("=== ЗАВДАННЯ 2: ОПЕРАТОРИ ===\n")

# 1. Математичні оператори
print("1. МАТЕМАТИЧНІ ОПЕРАТОРИ:")
a = 15
b = 4

print(f"   a = {a}, b = {b}")
print(f"   Додавання: {a} + {b} = {a + b}")
print(f"   Віднімання: {a} - {b} = {a - b}")
print(f"   Множення: {a} * {b} = {a * b}")
print(f"   Ділення: {a} / {b} = {a / b}")
print(f"   Цілочисельне ділення: {a} // {b} = {a // b}")
print(f"   Залишок від ділення: {a} % {b} = {a % b}")
print(f"   Піднесення до степеня: {a} ** {b} = {a ** b}")

# 2. Оператори порівняння
print("\n2. ОПЕРАТОРИ ПОРІВНЯННЯ:")
x = 10
y = 20

print(f"   x = {x}, y = {y}")
print(f"   Більше: {x} > {y} = {x > y}")
print(f"   Менше: {x} < {y} = {x < y}")
print(f"   Дорівнює: {x} == {y} = {x == y}")
print(f"   Не дорівнює: {x} != {y} = {x != y}")
print(f"   Більше або дорівнює: {x} >= {y} = {x >= y}")
print(f"   Менше або дорівнює: {x} <= {y} = {x <= y}")

# 3. Логічні оператори
print("\n3. ЛОГІЧНІ ОПЕРАТОРИ:")
p = True
q = False

print(f"   p = {p}, q = {q}")
print(f"   Логічне І (and): {p} and {q} = {p and q}")
print(f"   Логічне АБО (or): {p} or {q} = {p or q}")
print(f"   Заперечення (not): not {p} = {not p}")

# 4. Складні умови
print("\n4. СКЛАДНІ УМОВИ:")

age = 19
has_license = True
has_experience = False

print(f"   Вік: {age}")
print(f"   Має права: {has_license}")
print(f"   Має досвід: {has_experience}")

# Перевірка, чи може особа керувати авто
can_drive = age >= 18 and has_license
print(f"   Може керувати авто: {can_drive}")

# Перевірка, чи потребує нагляду
requires_supervision = age >= 16 and age < 18 or (age >= 18 and not has_experience)
print(f"   Потребує нагляду: {requires_supervision}")

# 5. Практичні приклади
print("\n5. ПРАКТИЧНІ ПРИКЛАДИ:")

# Перевірка парності числа
number = 7
is_even = number % 2 == 0
print(f"   Число {number} парне: {is_even}")

# Перевірка діапазону
score = 85
is_excellent = score >= 90
is_good = score >= 75 and score < 90
print(f"   Бал {score} є відмінним: {is_excellent}")
print(f"   Бал {score} є хорошим: {is_good}")

# 6. Введення від користувача
print("\n" + "="*50)
print("ПЕРЕВІРКА ЧИСЛА ВВІДУ КОРИСТУВАЧА")

user_number = int(input("Введіть ціле число: "))

# Перевірки
print(f"\nАНАЛІЗ ЧИСЛА {user_number}:")
print(f"   Парне: {user_number % 2 == 0}")
print(f"   Додатне: {user_number > 0}")
print(f"   Кратне 5: {user_number % 5 == 0}")
print(f"   У діапазоні 1-100: {user_number >= 1 and user_number <= 100}")