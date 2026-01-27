def search_and_replace(input_filename, output_filename, search_word, replace_word):
    """
    Функція для пошуку та заміни тексту у файлі
    """
    try:
        # Зчитуємо вміст файлу
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Виконуємо заміну
        # count - кількість замін
        new_content, count = content.replace(search_word, replace_word), content.count(search_word)
        
        # Записуємо результат у новий файл
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f"Заміна виконана успішно!")
        print(f"Знайдено та замінено {count} входжень слова '{search_word}' на '{replace_word}'")
        print(f"Результат збережено у файлі '{output_filename}'")
        
        # Показуємо фрагмент з замінами
        if count > 0:
            print("\nФрагмент тексту з виконаними замінами:")
            print("-" * 40)
            
            # Знаходимо перше входження у новому тексті
            lines = new_content.split('\n')
            for i, line in enumerate(lines[:5]):  # Показуємо перші 5 рядків
                if replace_word in line:
                    print(f"Рядок {i+1}: {line}")
                    if i == 4 and len(lines) > 5:
                        print("...")
    
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def search_and_replace_case_sensitive(input_filename, output_filename, search_word, replace_word):
    """
    Функція для пошуку та заміни з урахуванням регістру
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        count = 0
        new_lines = []
        
        for line in lines:
            # Замінюємо тільки повні слова з урахуванням регістру
            words = line.split()
            new_words = []
            
            for word in words:
                # Видаляємо розділові знаки для порівняння
                clean_word = word.strip('.,!?;:()[]{}"\'').strip("'")
                if clean_word == search_word:
                    # Замінюємо слово, зберігаючи розділові знаки
                    if word.startswith(clean_word):
                        new_word = replace_word + word[len(clean_word):]
                    else:
                        new_word = word.replace(clean_word, replace_word)
                    new_words.append(new_word)
                    count += 1
                else:
                    new_words.append(word)
            
            new_line = ' '.join(new_words)
            new_lines.append(new_line)
        
        # Записуємо результат
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
        
        print(f"Заміна виконана успішно!")
        print(f"Знайдено та замінено {count} повних слів '{search_word}' на '{replace_word}'")
        print(f"Результат збережено у файлі '{output_filename}'")
    
    except FileNotFoundError:
        print(f"Файл '{input_filename}' не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    input_file = input("Введіть ім'я вихідного файлу: ")
    output_file = input("Введіть ім'я нового файлу: ")
    search = input("Введіть слово для пошуку: ")
    replace = input("Введіть слово для заміни: ")
    
    print("\nОберіть тип пошуку:")
    print("1. Простий пошук (заміна всіх входжень)")
    print("2. Пошук повних слів з урахуванням регістру")
    
    choice = input("Ваш вибір (1 або 2): ")
    
    if choice == '1':
        search_and_replace(input_file, output_file, search, replace)
    elif choice == '2':
        search_and_replace_case_sensitive(input_file, output_file, search, replace)
    else:
        print("Невірний вибір. Використовується простий пошук.")
        search_and_replace(input_file, output_file, search, replace)