"""
Файл 6: Шаблон для домашнього завдання
Студенти можуть використовувати цей шаблон для власних проектів
"""

print("=" * 50)
print("ШАБЛОН ДЛЯ ДОМАШНЬОГО ЗАВДАННЯ")
print("=" * 50)

class StudentProject:
    """
    Базовий клас для студентського проекту з використанням множин та словників
    
    Студенти можуть модифікувати цей клас або створювати власні рішення
    """
    
    def __init__(self, project_name):
        self.project_name = project_name
        self.data = {}
        self.metadata = {
            "created": "2024-01-15",
            "author": "Студент",
            "version": "1.0"
        }
    
    def demonstrate_sets(self):
        """Демонстрація роботи з множинами"""
        print(f"\n{'='*30}")
        print(f"ДЕМОНСТРАЦІЯ МНОЖИН ДЛЯ ПРОЄКТУ: {self.project_name}")
        print(f"{'='*30}")
        
        # Приклад 1: Обробка унікальних користувачів
        users_visited_page_a = {"user1", "user2", "user3", "user5"}
        users_visited_page_b = {"user2", "user3", "user4", "user6"}
        
        print(f"\n1. Аналіз відвідувачів сторінок:")
        print(f"   Сторінка A: {users_visited_page_a}")
        print(f"   Сторінка B: {users_visited_page_b}")
        
        # Унікальні відвідувачі обох сторінок
        all_visitors = users_visited_page_a | users_visited_page_b
        print(f"   Всі унікальні відвідувачі: {all_visitors}")
        
        # Відвідувачі обох сторінок
        common_visitors = users_visited_page_a & users_visited_page_b
        print(f"   Відвідувачі обох сторінок: {common_visitors}")
        
        # Відвідувачі тільки сторінки A
        only_a = users_visited_page_a - users_visited_page_b
        print(f"   Тільки сторінка A: {only_a}")
        
        # Приклад 2: Фільтрація дублікатів
        print(f"\n2. Фільтрація дублікатів у даних:")
        raw_data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
        unique_data = set(raw_data)
        print(f"   Вихідні дані: {raw_data}")
        print(f"   Унікальні значення: {sorted(unique_data)}")
        
        return {
            "all_visitors": all_visitors,
            "common_visitors": common_visitors,
            "only_a": only_a,
            "unique_data": unique_data
        }
    
    def demonstrate_dictionaries(self):
        """Демонстрація роботи з словниками"""
        print(f"\n{'='*30}")
        print(f"ДЕМОНСТРАЦІЯ СЛОВНИКІВ ДЛЯ ПРОЄКТУ: {self.project_name}")
        print(f"{'='*30}")
        
        # Приклад 1: Словник продуктів
        products = {
            "001": {"name": "Ноутбук", "price": 25000, "category": "Електроніка"},
            "002": {"name": "Мишка", "price": 500, "category": "Електроніка"},
            "003": {"name": "Книга", "price": 300, "category": "Освіта"},
            "004": {"name": "Стілець", "price": 1500, "category": "Меблі"},
        }
        
        print(f"\n1. Каталог продуктів:")
        for product_id, product_info in products.items():
            print(f"   {product_id}: {product_info['name']} - {product_info['price']} грн")
        
        # Приклад 2: Агрегація даних
        print(f"\n2. Агрегація даних по категоріях:")
        category_stats = {}
        
        for product_id, product_info in products.items():
            category = product_info["category"]
            price = product_info["price"]
            
            if category not in category_stats:
                category_stats[category] = {
                    "count": 0,
                    "total_price": 0,
                    "products": []
                }
            
            category_stats[category]["count"] += 1
            category_stats[category]["total_price"] += price
            category_stats[category]["products"].append(product_info["name"])
        
        for category, stats in category_stats.items():
            avg_price = stats["total_price"] / stats["count"] if stats["count"] > 0 else 0
            print(f"   {category}: {stats['count']} товарів, "
                  f"середня ціна: {avg_price:.2f} грн")
        
        # Приклад 3: Пошук у словнику
        print(f"\n3. Пошук продуктів за критеріями:")
        max_price = 1000
        affordable_products = {
            pid: info for pid, info in products.items() 
            if info["price"] <= max_price
        }
        
        print(f"   Продукти дешевше {max_price} грн:")
        for pid, info in affordable_products.items():
            print(f"     {info['name']}: {info['price']} грн")
        
        return {
            "products": products,
            "category_stats": category_stats,
            "affordable_products": affordable_products
        }
    
    def create_custom_solution(self, problem_description):
        """
        Студенти мають реалізувати цей метод для власного завдання
        
        Аргументи:
            problem_description: опис проблеми для розв'язання
        
        Повертає:
            словник з результатами
        """
        print(f"\n{'='*30}")
        print(f"ВЛАСНЕ РІШЕННЯ: {problem_description}")
        print(f"{'='*30}")
        
        # TODO: Студенти мають реалізувати власне рішення тут
        print("Цей метод мають реалізувати студенти для власного проекту")
        
        # Приклад реалізації (для демонстрації)
        if "унікальні" in problem_description.lower():
            # Приклад: знаходження унікальних слів у тексті
            text = "Python це мова програмування Python це популярна мова"
            words = text.lower().split()
            unique_words = set(words)
            
            print(f"\nТекст: '{text}'")
            print(f"Унікальні слова: {unique_words}")
            print(f"Кількість унікальних слів: {len(unique_words)}")
            
            return {
                "text": text,
                "unique_words": unique_words,
                "count": len(unique_words)
            }
        
        return {"status": "Не реалізовано", "message": "Студент має реалізувати цей метод"}
    
    def present_results(self, results):
        """Презентація результатів проекту"""
        print(f"\n{'='*30}")
        print(f"ПРЕЗЕНТАЦІЯ РЕЗУЛЬТАТІВ: {self.project_name}")
        print(f"{'='*30}")
        
        print(f"\nМета проекту: Демонстрація використання множин та словників")
        print(f"Автор: {self.metadata['author']}")
        print(f"Версія: {self.metadata['version']}")
        
        print(f"\nОтримані результати:")
        for key, value in results.items():
            if isinstance(value, (set, dict, list)):
                print(f"  {key}: {type(value).__name__} з {len(value)} елементів")
            else:
                print(f"  {key}: {value}")
        
        print(f"\nВисновки:")
        print("  1. Множини ефективні для роботи з унікальними значеннями")
        print("  2. Словники дозволяють швидко отримувати доступ до даних за ключем")
        print("  3. Комбінація множин та словників дозволяє створювати потужні структури даних")

