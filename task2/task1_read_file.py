def read_file_line_by_line(filename):
    """
    Функція для читання файлу по рядках
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_number = 1
            for line in file:
                print(f"Рядок {line_number}: {line.strip()}")
                line_number += 1
    
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def create_test_file():
    with open('test_file.txt', 'w', encoding='utf-8') as file:
        file.write("Це перший рядок файлу.\n")
        file.write("Це другий рядок.\n")
        file.write("А це третій рядок тексту.\n")
        file.write("Python - чудова мова програмування.\n")
        file.write("Робота з файлами - важлива навичка.\n")

# Основна частина програми
if __name__ == "__main__":
    # Створення тестового файлу
    create_test_file()
    
    print("Читання файлу 'test_file.txt':")
    print("-" * 40)
    read_file_line_by_line('test_file.txt')