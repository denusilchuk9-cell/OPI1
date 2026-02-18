class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'connected'):
            self.connected = False
            self.connection_string = None
            self.query_count = 0
    
    def connect(self, connection_string):
        if not self.connected:
            self.connection_string = connection_string
            self.connected = True
            print(f"Підключено до БД: {connection_string}")
    
    def execute_query(self, query):
        if not self.connected:
            raise Exception("Спочатку підключіться до БД")
        
        self.query_count += 1
        return f"Виконано запит #{self.query_count}: {query}"
    
    def disconnect(self):
        if self.connected:
            self.connected = False
            print("Відключено від БД")

# Тестування
print("\n=== DatabaseConnection Singleton ===")
db1 = DatabaseConnection()
db2 = DatabaseConnection()

db1.connect("localhost:5432/mydb")
print(db1.execute_query("SELECT * FROM users"))
print(db2.execute_query("INSERT INTO logs VALUES ('test')"))
db2.disconnect()

try:
    db1.execute_query("SELECT * FROM products")  # Помилка, бо вже відключено
except Exception as e:
    print(f"Помилка: {e}")