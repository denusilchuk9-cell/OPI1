import struct
import random

def write_numbers_to_binary(filename, numbers):
    """
    Запис списку чисел у бінарний файл
    """
    try:
        with open(filename, 'wb') as file:  # 'wb' - write binary
            file.write(struct.pack('i', len(numbers)))
            
            for num in numbers:
                file.write(struct.pack('d', num))
        
        print(f"Список чисел успішно записано у бінарний файл '{filename}'")
    
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")

def read_numbers_from_binary(filename):
    """
    Читання чисел з бінарного файлу та обчислення суми
    """
    try:
        with open(filename, 'rb') as file:  # 'rb' - read binary
            count_bytes = file.read(4)
            if len(count_bytes) < 4:
                print("Файл занадто короткий!")
                return []
            
            count = struct.unpack('i', count_bytes)[0]
            
            numbers = []
            for _ in range(count):
                num_bytes = file.read(8)
                if len(num_bytes) < 8:
                    print("Недостатньо даних у файлі!")
                    break
                num = struct.unpack('d', num_bytes)[0]
                numbers.append(num)
        
        return numbers
    
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено!")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

def demonstrate_binary_operations():
    """
    Демонстраційна функція для роботи з бінарними файлами
    """
    print("Демонстрація роботи з бінарними файлами")
    print("-" * 40)
    
    numbers = [random.uniform(1, 100) for _ in range(10)]
    
    print("Згенеровані числа:")
    for i, num in enumerate(numbers, 1):
        print(f"{i:2}. {num:10.4f}")
    
    filename = "numbers.bin"
    write_numbers_to_binary(filename, numbers)
    
    print(f"\nЧитання чисел з файлу '{filename}':")
    read_numbers = read_numbers_from_binary(filename)
    
    if read_numbers:
        print("Прочитані числа:")
        total_sum = 0
        
        for i, num in enumerate(read_numbers, 1):
            print(f"{i:2}. {num:10.4f}")
            total_sum += num
        
        print("-" * 40)
        print(f"Сума всіх чисел: {total_sum:.4f}")
        print(f"Середнє арифметичне: {total_sum/len(read_numbers):.4f}")
        
        if len(numbers) == len(read_numbers):
            all_match = all(abs(a - b) < 0.0001 for a, b in zip(numbers, read_numbers))
            if all_match:
                print("✓ Дані успішно збережено та відновлено!")
            else:
                print("⚠ Деякі дані не співпадають!")
    
    print(f"\nПерегляд бінарного файлу '{filename}' у HEX форматі:")
    try:
        with open(filename, 'rb') as file:
            data = file.read()
            hex_data = data[:64].hex()
            for i in range(0, len(hex_data), 16):
                print(hex_data[i:i+16])
        
        print(f"\nРозмір файлу: {len(data)} байт")
    
    except Exception as e:
        print(f"Помилка: {e}")

def manual_binary_operations():
    """
    Функція для ручного введення чисел
    """
    print("Ручне введення чисел для запису у бінарний файл")
    
    numbers = []
    print("Введіть числа (для завершення введіть 'кінець'):")
    
    while True:
        user_input = input("Число: ")
        if user_input.lower() == 'кінець':
            break
        
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Будь ласка, введіть дійсне число!")
    
    if numbers:
        filename = input("Введіть ім'я бінарного файлу: ")
        write_numbers_to_binary(filename, numbers)
        
        read_numbers = read_numbers_from_binary(filename)
        if read_numbers:
            total_sum = sum(read_numbers)
            print(f"\nСума чисел: {total_sum:.4f}")
            print(f"Кількість чисел: {len(read_numbers)}")
            print(f"Середнє значення: {total_sum/len(read_numbers):.4f}")
    else:
        print("Не введено жодного числа!")

if __name__ == "__main__":
    print("Робота з бінарними файлами")
    print("1. Демонстраційний режим")
    print("2. Ручне введення чисел")
    
    choice = input("Ваш вибір (1 або 2): ")
    
    if choice == '1':
        demonstrate_binary_operations()
    elif choice == '2':
        manual_binary_operations()
    else:
        print("Невірний вибір. Запускається демонстраційний режим.")
        demonstrate_binary_operations()