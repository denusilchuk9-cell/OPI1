"""
Файл 3: Практичні задачі з використанням множин та словників
Демонструє реальне застосування структур даних
"""

print("=" * 50)
print("ПРАКТИЧНІ ЗАДАЧІ З МНОЖИНАМИ ТА СЛОВНИКАМИ")
print("=" * 50)

# 1. Задача: Фільтрація унікальних значень
print("\n1. ФІЛЬТРАЦІЯ УНІКАЛЬНИХ ЗНАЧЕНЬ")

# Задача: отримати унікальні слова з тексту
text = """
Python це мова програмування високого рівня 
Python популярна для наукових обчислень та веб розробки 
мова Python має простий та зрозумілий синтаксис
"""

# Розділити текст на слова та перевести в нижній регістр
words = text.lower().split()
print(f"Усі слова тексту ({len(words)}): {words}")

# Використовуємо множину для отримання унікальних слів
unique_words = set(words)
print(f"Унікальні слова ({len(unique_words)}): {unique_words}")

# Сортуємо унікальні слова
sorted_unique_words = sorted(unique_words)
print(f"Відсортовані унікальні слова: {sorted_unique_words}")

# 2. Задача: Аналіз відвідуваності
print("\n2. АНАЛІЗ ВІДВІДУВАНОСТІ ПОДІЙ")

# Словник для зберігання відвідувачів різних подій
event_attendance = {
    "лекція_1": {"Анна", "Богдан", "Віктор", "Дмитро"},
    "лекція_2": {"Богдан", "Віктор", "Галина", "Дмитро", "Євген"},
    "лекція_3": {"Анна", "Віктор", "Галина", "Євген", "Зоя"}
}

print("Відвідувачі подій:")
for event, attendees in event_attendance.items():
    print(f"  {event}: {attendees}")

# Хто відвідав всі події?
all_events = set.intersection(*event_attendance.values())
print(f"\nСтуденти, які відвідали всі події: {all_events}")

# Хто відвідав хоча б одну подію?
any_event = set.union(*event_attendance.values())
print(f"Студенти, які відвідали хоча б одну подію: {any_event}")

# Хто відвідав тільки першу лекцію?
only_first = event_attendance["лекція_1"] - event_attendance["лекція_2"] - event_attendance["лекція_3"]
print(f"Студенти, які відвідали тільки першу лекцію: {only_first}")

# 3. Задача: Підрахунк слів у тексті
print("\n3. ПІДРАХУНОК СЛІВ У ТЕКСТІ")

def count_words(text):
    """Функція для підрахунку слів у тексті"""
    # Розділити текст на слова, перевести в нижній регістр
    words = text.lower().split()
    
    # Видалити розділові знаки
    import string
    words = [word.strip(string.punctuation) for word in words]
    
    # Створити словник для підрахунку
    word_count = {}
    
    for word in words:
        if word:  # перевірка на порожній рядок
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

sample_text = "Python це мова програмування. Python це популярна мова. Python це потужна мова."
word_counts = count_words(sample_text)

print(f"Текст: '{sample_text}'")
print("\nЧастота слів:")
for word, count in sorted(word_counts.items()):
    print(f"  '{word}': {count}")

# 4. Задача: Знаходження спільних елементів
print("\n4. ЗНАХОДЖЕННЯ СПІЛЬНИХ ІНТЕРЕСІВ")

# Словник з інтересами студентів
student_interests = {
    "Анна": {"програмування", "музика", "спорт"},
    "Богдан": {"читання", "програмування", "подорожі"},
    "Віктор": {"спорт", "програмування", "музика"},
    "Галина": {"малювання", "читання", "подорожі"}
}

print("Інтереси студентів:")
for student, interests in student_interests.items():
    print(f"  {student}: {interests}")

# Знайти спільні інтереси для кожної пари студентів
print("\nСпільні інтереси пар студентів:")
students = list(student_interests.keys())

for i in range(len(students)):
    for j in range(i + 1, len(students)):
        student1 = students[i]
        student2 = students[j]
        common_interests = student_interests[student1] & student_interests[student2]
        
        if common_interests:
            print(f"  {student1} та {student2}: {common_interests}")

# 5. Задача: Інвертування словника
print("\n5. ІНВЕРТУВАННЯ СЛОВНИКА")

def invert_dictionary(original_dict):
    """Функція для інвертування словника (ключі стають значеннями і навпаки)"""
    inverted_dict = {}
    
    for key, value in original_dict.items():
        # Якщо значення вже є ключем, додаємо до списку
        if value in inverted_dict:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key
    
    return inverted_dict

# Тестування функції
grades = {
    "Іван": "A",
    "Марія": "B",
    "Олексій": "A",
    "Анна": "C",
    "Богдан": "B"
}

inverted_grades = invert_dictionary(grades)
print(f"Оригінальний словник: {grades}")
print(f"Інвертований словник: {inverted_grades}")

# 6. Задача: Статистика за продуктами
print("\n6. СТАТИСТИКА ПРОДАЖІВ ПРОДУКТІВ")

# Словник з продажами продуктів
sales_data = [
    {"product": "Ноутбук", "category": "Електроніка", "price": 25000, "quantity": 3},
    {"product": "Мишка", "category": "Електроніка", "price": 500, "quantity": 10},
    {"product": "Книга", "category": "Книги", "price": 300, "quantity": 15},
    {"product": "Стілець", "category": "Меблі", "price": 1500, "quantity": 5},
    {"product": "Монітор", "category": "Електроніка", "price": 8000, "quantity": 2},
    {"product": "Олівець", "category": "Канцелярія", "price": 10, "quantity": 100},
]

# Загальна статистика по категоріям
category_stats = {}

for sale in sales_data:
    category = sale["category"]
    total = sale["price"] * sale["quantity"]
    
    if category not in category_stats:
        category_stats[category] = {
            "total_sales": 0,
            "total_quantity": 0,
            "products": set()
        }
    
    category_stats[category]["total_sales"] += total
    category_stats[category]["total_quantity"] += sale["quantity"]
    category_stats[category]["products"].add(sale["product"])

print("Статистика продажів по категоріям:")
for category, stats in category_stats.items():
    print(f"\n  {category}:")
    print(f"    Загальний обсяг продажів: {stats['total_sales']} грн")
    print(f"    Загальна кількість: {stats['total_quantity']} шт")
    print(f"    Продукти: {', '.join(stats['products'])}")

# 7. Задача: Пошук дублікатів
print("\n7. ПОШУК ДУБЛІКАТІВ У СПИСКУ")

def find_duplicates(items):
    """Функція для пошуку дублікатів у списку"""
    seen = set()
    duplicates = set()
    
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return duplicates

# Тестування функції
test_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 7, 9]
duplicates_found = find_duplicates(test_list)

print(f"Список: {test_list}")
print(f"Знайдені дублікати: {duplicates_found}")

print("\n" + "=" * 50)
print("ПРАКТИЧНІ ЗАДАЧІ ЗАВЕРШЕНІ")
print("=" * 50)