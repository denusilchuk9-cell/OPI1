"""
Файл 5: Реальні застосування множин та словників
"""

print("=" * 50)
print("РЕАЛЬНІ ЗАСТОСУВАННЯ МНОЖИН ТА СЛОВНИКІВ")
print("=" * 50)

# 1. Система управління завданнями
print("\n1. СИСТЕМА УПРАВЛІННЯ ЗАВДАННЯМИ")

class TaskManager:
    def __init__(self):
        self.tasks = {}  # ID завдання -> інформація про завдання
        self.categories = set()  # Унікальні категорії
        self.completed_tasks = set()  # ID виконаних завдань
        self.next_id = 1
    
    def add_task(self, description, category, priority=1):
        """Додати нове завдання"""
        task_id = self.next_id
        self.tasks[task_id] = {
            "description": description,
            "category": category,
            "priority": priority,
            "created": "2024-01-15"  # Тут можна використати datetime.now()
        }
        self.categories.add(category)
        self.next_id += 1
        return task_id
    
    def complete_task(self, task_id):
        """Позначити завдання як виконане"""
        if task_id in self.tasks:
            self.completed_tasks.add(task_id)
            return True
        return False
    
    def get_tasks_by_category(self, category):
        """Отримати завдання за категорією"""
        return {task_id: task_info 
                for task_id, task_info in self.tasks.items() 
                if task_info["category"] == category and task_id not in self.completed_tasks}
    
    def get_statistics(self):
        """Отримати статистику по завданнях"""
        total_tasks = len(self.tasks)
        completed = len(self.completed_tasks)
        pending = total_tasks - completed
        
        # Завдання по категоріях
        tasks_by_category = {}
        for task_id, task_info in self.tasks.items():
            category = task_info["category"]
            if category not in tasks_by_category:
                tasks_by_category[category] = {"total": 0, "completed": 0}
            
            tasks_by_category[category]["total"] += 1
            if task_id in self.completed_tasks:
                tasks_by_category[category]["completed"] += 1
        
        return {
            "total_tasks": total_tasks,
            "completed": completed,
            "pending": pending,
            "completion_rate": (completed / total_tasks * 100) if total_tasks > 0 else 0,
            "by_category": tasks_by_category
        }

# Демонстрація системи
print("Демонстрація системи управління завданнями:")
manager = TaskManager()

# Додаємо завдання
manager.add_task("Зробити практичну роботу з Python", "Навчання", priority=2)
manager.add_task("Купити продукти", "Особисте", priority=1)
manager.add_task("Прочитати книгу", "Навчання", priority=3)
manager.add_task("Помити авто", "Особисте", priority=2)

# Позначаємо деякі завдання виконаними
manager.complete_task(1)
manager.complete_task(4)

# Отримуємо статистику
stats = manager.get_statistics()

print(f"\nЗагальна статистика:")
print(f"  Всього завдань: {stats['total_tasks']}")
print(f"  Виконано: {stats['completed']}")
print(f"  В очікуванні: {stats['pending']}")
print(f"  Відсоток виконання: {stats['completion_rate']:.1f}%")

print(f"\nСтатистика по категоріях:")
for category, cat_stats in stats['by_category'].items():
    print(f"  {category}: {cat_stats['completed']}/{cat_stats['total']} виконано")

print(f"\nНевиконані завдання по категоріях:")
for category in manager.categories:
    pending_tasks = manager.get_tasks_by_category(category)
    if pending_tasks:
        print(f"  {category}: {len(pending_tasks)} завдань")

# 2. Система рекомендацій на основі інтересів
print("\n\n2. СИСТЕМА РЕКОМЕНДАЦІЙ")

class RecommendationSystem:
    def __init__(self):
        self.user_interests = {}  # Користувач -> множина інтересів
        self.item_categories = {}  # Елемент -> категорія
    
    def add_user(self, user_id, interests):
        """Додати користувача з його інтересами"""
        self.user_interests[user_id] = set(interests)
    
    def add_item(self, item_id, category):
        """Додати елемент з категорією"""
        self.item_categories[item_id] = category
    
    def recommend_items(self, user_id, all_items):
        """Рекомендувати елементи користувачу"""
        if user_id not in self.user_interests:
            return []
        
        user_interests = self.user_interests[user_id]
        recommended = []
        
        for item_id in all_items:
            if item_id in self.item_categories:
                category = self.item_categories[item_id]
                if category in user_interests:
                    recommended.append(item_id)
        
        return recommended
    
    def find_similar_users(self, user_id):
        """Знайти користувачів зі схожими інтересами"""
        if user_id not in self.user_interests:
            return []
        
        current_interests = self.user_interests[user_id]
        similar_users = []
        
        for other_user, interests in self.user_interests.items():
            if other_user != user_id:
                # Обчислюємо схожість за допомогою коефіцієнта Жаккара
                common = len(current_interests & interests)
                total = len(current_interests | interests)
                similarity = common / total if total > 0 else 0
                
                if similarity > 0.3:  # Поріг схожості
                    similar_users.append((other_user, similarity))
        
        # Сортуємо за схожістю (спадання)
        similar_users.sort(key=lambda x: x[1], reverse=True)
        return similar_users

# Демонстрація системи рекомендацій
print("Демонстрація системи рекомендацій:")

rec_system = RecommendationSystem()

# Додаємо користувачів
rec_system.add_user("user1", ["програмування", "наука", "технології"])
rec_system.add_user("user2", ["мистецтво", "музика", "література"])
rec_system.add_user("user3", ["програмування", "математика", "наука"])

