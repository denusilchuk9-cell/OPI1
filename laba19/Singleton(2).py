class LazySingleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Лінива ініціалізація: створюємо екземпляр")
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.data = []
            self.initialized = True
            print("Ініціалізація даних")
    
    def add_data(self, item):
        self.data.append(item)
        return f"Додано: {item}"

# Тестування
print("\n=== Лінива ініціалізація ===")
lazy1 = LazySingleton()
lazy2 = LazySingleton()
print(lazy1.add_data("тест"))
print(f"Дані: {lazy2.data}")