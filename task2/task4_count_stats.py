# task4_count_stats.py

def count_file_stats(filename):
    """
    Функція для підрахунку рядків, слів та символів у файлі
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        lines = content.split('\n')
        if lines[-1] == '':
            lines = lines[:-1]
        line_count = len(lines)
        words = content.split()
        word_count = len(words)
        
        char_count = len(content)
        
        char_count_no_spaces = len(content.replace(' ', '').replace('\n', ''))
        
        # Виведення результатів
        print(f"Статистика для файлу '{filename}':")
        print("-" * 40)
        print(f"Кількість рядків: {line_count}")
        print(f"Кількість слів: {word_count}")
        print(f"Кількість символів (з пробілами): {char_count}")
        print(f"Кількість символів (без пробілів): {char_count_no_spaces}")
        
        print("\nЧастота 10 найбільш вживаних слів:")
        from collections import Counter
        
        clean_words = []
        for word in words:
            clean_word = word.strip('.,!?;:()[]{}"\'').lower()
            if clean_word:
                clean_words.append(clean_word)
        
        word_freq = Counter(clean_words)
        
        # Виведення 10 найбільш вживаних слів
        for word, count in word_freq.most_common(10):
            print(f"  '{word}': {count} разів")
    
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    filename = input("Введіть ім'я файлу для аналізу: ")
    count_file_stats(filename)