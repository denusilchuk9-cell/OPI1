"""
ДОМАШНЄ ЗАВДАННЯ
Система управління студентами

Програма дозволяє:
1. Додавати студентів
2. Переглядати список студентів
3. Обчислювати середній бал
4. Визначати статус студента
"""

print("=== СИСТЕМА УПРАВЛІННЯ СТУДЕНТАМИ ===\n")

students = []

def add_student():
    """Додавання нового студента"""
    print("\n" + "="*40)
    print("ДОДАВАННЯ СТУДЕНТА")
    print("="*40)
    
    name = input("Ім'я студента: ")
    
    # Перевірка валідності віку
    while True:
        try:
            age = int(input("Вік студента: "))
            if age < 16 or age > 60:
                print("Вік має бути від 16 до 60 років. Спробуйте ще раз.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть правильний вік (число).")
    
    # Перевірка валідності курсу
    while True:
        try:
            course = int(input("Курс (1-6): "))
            if course < 1 or course > 6:
                print("Курс має бути від 1 до 6. Спробуйте ще раз.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть правильний курс (число).")
    
    # Введення оцінок
    grades = []
    print("Введіть оцінки студента (від 0 до 100). Для завершення введіть 'end':")
    
    while True:
        grade_input = input("Оцінка (або 'end' для завершення): ")
        if grade_input.lower() == 'end':
            break
        
        try:
            grade = float(grade_input)
            if grade < 0 or grade > 100:
                print("Оцінка має бути від 0 до 100. Спробуйте ще раз.")
                continue
            grades.append(grade)
        except ValueError:
            print("Будь ласка, введіть правильну оцінку (число).")
    
    # Створення словника студента
    student = {
        'id': len(students) + 1,
        'name': name,
        'age': age,
        'course': course,
        'grades': grades
    }
    
    students.append(student)
    print(f"\n✅ Студента '{name}' успішно додано!")
    print(f"   ID: {student['id']}")
    print(f"   Кількість оцінок: {len(grades)}")

def view_students():
    """Перегляд списку студентів"""
    print("\n" + "="*40)
    print("СПИСОК СТУДЕНТІВ")
    print("="*40)
    
    if not students:
        print("Список студентів порожній.")
        return
    
    print(f"\nКількість студентів: {len(students)}")
    print("-"*50)
    
    for student in students:
        avg_grade = calculate_average(student['grades'])
        status = determine_status(avg_grade)
        
        print(f"ID: {student['id']}")
        print(f"Ім'я: {student['name']}")
        print(f"Вік: {student['age']}")
        print(f"Курс: {student['course']}")
        print(f"Кількість оцінок: {len(student['grades'])}")
        print(f"Середній бал: {avg_grade:.2f}" if avg_grade > 0 else "Середній бал: немає оцінок")
        print(f"Статус: {status}")
        print("-"*50)

def calculate_average(grades):
    """Обчислення середнього балу"""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def determine_status(average_grade):
    """Визначення статусу студента"""
    if average_grade == 0:
        return "Немає оцінок"
    elif average_grade >= 90:
        return "Відмінник 🏆"
    elif average_grade >= 75:
        return "Добре 👍"
    elif average_grade >= 60:
        return "Задовільно ✅"
    else:
        return "Незадовільно ⚠️"

def view_statistics():
    """Перегляд статистики"""
    print("\n" + "="*40)
    print("СТАТИСТИКА СТУДЕНТІВ")
    print("="*40)
    
    if not students:
        print("Немає студентів для статистики.")
        return
    
    total_students = len(students)
    total_grades = sum(len(student['grades']) for student in students)
    
    # Середній бал всіх студентів
    all_grades = []
    for student in students:
        all_grades.extend(student['grades'])
    
    overall_average = calculate_average(all_grades) if all_grades else 0
    
    # Статистика по курсах
    courses_stats = {}
    for student in students:
        course = student['course']
        if course not in courses_stats:
            courses_stats[course] = {'count': 0, 'grades': []}
        
        courses_stats[course]['count'] += 1
        courses_stats[course]['grades'].extend(student['grades'])
    
    # Статистика за статусами
    status_stats = {
        'Відмінник 🏆': 0,
        'Добре 👍': 0,
        'Задовільно ✅': 0,
        'Незадовільно ⚠️': 0,
        'Немає оцінок': 0
    }
    
    for student in students:
        avg_grade = calculate_average(student['grades'])
        status = determine_status(avg_grade)
        status_stats[status] += 1
    
    print(f"\n📊 ЗАГАЛЬНА СТАТИСТИКА:")
    print(f"   Кількість студентів: {total_students}")
    print(f"   Всього оцінок: {total_grades}")
    print(f"   Середній бал всіх студентів: {overall_average:.2f}")
    
    print(f"\n📚 СТАТИСТИКА ПО КУРСАХ:")
    for course in sorted(courses_stats.keys()):
        avg = calculate_average(courses_stats[course]['grades'])
        print(f"   Курс {course}: {courses_stats[course]['count']} студентів, середній бал: {avg:.2f}")
    
    print(f"\n🏅 РОЗПОДІЛ ЗА СТАТУСАМИ:")
    for status, count in status_stats.items():
        if count > 0:
            percentage = (count / total_students) * 100
            print(f"   {status}: {count} студентів ({percentage:.1f}%)")

