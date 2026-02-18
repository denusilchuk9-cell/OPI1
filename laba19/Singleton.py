class SimpleSingleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Створено новий екземпляр SimpleSingleton")
        return cls._instance
    
    def __init__(self):
        self.value = 0
    
    def increment(self):
        self.value += 1
        return self.value

# Тестування
print("=== Простий Singleton ===")
s1 = SimpleSingleton()
s2 = SimpleSingleton()
print(f"s1.value = {s1.increment()}")  # 1
print(f"s2.value = {s2.increment()}")  # 2
print(f"s1 is s2: {s1 is s2}")  # True