# Головна функція для запуску проекту
def main():
    """Основна функція для демонстрації проекту"""
    
    # Створення екземпляру проекту
    project = StudentProject("Аналіз даних з використанням множин та словників")
    
    print(f"Запуск проекту: {project.project_name}")
    print(f"Автор: {project.metadata['author']}")
    
    # Демонстрація можливостей
    set_results = project.demonstrate_sets()
    dict_results = project.demonstrate_dictionaries()
    
    # Власне рішення студента
    custom_solution = project.create_custom_solution(
        "Знаходження унікальних елементів у наборі даних"
    )
    
    # Презентація результатів
    all_results = {
        "set_operations": set_results,
        "dictionary_operations": dict_results,
        "custom_solution": custom_solution
    }
    
    project.present_results(all_results)
    
    print(f"\n{'='*50}")
    print(f"ПРОЄКТ ЗАВЕРШЕНО УСПІШНО!")
    print(f"{'='*50}")

# Додаткові функції для допомоги студентам
def helper_functions():
    """Допоміжні функції для студентів"""
    
    print(f"\n{'='*30}")
    print("ДОПОМІЖНІ ФУНКЦІЇ ТА ПРИКЛАДИ")
    print(f"{'='*30}")
    
    # 1. Конвертація між типами
    print("\n1. Конвертація між множинами та списками:")
    
    my_list = [1, 2, 3, 2, 4, 1, 5]
    my_set = set(my_list)
    new_list = list(my_set)
    
    print(f"   Початковий список: {my_list}")
    print(f"   Множина (без дублікатів): {my_set}")
    print(f"   Новий список з унікальних значень: {new_list}")
    
    # 2. Сортування словника
    print("\n2. Сортування словника:")
    
    scores = {"Анна": 85, "Богдан": 92, "Віктор": 78, "Галина": 95}
    
    # Сортування за ключами
    sorted_by_name = dict(sorted(scores.items()))
    print(f"   Сортування за іменами: {sorted_by_name}")
    
    # Сортування за значеннями (спадання)
    sorted_by_score = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    print(f"   Сортування за оцінками (спадання): {sorted_by_score}")
    
    # 3. Об'єднання словників
    print("\n3. Об'єднання словників:")
    
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}  # Зауважте: ключ 'b' присутній в обох словниках
    
    # Спосіб 1: update() (перезаписує значення)
    merged1 = dict1.copy()
    merged1.update(dict2)
    print(f"   update() (останнє значення для 'b'): {merged1}")
    
    # Спосіб 2: додавання значень для спільних ключів
    merged2 = {}
    for key in set(dict1.keys()) | set(dict2.keys()):
        merged2[key] = dict1.get(key, 0) + dict2.get(key, 0)
    print(f"   Сума значень для спільних ключів: {merged2}")
    
    return {
        "list_to_set": my_set,
        "sorted_scores": sorted_by_score,
        "merged_dicts": [merged1, merged2]
    }

# Інструкції для студентів
def student_instructions():
    """Інструкції для виконання домашнього завдання"""
    
    print(f"\n{'='*50}")
    print("ІНСТРУКЦІЇ ДЛЯ ВИКОНАННЯ ДОМАШНЬОГО ЗАВДАННЯ")
    print(f"{'='*50}")
    
    instructions = [
        "1. Виберіть тему для власного проекту (наприклад: система обліку книг,",
        "   аналіз соціальних мереж, система рекомендацій, обробка текстів тощо)",
        "",
        "2. Модифікуйте клас StudentProject або створіть власний клас",
        "",
        "3. Реалізуйте метод create_custom_solution() для вашого завдання",
        "",
        "4. Використайте множини для:",
        "   - Видалення дублікатів",
        "   - Пошуку спільних/унікальних елементів",
        "   - Операцій об'єднання, перетину, різниці",
        "",
        "5. Використайте словники для:",
        "   - Зберігання структурованих даних",
        "   - Швидкого пошуку за ключем",
        "   - Агрегації та аналізу даних",
        "",
        "6. Підготуйте презентацію, яка містить:",
        "   - Опис проблеми",
        "   - Вибір структур даних та обґрунтування",
        "   - Приклади коду з коментарями",
        "   - Результати роботи програми",
        "   - Висновки",
        "",
        "7. Перевірте програму на різних вхідних даних",
        "",
        "8. Подумайте про оптимізацію та можливі покращення",
    ]
    
    for line in instructions:
        print(line)

if __name__ == "__main__":
    # Запуск демонстрації
    main()
    
    # Показати допоміжні функції
    helper_functions()
    
    # Показати інструкції
    student_instructions()