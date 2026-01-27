def filter_lines_by_word(input_filename, output_filename, keyword):
    """
    Функція для фільтрації рядків, що містять ключове слово
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        filtered_lines = []
        line_numbers = []
        
        for i, line in enumerate(lines, 1):
            if keyword.lower() in line.lower():
                filtered_lines.append(line)
                line_numbers.append(i)
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)
        
        print(f"Результати фільтрації:")
        print(f"Знайдено рядків з ключовим словом '{keyword}': {len(filtered_lines)}")
        print(f"Номери рядків: {line_numbers}")
        print(f"Результат збережено у файлі '{output_filename}'")
        
        if filtered_lines:
            print("\nЗнайдені рядки:")
            print("-" * 40)
            for i, line in zip(line_numbers, filtered_lines):
                print(f"Рядок {i}: {line.strip()}")
    
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def filter_lines_by_phrase(input_filename, output_filename, phrase):
    """
    Функція для фільтрації рядків, що містять фразу
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        filtered_lines = []
        line_numbers = []
        
        for i, line in enumerate(lines, 1):
            if phrase in line:
                filtered_lines.append(line)
                line_numbers.append(i)
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)
        
        print(f"Результати фільтрації за фразою '{phrase}':")
        print(f"Знайдено рядків: {len(filtered_lines)}")
        print(f"Результат збережено у файлі '{output_filename}'")
    
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def filter_lines_with_options(input_filename, output_filename, keyword, case_sensitive=False, whole_word=False):
    """
    Розширена функція фільтрації з додатковими опціями
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        filtered_lines = []
        line_numbers = []
        
        for i, line in enumerate(lines, 1):
            line_to_check = line if case_sensitive else line.lower()
            keyword_to_check = keyword if case_sensitive else keyword.lower()
            
            if whole_word:
                words = line_to_check.split()
                found = any(word.strip('.,!?;:()[]{}"\'') == keyword_to_check for word in words)
            else:
                found = keyword_to_check in line_to_check
            
            if found:
                filtered_lines.append(line)
                line_numbers.append(i)
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)
        
        total_lines = len(lines)
        filtered_count = len(filtered_lines)
        
        print(f"Статистика фільтрації:")
        print(f"Всього рядків у вихідному файлі: {total_lines}")
        print(f"Знайдено рядків з '{keyword}': {filtered_count}")
        print(f"Відсоток знайдених рядків: {filtered_count/total_lines*100:.1f}%")
        print(f"Результат збережено у файлі '{output_filename}'")
        
        return filtered_lines
    
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не знайдено!")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

if __name__ == "__main__":
    input_file = input("Введіть ім'я вихідного файлу: ")
    output_file = input("Введіть ім'я нового файлу: ")
    keyword = input("Введіть слово або фразу для пошуку: ")
    
    print("\nОберіть опції пошуку:")
    print("1. Простий пошук (без урахування регістру)")
    print("2. Пошук з урахуванням регістру")
    print("3. Пошук цілих слів (без урахування регістру)")
    print("4. Пошук цілих слів (з урахуванням регістру)")
    
    choice = input("Ваш вибір (1-4): ")
    
    if choice == '1':
        filter_lines_by_word(input_file, output_file, keyword)
    elif choice == '2':
        filter_lines_with_options(input_file, output_file, keyword, case_sensitive=True)
    elif choice == '3':
        filter_lines_with_options(input_file, output_file, keyword, whole_word=True)
    elif choice == '4':
        filter_lines_with_options(input_file, output_file, keyword, case_sensitive=True, whole_word=True)
    else:
        print("Невірний вибір. Використовується простий пошук.")
        filter_lines_by_word(input_file, output_file, keyword)