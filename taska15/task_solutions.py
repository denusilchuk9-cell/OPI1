import math
import itertools
from collections import Counter

def demonstrate_basic_loops():
    """Демонстрація основних типів циклів"""
    print("\n" + "="*50)
    print("ДЕМОНСТРАЦІЯ ОСНОВНИХ ЦИКЛІВ")
    print("="*50)
    
    print("\n1. Цикл for зі списком:")
    fruits = ["яблуко", "банан", "апельсин", "виноград"]
    for fruit in fruits:
        print(f"  - {fruit}")
    
    print("\n2. Цикл for з функцією range():")
    for i in range(1, 6):
        print(f"  Число: {i}")
    
    print("\n3. Цикл while:")
    counter = 1
    while counter <= 5:
        print(f"  Лічильник: {counter}")
        counter += 1
    
    print("\n4. Цикл for з enumerate():")
    for index, fruit in enumerate(fruits, start=1):
        print(f"  {index}. {fruit}")
    
    print("\n5. Вкладені цикли (таблиця множення):")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"  {i} x {j} = {i*j}")
    
    print("\n6. Цикл з break та continue:")
    for i in range(1, 11):
        if i == 3:
            continue  # пропустити 3
        if i == 8:
            break     # зупинитися на 8
        print(f"  Число: {i}")


def demonstrate_functions():
    """Демонстрація створення та використання функцій"""
    print("\n" + "="*50)
    print("ДЕМОНСТРАЦІЯ ФУНКЦІЙ")
    print("="*50)
    
    def greet():
        return "Привіт, світ!"
    
    print("\n1. Проста функція:")
    print(f"  {greet()}")
    
    def add_numbers(a, b):
        """Додає два числа"""
        return a + b
    
    print("\n2. Функція з параметрами:")
    result = add_numbers(5, 3)
    print(f"  5 + 3 = {result}")
    
    def power(base, exponent=2):
        """Піднесення до степеня"""
        return base ** exponent
    
    print("\n3. Функція зі значеннями за замовчуванням:")
    print(f"  3^2 = {power(3)}")
    print(f"  2^5 = {power(2, 5)}")
    
    def average(*numbers):
        """Обчислення середнього значення"""
        if len(numbers) == 0:
            return 0
        return sum(numbers) / len(numbers)
    
    print("\n4. Функція з довільною кількістю аргументів:")
    print(f"  Середнє чисел 1, 2, 3, 4, 5: {average(1, 2, 3, 4, 5):.2f}")
    
    def min_max(numbers):
        """Знаходить мінімальне та максимальне значення"""
        return min(numbers), max(numbers)
    
    print("\n5. Функція, що повертає кілька значень:")
    numbers_list = [4, 2, 9, 7, 5]
    min_val, max_val = min_max(numbers_list)
    print(f"  Список: {numbers_list}")
    print(f"  Мінімум: {min_val}, Максимум: {max_val}")
    
    def factorial(n):
        """Обчислення факторіалу рекурсивно"""
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    
    print("\n6. Рекурсивна функція (факторіал):")
    print(f"  5! = {factorial(5)}")


def demonstrate_loops_and_functions():
    """Демонстрація комбінації циклів та функцій"""
    print("\n" + "="*50)
    print("КОМБІНАЦІЯ ЦИКЛІВ ТА ФУНКЦІЙ")
    print("="*50)
    
    def is_prime(n):
        """Перевіряє, чи є число простим"""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    print("\n1. Пошук простих чисел у діапазоні:")
    prime_numbers = []
    for num in range(1, 31):
        if is_prime(num):
            prime_numbers.append(num)
    
    print(f"  Прості числа від 1 до 30: {prime_numbers}")
    
    def process_list(numbers, operation):
        """Застосовує операцію до кожного елемента списку"""
        result = []
        for num in numbers:
            if operation == "square":
                result.append(num ** 2)
            elif operation == "cube":
                result.append(num ** 3)
            elif operation == "double":
                result.append(num * 2)
        return result
    
    print("\n2. Обробка списку за допомогою функції:")
    numbers = [1, 2, 3, 4, 5]
    print(f"  Початковий список: {numbers}")
    print(f"  Квадрати: {process_list(numbers, 'square')}")
    print(f"  Кубі: {process_list(numbers, 'cube')}")
    
    print("\n3. Генератор списку з використанням функції:")
    squares = [x**2 for x in range(1, 6)]
    cubes = [x**3 for x in range(1, 6)]
    print(f"  Квадрати: {squares}")
    print(f"  Кубі: {cubes}")


def demonstrate_libraries():
    """Демонстрація використання бібліотек"""
    print("\n" + "="*50)
    print("ВИКОРИСТАННЯ БІБЛІОТЕК")
    print("="*50)
    
    print("\n1. Використання модуля math:")
    print(f"  math.pi = {math.pi:.5f}")
    print(f"  math.sin(math.pi/2) = {math.sin(math.pi/2):.3f}")
    print(f"  math.sqrt(16) = {math.sqrt(16)}")
    print(f"  math.factorial(6) = {math.factorial(6)}")
    
    print("\n2. Використання модуля itertools:")
    
    print("  itertools.count (перші 5 чисел):")
    counter = itertools.count(start=10, step=2)
    for i, num in enumerate(counter):
        if i >= 5:
            break
        print(f"    {num}")
    
    print("\n  itertools.cycle (3 цикли):")
    cycle = itertools.cycle(['A', 'B', 'C'])
    for i in range(9):
        if i >= 9:
            break
        print(f"    {next(cycle)}", end=' ')
    print()
    
    print("\n  itertools.permutations:")
    items = ['X', 'Y', 'Z']
    permutations = list(itertools.permutations(items, 2))
    print(f"    Перестановки з {items} по 2: {permutations}")


def run_statistics_calculator():
    """Калькулятор статистики - реальна задача"""
    print("\n" + "="*50)
    print("КАЛЬКУЛЯТОР СТАТИСТИКИ")
    print("="*50)
    
    def calculate_statistics(data):
        """Обчислює основні статистичні показники"""
        if not data:
            return None
        
        n = len(data)
        mean = sum(data) / n
        
        sorted_data = sorted(data)
        if n % 2 == 0:
            median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            median = sorted_data[n//2]
        
        from collections import Counter
        freq = Counter(data)
        max_freq = max(freq.values())
        mode = [k for k, v in freq.items() if v == max_freq]
        
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = math.sqrt(variance)
        
        min_val = min(data)
        max_val = max(data)
        
        return {
            'кількість': n,
            'середнє': mean,
            'медіана': median,
            'мода': mode,
            'дисперсія': variance,
            'стандартне відхилення': std_dev,
            'мінімум': min_val,
            'максимум': max_val,
            'сума': sum(data)
        }
    
    test_data = [12, 15, 18, 22, 25, 25, 28, 30, 32, 35]
    print("\nПриклад даних:", test_data)
    
    stats = calculate_statistics(test_data)
    
    if stats:
        print("\nРезультати статистичного аналізу:")
        for key, value in stats.items():
            if isinstance(value, float):
                print(f"  {key}: {value:.2f}")
            else:
                print(f"  {key}: {value}")