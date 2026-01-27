# task5_copy_file.py

def copy_file(source_filename, dest_filename):
    """
    Функція для копіювання вмісту одного файлу в інший
    """
    try:
        # Відкриваємо файл-джерело для читання
        with open(source_filename, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        
        # Відкриваємо файл-призначення для запису
        with open(dest_filename, 'w', encoding='utf-8') as dest_file:
            dest_file.write(content)
        
        print(f"Файл '{source_filename}' успішно скопійовано в '{dest_filename}'!")
        
        # Перевіряємо розміри файлів
        import os
        source_size = os.path.getsize(source_filename)
        dest_size = os.path.getsize(dest_filename)
        
        print(f"\nРозмір вихідного файлу: {source_size} байт")
        print(f"Розмір скопійованого файлу: {dest_size} байт")
        
        if source_size == dest_size:
            print("✓ Копіювання пройшло успішно, розміри файлів співпадають!")
        else:
            print("⚠ Увага: розміри файлів не співпадають!")
    
    except FileNotFoundError:
        print(f"Файл '{source_filename}' не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def copy_large_file(source_filename, dest_filename):
    """
    Функція для копіювання великих файлів по частинах
    (оптимальніше для роботи з великими файлами)
    """
    try:
        with open(source_filename, 'r', encoding='utf-8') as source_file:
            with open(dest_filename, 'w', encoding='utf-8') as dest_file:
                # Читаємо та записуємо файл частинами (по 1024 байта)
                chunk_size = 1024
                while True:
                    chunk = source_file.read(chunk_size)
                    if not chunk:
                        break
                    dest_file.write(chunk)
        
        print(f"Великий файл '{source_filename}' успішно скопійовано в '{dest_filename}'!")
    
    except FileNotFoundError:
        print(f"Файл '{source_filename}' не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    source = input("Введіть ім'я вихідного файлу: ")
    destination = input("Введіть ім'я нового файлу: ")
    
    # Запитуємо користувача про спосіб копіювання
    print("\nОберіть спосіб копіювання:")
    print("1. Стандартне копіювання (для малих файлів)")
    print("2. Копіювання по частинах (для великих файлів)")
    
    choice = input("Ваш вибір (1 або 2): ")
    
    if choice == '1':
        copy_file(source, destination)
    elif choice == '2':
        copy_large_file(source, destination)
    else:
        print("Невірний вибір. Використовується стандартне копіювання.")
        copy_file(source, destination)