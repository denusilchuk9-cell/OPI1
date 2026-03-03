from abc import ABC, abstractmethod

# ========== Person (абстрактний клас) ==========
class Person(ABC):
    def __init__(self, name, age, address):
        if not name or not name.strip():
            raise ValueError("Ім'я не може бути порожнім")
        if age < 0 or age > 150:
            raise ValueError("Вік має бути від 0 до 150")
        if not address or not address.strip():
            raise ValueError("Адреса не може бути порожньою")
        
        self._name = name
        self._age = age
        self._address = address
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        if not value or not value.strip():
            raise ValueError("Адреса не може бути порожньою")
        self._address = value
    
    @abstractmethod
    def get_role(self):
        pass
    
    def get_info(self):
        return f"Ім'я: {self._name}, Вік: {self._age}"

# ========== Student ==========
class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self._student_id = student_id
        self._grades = {}
    
    @property
    def student_id(self):
        return self._student_id
    
    @property
    def gpa(self):
        if not self._grades:
            return 0
        total = sum(self._grades.values())
        return total / len(self._grades)
    
    def get_role(self):
        return "Студент"
    
    def get_info(self):
        return f"{super().get_info()}, ID: {self._student_id}, Роль: {self.get_role()}, GPA: {self.gpa:.2f}"
    
    def add_grade(self, course_name, grade):
        self._grades[course_name] = grade

# ========== Instructor ==========
class Instructor(Person):
    def __init__(self, name, age, address, salary, department):
        super().__init__(name, age, address)
        self._salary = salary
        self._department = department
    
    @property
    def salary(self):
        return self._salary
    
    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, value):
        self._department = value
    
    def get_role(self):
        return "Викладач"
    
    def get_info(self):
        return f"{super().get_info()}, Департамент: {self._department}"

# ========== Course ==========
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self._students = []
        self._instructor = None
    
    @property
    def instructor(self):
        return self._instructor
    
    def enroll_student(self, student):
        if student not in self._students:
            self._students.append(student)
            print(f"Студента {student.name} додано до курсу {self.course_name}")
    
    def assign_instructor(self, instructor):
        self._instructor = instructor
        print(f"Викладач {instructor.name} призначений на курс {self.course_name}")
    
    def get_enrolled_students(self):
        return [student.name for student in self._students]

# ========== Головна функція ==========
def main():
    print("=== Система Університету ===\n")
    
    student1 = Student("Олександр Петренко", 20, "Київ, вул. Хрещатик 1", "ST12345")
    student2 = Student("Марія Іваненко", 19, "Львів, вул. Лесі Українки 5", "ST67890")
    teacher = Instructor("Дмитро Коваленко", 45, "Одеса, вул. Дерибасівська 10", 25000, "Інженерії")
    
    student1.add_grade("Математика", 95.5)
    student1.add_grade("Фізика", 88.0)
    student2.add_grade("Математика", 92.0)
    
    math_course = Course("Вища математика", "MATH101")
    
    math_course.assign_instructor(teacher)
    math_course.enroll_student(student1)
    math_course.enroll_student(student2)
    
    print("\n=== Інформація про учасників ===")
    people = [student1, student2, teacher]
    
    for person in people:
        print(person.get_info())
    
    print(f"\nСередній бал {student1.name}: {student1.gpa:.2f}")
    print(f"Середній бал {student2.name}: {student2.gpa:.2f}")

if __name__ == "__main__":
    main()