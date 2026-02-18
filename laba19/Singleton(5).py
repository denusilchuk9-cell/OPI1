from datetime import datetime

class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'logs'):
            self.logs = []
            self.log_file = "app.log"
    
    def log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.logs.append(log_entry)
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
        
        print(log_entry)
    
    def info(self, message):
        self.log("INFO", message)
    
    def error(self, message):
        self.log("ERROR", message)
    
    def warning(self, message):
        self.log("WARNING", message)
    
    def get_logs(self):
        return self.logs

# Тестування
print("\n=== Logger Singleton ===")
logger1 = Logger()
logger2 = Logger()

logger1.info("Програма запущена")
logger2.warning("Низький рівень пам'яті")
logger1.error("Помилка з'єднання")

print(f"logger1 is logger2: {logger1 is logger2}")
print(f"Всього записів: {len(logger2.get_logs())}")