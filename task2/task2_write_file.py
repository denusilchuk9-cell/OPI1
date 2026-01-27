# task2_write_file.py

def write_to_file():
    """
    Функція для запису рядків від користувача у файл
    """
    filename = input("Введіть ім'я файлу для запису: ")
    
    print("Введіть текст (для завершення введіть 'кінець'):")
    
    lines = []
    line_count = 1
    
    while True:
        line = input(f"Рядок {line_count}: ")
        if line.lower() == 'кінець':
            break
        lines.append(line)
        line_count += 1
    
    try:
        # Відкриваємо файл для запису ('w' - write)
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        
        print(f"Дані успішно записані у файл '{filename}'!")
        
        # Показуємо вміст створеного файлу
        print("\nВміст файлу:")
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    write_to_file()