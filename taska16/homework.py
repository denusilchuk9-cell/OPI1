def run_homework():
    print("\n" + "="*60)
    print("ДОМАШНЄ ЗАВДАННЯ: СИСТЕМА УПРАВЛІННЯ БІБЛІОТЕКОЮ")
    print("="*60)
    
    library_system()

def library_system():
    books = [
        ("1984", "Джордж Орвелл", 1949, "Фантастика", True),
        ("Гаррі Поттер і філософський камінь", "Дж.К. Роулінг", 1997, "Фентезі", True),
        ("Війна і мир", "Лев Толстой", 1869, "Класика", False),
        ("Мастер і Маргарита", "Михайло Булгаков", 1967, "Класика", True),
        ("Місто гріхів", "Френк Міллер", 1991, "Графічний роман", True),
    ]
    
    borrowed_books = []
    
    def display_books():
        print("\n" + "-"*60)
        print("КНИГИ В БІБЛІОТЕЦІ")
        print("-"*60)
        for i, (title, author, year, genre, available) in enumerate(books, 1):
            status = "Доступна" if available else "Видана"
            print(f"{i}. {title}")
            print(f"   Автор: {author}, Рік: {year}, Жанр: {genre}, Статус: {status}")
    
    def add_book():
        print("\n--- Додати нову книгу ---")
        title = input("Назва книги: ")
        author = input("Автор: ")
        year = int(input("Рік видання: "))
        genre = input("Жанр: ")
        books.append((title, author, year, genre, True))
        print(f"Книга '{title}' додана до бібліотеки!")
    
    def borrow_book():
        display_books()
        try:
            book_num = int(input("\nНомер книги для позичення: "))
            if 1 <= book_num <= len(books):
                title, author, year, genre, available = books[book_num-1]
                if available:
                    books[book_num-1] = (title, author, year, genre, False)
                    borrowed_books.append((title, author))
                    print(f"Ви позичили книгу '{title}'!")
                else:
                    print("Ця книга вже позичена!")
            else:
                print("Невірний номер книги!")
        except ValueError:
            print("Введіть коректний номер!")
    
    def return_book():
        if not borrowed_books:
            print("Немає позичених книг!")
            return
        
        print("\n--- Повернення книги ---")
        print("Позичені книги:")
        for i, (title, author) in enumerate(borrowed_books, 1):
            print(f"{i}. {title} ({author})")
        
        try:
            book_num = int(input("Номер книги для повернення: "))
            if 1 <= book_num <= len(borrowed_books):
                title, author = borrowed_books.pop(book_num-1)
                
                for i, (b_title, b_author, year, genre, available) in enumerate(books):
                    if b_title == title and b_author == author:
                        books[i] = (b_title, b_author, year, genre, True)
                        break
                
                print(f"Книга '{title}' повернена!")
            else:
                print("Невірний номер!")
        except ValueError:
            print("Введіть коректний номер!")
    
    def search_books():
        print("\n--- Пошук книг ---")
        print("1. За назвою")
        print("2. За автором")
        print("3. За жанром")
        
        choice = input("Оберіть критерій пошуку: ")
        search_term = input("Введіть пошуковий запит: ").lower()
        
        results = []
        
        if choice == "1":
            results = [book for book in books if search_term in book[0].lower()]
        elif choice == "2":
            results = [book for book in books if search_term in book[1].lower()]
        elif choice == "3":
            results = [book for book in books if search_term in book[3].lower()]
        else:
            print("Невірний вибір!")
            return
        
        if results:
            print(f"\nЗнайдено {len(results)} книг:")
            for i, (title, author, year, genre, available) in enumerate(results, 1):
                status = "Доступна" if available else "Видана"
                print(f"{i}. {title} ({author}) - {genre}, {year}, {status}")
        else:
            print("Книг не знайдено!")
    
    def statistics():
        print("\n--- Статистика бібліотеки ---")
        total_books = len(books)
        available_books = sum(1 for book in books if book[4])
        borrowed_count = len(borrowed_books)
        
        genres = {}
        for _, _, _, genre, _ in books:
            genres[genre] = genres.get(genre, 0) + 1
        
        print(f"Загальна кількість книг: {total_books}")
        print(f"Доступних книг: {available_books}")
        print(f"Позичених книг: {borrowed_count}")
        
        print("\nРозподіл за жанрами:")
        for genre, count in genres.items():
            percentage = (count / total_books) * 100
            print(f"  {genre}: {count} книг ({percentage:.1f}%)")
        
        if books:
            oldest = min(books, key=lambda x: x[2])
            newest = max(books, key=lambda x: x[2])
            print(f"\nНайстаріша книга: {oldest[0]} ({oldest[2]} рік)")
            print(f"Найновіша книга: {newest[0]} ({newest[2]} рік)")
    
    while True:
        print("\n" + "="*60)
        print("СИСТЕМА УПРАВЛІННЯ БІБЛІОТЕКОЮ")
        print("="*60)
        print("1. Переглянути всі книги")
        print("2. Додати нову книгу")
        print("3. Позичити книгу")
        print("4. Повернути книгу")
        print("5. Пошук книг")
        print("6. Статистика")
        print("7. Сортувати книги")
        print("0. Вийти")
        
        choice = input("\nОберіть опцію: ")
        
        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            search_books()
        elif choice == "6":
            statistics()
        elif choice == "7":
            print("\n--- Сортування книг ---")
            print("1. За назвою")
            print("2. За автором")
            print("3. За роком видання")
            print("4. За жанром")
            
            sort_choice = input("Оберіть критерій сортування: ")
            
            if sort_choice == "1":
                books.sort(key=lambda x: x[0])
                print("Відсортовано за назвою!")
            elif sort_choice == "2":
                books.sort(key=lambda x: x[1])
                print("Відсортовано за автором!")
            elif sort_choice == "3":
                books.sort(key=lambda x: x[2])
                print("Відсортовано за роком видання!")
            elif sort_choice == "4":
                books.sort(key=lambda x: x[3])
                print("Відсортовано за жанром!")
            else:
                print("Невірний вибір!")
        elif choice == "0":
            print("Дякуємо за використання системи!")
            break
        else:
            print("Невірний вибір!")
    
    print("\n" + "="*60)
    print("ОСОБЛИВОСТІ РЕАЛІЗАЦІЇ:")
    print("="*60)
    print("1. Використані структури даних:")
    print("   - Список кортежів для зберігання книг")
    print("   - Список кортежів для позичених книг")
    print("   - Словник для статистики жанрів")
    print("\n2. Переваги обраних структур:")
    print("   - Кортежі: незмінність, швидкий доступ")
    print("   - Списки: динамічність, зручність модифікації")
    print("   - Словники: швидкий пошук, зручна статистика")
    print("\n3. Функціонал системи:")
    print("   - CRUD операції з книгами")
    print("   - Пошук та сортування")
    print("   - Статистичний аналіз")
    print("   - Управління позиками")