# Додаємо елементи
rec_system.add_item("курс_python", "програмування")
rec_system.add_item("книга_мистецтво", "мистецтво")
rec_system.add_item("курс_математика", "математика")
rec_system.add_item("концерт", "музика")
rec_system.add_item("лекція_наука", "наука")

# Отримуємо рекомендації
all_items = ["курс_python", "книга_мистецтво", "курс_математика", "концерт", "лекція_наука"]
recommendations = rec_system.recommend_items("user1", all_items)

print(f"\nРекомендації для user1: {recommendations}")

# Знаходимо схожих користувачів
similar = rec_system.find_similar_users("user1")
print(f"\nКористувачі, схожі на user1:")
for user, similarity in similar:
    print(f"  {user}: {similarity:.2f} схожості")

# 3. Аналіз логів веб-сервера
print("\n\n3. АНАЛІЗ ЛОГІВ ВЕБ-СЕРВЕРА")

def analyze_web_logs(log_entries):
    """Аналізує лог-файли веб-сервера"""
    
    # Статистика
    stats = {
        "total_requests": 0,
        "unique_ips": set(),
        "endpoints": {},
        "status_codes": {},
        "requests_by_hour": {}
    }
    
    for entry in log_entries:
        stats["total_requests"] += 1
        
        # Розбираємо запис (спрощено)
        parts = entry.split()
        if len(parts) >= 7:
            ip = parts[0]
            endpoint = parts[6]
            status_code = parts[8]
            hour = parts[3].split(':')[1]
            
            # Збираємо статистику
            stats["unique_ips"].add(ip)
            
            stats["endpoints"][endpoint] = stats["endpoints"].get(endpoint, 0) + 1
            stats["status_codes"][status_code] = stats["status_codes"].get(status_code, 0) + 1
            stats["requests_by_hour"][hour] = stats["requests_by_hour"].get(hour, 0) + 1
    
    # Конвертуємо множину IP в список для виводу
    stats["unique_ips"] = list(stats["unique_ips"])
    
    return stats

# Приклад логів
sample_logs = [
    '192.168.1.1 - - [15/Jan/2024:10:15:32 +0200] "GET /index.html HTTP/1.1" 200 1234',
    '192.168.1.2 - - [15/Jan/2024:10:15:35 +0200] "GET /about.html HTTP/1.1" 200 5678',
    '192.168.1.1 - - [15/Jan/2024:10:16:10 +0200] "POST /login HTTP/1.1" 302 123',
    '192.168.1.3 - - [15/Jan/2024:10:16:15 +0200] "GET /contact.html HTTP/1.1" 200 3456',
    '192.168.1.2 - - [15/Jan/2024:10:16:20 +0200] "GET /admin.php HTTP/1.1" 403 789',
    '192.168.1.4 - - [15/Jan/2024:11:05:01 +0200] "GET /index.html HTTP/1.1" 200 1234',
]

print("Аналіз логів веб-сервера:")
analysis = analyze_web_logs(sample_logs)

print(f"\nЗагальна статистика:")
print(f"  Всього запитів: {analysis['total_requests']}")
print(f"  Унікальних IP: {len(analysis['unique_ips'])}")
print(f"  Список IP: {analysis['unique_ips']}")

print(f"\nНайпопулярніші ендпоінти:")
for endpoint, count in sorted(analysis['endpoints'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {endpoint}: {count} запитів")

print(f"\nСтатус коди відповідей:")
for code, count in sorted(analysis['status_codes'].items()):
    print(f"  {code}: {count} разів")

print(f"\nЗапити за годинами:")
for hour, count in sorted(analysis['requests_by_hour'].items()):
    print(f"  {hour}:00 - {count} запитів")

# 4. Система кешування
print("\n\n4. ПРОСТА СИСТЕМА КЕШУВАННЯ")

class LRUCache:
    """Проста реалізація LRU (Least Recently Used) кешу"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Ключ -> значення
        self.access_order = []  # Список для відстеження порядку доступу
    
    def get(self, key):
        """Отримати значення за ключем"""
        if key in self.cache:
            # Оновлюємо порядок доступу
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        """Додати значення в кеш"""
        if key in self.cache:
            # Оновлюємо існуючий запис
            self.cache[key] = value
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            # Додаємо новий запис
            if len(self.cache) >= self.capacity:
                # Видаляємо найменш використаний елемент
                lru_key = self.access_order.pop(0)
                del self.cache[lru_key]
            
            self.cache[key] = value
            self.access_order.append(key)
    
    def clear(self):
        """Очистити кеш"""
        self.cache.clear()
        self.access_order.clear()
    
    def __str__(self):
        return f"LRUCache({len(self.cache)}/{self.capacity}): {self.cache}"

# Демонстрація кешу
print("Демонстрація LRU кешування:")

cache = LRUCache(3)

# Додаємо елементи
cache.put("user:1", {"name": "Анна", "age": 25})
cache.put("user:2", {"name": "Богдан", "age": 30})
cache.put("user:3", {"name": "Віктор", "age": 28})

print(f"Після додавання 3 елементів: {cache}")

# Отримуємо елемент (оновлюємо його "вік")
user1 = cache.get("user:1")
print(f"\nОтримано user:1: {user1}")
print(f"Після доступу до user:1: {cache}")

# Додаємо новий елемент (повинен витіснити user:2)
cache.put("user:4", {"name": "Галина", "age": 32})
print(f"\nПісля додавання user:4 (перевищення ємності): {cache}")

# Перевіряємо, що user:2 був видалений
user2 = cache.get("user:2")
print(f"Отримано user:2: {user2} (очікується None)")

print("\n" + "=" * 50)
print("РЕАЛЬНІ ЗАСТОСУВАННЯ ЗАВЕРШЕНІ")
print("=" * 50)