def find_student():
    """Пошук студента"""
    print("\n" + "="*40)
    print("ПОШУК СТУДЕНТА")
    print("="*40)
    
    search_type = input("Пошук за:\n1. ID\n2. Імені\n3. Курсу\nВиберіть варіант (1-3): ")
    
    results = []
    
    if search_type == "1":
        try:
            search_id = int(input("Введіть ID студента: "))
            results = [student for student in students if student['id'] == search_id]
        except ValueError:
            print("Невірний формат ID.")
    
    elif search_type == "2":
        search_name = input("Введіть ім'я студента: ").lower()
        results = [student for student in students if search_name in student['name'].lower()]
    
    elif search_type == "3":
        try:
            search_course = int(input("Введіть курс: "))
            results = [student for student in students if student['course'] == search_course]
        except ValueError:
            print("Невірний формат курсу.")
    
    else:
        print("Невірний вибір.")
        return
    
    if not results:
        print("Студентів не знайдено.")
    else:
        print(f"\nЗнайдено {len(results)} студентів:")
        print("-"*50)
        
        for student in results:
            avg_grade = calculate_average(student['grades'])
            status = determine_status(avg_grade)
            
            print(f"ID: {student['id']}")
            print(f"Ім'я: {student['name']}")
            print(f"Вік: {student['age']}")
            print(f"Курс: {student['course']}")
            print(f"Середній бал: {avg_grade:.2f}" if avg_grade > 0 else "Середній бал: немає оцінок")
            print(f"Статус: {status}")
            print("Оцінки:", ", ".join(map(str, student['grades'])) if student['grades'] else "немає оцінок")
            print("-"*50)

def edit_student():
    """Редагування даних студента"""
    print("\n" + "="*40)
    print("РЕДАГУВАННЯ СТУДЕНТА")
    print("="*40)
    
    if not students:
        print("Немає студентів для редагування.")
        return
    
    view_students()
    
    try:
        student_id = int(input("\nВведіть ID студента для редагування: "))
        
        # Пошук студента за ID
        student = None
        for s in students:
            if s['id'] == student_id:
                student = s
                break
        
        if not student:
            print("Студента з таким ID не знайдено.")
            return
        
        print(f"\nРедагування студента: {student['name']}")
        print("="*30)
        
        print("\nЩо бажаєте редагувати?")
        print("1. Ім'я")
        print("2. Вік")
        print("3. Курс")
        print("4. Оцінки")
        
        choice = input("Виберіть опцію (1-4): ")
        
        if choice == "1":
            new_name = input(f"Нове ім'я (поточне: {student['name']}): ")
            if new_name.strip():
                student['name'] = new_name
                print("Ім'я змінено успішно.")
        
        elif choice == "2":
            while True:
                try:
                    new_age = int(input(f"Новий вік (поточний: {student['age']}): "))
                    if 16 <= new_age <= 60:
                        student['age'] = new_age
                        print("Вік змінено успішно.")
                        break
                    else:
                        print("Вік має бути від 16 до 60 років.")
                except ValueError:
                    print("Будь ласка, введіть правильний вік.")
        
        elif choice == "3":
            while True:
                try:
                    new_course = int(input(f"Новий курс (поточний: {student['course']}): "))
                    if 1 <= new_course <= 6:
                        student['course'] = new_course
                        print("Курс змінено успішно.")
                        break
                    else:
                        print("Курс має бути від 1 до 6.")
                except ValueError:
                    print("Будь ласка, введіть правильний курс.")
        
        elif choice == "4":
            print("\nПоточні оцінки:", student['grades'] if student['grades'] else "немає оцінок")
            print("\nОпції редагування оцінок:")
            print("1. Додати нову оцінку")
            print("2. Видалити оцінку")
            
            grade_choice = input("Виберіть опцію (1-2): ")
            
            if grade_choice == "1":
                while True:
                    try:
                        new_grade = float(input("Введіть нову оцінку (0-100): "))
                        if 0 <= new_grade <= 100:
                            student['grades'].append(new_grade)
                            print("Оцінку додано успішно.")
                            break
                        else:
                            print("Оцінка має бути від 0 до 100.")
                    except ValueError:
                        print("Будь ласка, введіть правильну оцінку.")
            
            elif grade_choice == "2" and student['grades']:
                print("Поточні оцінки:")
                for i, grade in enumerate(student['grades'], 1):
                    print(f"{i}. {grade}")
                
                try:
                    grade_index = int(input("Введіть номер оцінки для видалення: ")) - 1
                    if 0 <= grade_index < len(student['grades']):
                        removed_grade = student['grades'].pop(grade_index)
                        print(f"Оцінку {removed_grade} видалено успішно.")
                    else:
                        print("Невірний номер оцінки.")
                except ValueError:
                    print("Будь ласка, введіть правильний номер.")
            
            else:
                print("Немає оцінок для видалення або невірний вибір.")
        
        else:
            print("Невірний вибір.")
    
    except ValueError:
        print("Невірний формат ID.")

