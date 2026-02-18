import threading
import time

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    print("Створено потокобезпечний Singleton")
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'counter'):
            self.counter = 0
            self.log = []
    
    def safe_increment(self, thread_name):
        with self._lock:
            self.counter += 1
            message = f"{thread_name}: {self.counter}"
            self.log.append(message)
            time.sleep(0.1)  # Імітація роботи
            return message

def worker(thread_name, singleton):
    for i in range(3):
        result = singleton.safe_increment(thread_name)
        print(result)

# Тестування
print("\n=== Потокобезпечний Singleton ===")
safe_singleton = ThreadSafeSingleton()

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}", safe_singleton))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Фінальний лічильник: {safe_singleton.counter}")