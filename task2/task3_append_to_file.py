# task3_append_to_file.py

def append_to_file(filename):
    """
    Функція для додавання тексту до існуючого файлу
    """
    print("Введіть текст для додавання до файлу:")
    text = input("Текст: ")
    
    try:
        # Відкриваємо файл для додавання ('a' - append)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text + '\n')
        
        print(f"Текст успішно додано до файлу '{filename}'!")
        
        # Показуємо оновлений вміст файлу
        print(f"\nОновлений вміст файлу '{filename}':")
        print("-" * 40)
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено!")
        # Створюємо новий файл, якщо він не існує
        create_new = input("Створити новий файл? (так/ні): ")
        if create_new.lower() == 'так':
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(text + '\n')
            print(f"Файл '{filename}' створено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    filename = input("Введіть ім'я файлу: ")
    append_to_file(filename)