def delete_student():
    """Видалення студента"""
    print("\n" + "="*40)
    print("ВИДАЛЕННЯ СТУДЕНТА")
    print("="*40)
    
    if not students:
        print("Немає студентів для видалення.")
        return
    
    view_students()
    
    try:
        student_id = int(input("\nВведіть ID студента для видалення: "))
        
        # Пошук індексу студента
        student_index = -1
        for i, student in enumerate(students):
            if student['id'] == student_id:
                student_index = i
                break
        
        if student_index == -1:
            print("Студента з таким ID не знайдено.")
            return
        
        # Підтвердження видалення
        student_to_delete = students[student_index]
        confirm = input(f"Ви впевнені, що хочете видалити студента '{student_to_delete['name']}'? (так/ні): ")
        
        if confirm.lower() == 'так':
            deleted_student = students.pop(student_index)
            print(f"Студента '{deleted_student['name']}' успішно видалено.")
        else:
            print("Видалення скасовано.")
    
    except ValueError:
        print("Невірний формат ID.")

def main_menu():
    """Головне меню програми"""
    while True:
        print("\n" + "="*40)
        print("ГОЛОВНЕ МЕНЮ")
        print("="*40)
        print("1. Додати нового студента")
        print("2. Переглянути всіх студентів")
        print("3. Знайти студента")
        print("4. Редагувати дані студента")
        print("5. Видалити студента")
        print("6. Переглянути статистику")
        print("7. Вийти з програми")
        print("="*40)
        
        choice = input("Виберіть опцію (1-7): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            find_student()
        elif choice == "4":
            edit_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            view_statistics()
        elif choice == "7":
            print("\nДякую за використання програми!")
            print("Завершення роботи...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
        
        # Пауза перед наступним меню
        if choice != "7":
            input("\nНатисніть Enter для продовження...")

# Запуск програми
if __name__ == "__main__":
    print("Ласкаво просимо до системи управління студентами!")
    print("Розробник: [Ваше ім'я]")
    print("Версія: 1.0")
    
    # Додамо декілька тестових студентів для прикладу
    test_students = [
        {
            'id': 1,
            'name': 'Іван Петренко',
            'age': 19,
            'course': 2,
            'grades': [85, 92, 78, 90]
        },
        {
            'id': 2,
            'name': 'Марія Коваленко',
            'age': 20,
            'course': 3,
            'grades': [95, 98, 92, 96]
        },
        {
            'id': 3,
            'name': 'Олексій Сидоренко',
            'age': 18,
            'course': 1,
            'grades': [65, 58, 72, 60]
        }
    ]
    
    # Запитуємо, чи додати тестових студентів
    add_test = input("\nБажаєте додати тестових студентів? (так/ні): ")
    if add_test.lower() == 'так':
        students.extend(test_students)
        print("Додано 3 тестових студенти.")
    
    main_menu()