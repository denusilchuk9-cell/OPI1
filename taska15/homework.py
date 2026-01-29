"""
Домашнє завдання: Власна програма з циклами та функціями
"""

def run_homework():
    """Виконання домашнього завдання"""
    print("\n" + "="*50)
    print("ДОМАШНЄ ЗАВДАННЯ")
    print("="*50)
    print("\nПРОГРАМА: АНАЛІЗ ТЕКСТУ ТА СТАТИСТИКА")
    print("-"*50)
    
    # Основна програма
    text_analyzer()

def text_analyzer():
    """
    Програма для аналізу тексту:
    1. Підрахунок слів, символів, речень
    2. Аналіз частоти слів
    3. Пошук найдовших/найкоротших слів
    4. Статистика унікальних слів
    """
    
    def get_text_from_user():
        """Отримання тексту від користувача"""
        print("\nВведіть текст для аналізу (або натисніть Enter для використання тестового тексту):")
        user_text = input()
        
        if not user_text.strip():
            # Тестовий текст за замовчуванням
            test_text = """
            Python - це мова програмування високого рівня, яка широко використовується 
            для розробки веб-додатків, наукових досліджень, аналізу даних, 
            штучного інтелекту та автоматизації завдань. Мова відрізняється 
            простотою синтаксису та читабельністю коду, що робить її популярною 
            серед початківців та досвідчених розробників.
            """
            print("\nВикористовується тестовий текст.")
            return test_text
        return user_text
    
    def count_words(text):
        """Підрахунок слів у тексті"""
        words = text.split()
        return len(words)
    
    def count_characters(text):
        """Підрахунок символів у тексті"""
        return len(text)
    
    def count_sentences(text):
        """Підрахунок речень у тексті"""
        sentence_endings = ['.', '!', '?']
        count = 0
        for char in text:
            if char in sentence_endings:
                count += 1
        return count
    
    def get_word_frequency(text):
        """Аналіз частоти слів"""
        # Очищення тексту
        import string
        cleaned_text = text.lower()
        for punct in string.punctuation:
            cleaned_text = cleaned_text.replace(punct, '')
        
        words = cleaned_text.split()
        frequency = {}
        
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        
        # Сортування за частотою
        sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return sorted_freq[:10]  # Топ-10 слів
    
    def find_longest_shortest_words(text):
        """Пошук найдовших та найкоротших слів"""
        import string
        cleaned_text = text.lower()
        for punct in string.punctuation:
            cleaned_text = cleaned_text.replace(punct, '')
        
        words = cleaned_text.split()
        
        if not words:
            return None, None
        
        longest = max(words, key=len)
        shortest = min(words, key=len)
        
        # Знайти всі слова з такою ж довжиною
        all_longest = [w for w in words if len(w) == len(longest)]
        all_shortest = [w for w in words if len(w) == len(shortest)]
        
        return list(set(all_longest)), list(set(all_shortest))
    
    def calculate_readability(text):
        """Обчислення індексу читабельності"""
        words = text.split()
        sentences = count_sentences(text)
        
        if words == 0 or sentences == 0:
            return 0
        
        # Підрахунок складних слів (слово з 3+ складів)
        complex_words = 0
        vowels = "аеиіоуяюєїАЕИІОУЯЮЄЇ"
        
        for word in words:
            syllable_count = 0
            for char in word:
                if char in vowels:
                    syllable_count += 1
            
            if syllable_count >= 3:
                complex_words += 1
        
        # Індекс читабельності
        readability = 206.835 - 1.015 * (len(words)/sentences) - 84.6 * (complex_words/len(words))
        return readability
    
    def display_statistics(stats):
        """Виведення статистики"""
        print("\n" + "="*50)
        print("РЕЗУЛЬТАТИ АНАЛІЗУ ТЕКСТУ")
        print("="*50)
        
        for key, value in stats.items():
            if isinstance(value, float):
                print(f"{key}: {value:.2f}")
            elif isinstance(value, list):
                print(f"{key}:")
                for item in value:
                    print(f"  - {item}")
            else:
                print(f"{key}: {value}")
    
    # Основна логіка програми
    text = get_text_from_user()
    
    # Обчислення статистики
    stats = {
        "Загальна кількість символів": count_characters(text),
        "Загальна кількість слів": count_words(text),
        "Кількість речень": count_sentences(text),
        "Середня довжина слова": count_characters(text) / max(count_words(text), 1),
        "Середня довжина речення": count_words(text) / max(count_sentences(text), 1),
    }
    
    # Частота слів
    top_words = get_word_frequency(text)
    stats["Топ-10 найчастіших слів"] = [f"{word} ({count})" for word, count in top_words]
    
    # Найдовші та найкоротші слова
    longest, shortest = find_longest_shortest_words(text)
    if longest:
        stats["Найдовші слова"] = longest
    if shortest:
        stats["Найкоротші слова"] = shortest
    
    # Читабельність
    readability = calculate_readability(text)
    stats["Індекс читабельності"] = readability
    
    if readability > 80:
        stats["Рівень читабельності"] = "Дуже легкий"
    elif readability > 60:
        stats["Рівень читабельності"] = "Легкий"
    elif readability > 40:
        stats["Рівень читабельності"] = "Помірний"
    elif readability > 20:
        stats["Рівень читабельності"] = "Складний"
    else:
        stats["Рівень читабельності"] = "Дуже складний"
    
    # Виведення результатів
    display_statistics(stats)
    
    # Додатковий аналіз
    print("\n" + "-"*50)
    print("ДОДАТКОВИЙ АНАЛІЗ")
    print("-"*50)
    
    # Аналіз довжини слів
    word_lengths = {}
    for word in text.split():
        length = len(word)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1
    
    print("\nРозподіл слів за довжиною:")
    for length in sorted(word_lengths.keys()):
        print(f"  {length} символів: {word_lengths[length]} слів")
    
    # Графік розподілу
    print("\nВізуалізація розподілу:")
    max_count = max(word_lengths.values()) if word_lengths else 0
    for length in sorted(word_lengths.keys()):
        bar = '█' * int(word_lengths[length] / max_count * 20) if max_count > 0 else ''
        print(f"  {length:2} сим. [{bar}] {word_lengths[length]}")