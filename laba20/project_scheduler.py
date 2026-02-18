class ProjectTask:
    def __init__(self, name, duration, dependencies=None):
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.early_start = 0
        self.early_finish = 0
        self.late_start = 0
        self.late_finish = 0
        self.slack = 0

class ProjectScheduler:
    def __init__(self, name):
        self.name = name
        self.tasks = {}
        self.start_date = None
    
    def add_task(self, task):
        self.tasks[task.name] = task
    
    def calculate_critical_path(self):
        # Forward pass
        for task in self.tasks.values():
            if not task.dependencies:
                task.early_start = 0
            else:
                task.early_start = max(self.tasks[dep].early_finish for dep in task.dependencies)
            task.early_finish = task.early_start + task.duration
        
        # Backward pass
        project_duration = max(task.early_finish for task in self.tasks.values())
        for task in reversed(list(self.tasks.values())):
            if not any(task.name in t.dependencies for t in self.tasks.values()):
                task.late_finish = project_duration
            else:
                task.late_finish = min(self.tasks[t.name].late_start for t in self.tasks.values() 
                                      if task.name in t.dependencies)
            task.late_start = task.late_finish - task.duration
            task.slack = task.late_start - task.early_start
        
        # Find critical path
        critical_path = [task.name for task in self.tasks.values() if task.slack == 0]
        return critical_path, project_duration
    
    def print_gantt_chart(self):
        print(f"\n{'='*60}")
        print(f"ДІАГРАМА ГАНТА - {self.name}")
        print(f"{'='*60}")
        
        max_name_length = max(len(task.name) for task in self.tasks.values())
        project_duration = max(task.early_finish for task in self.tasks.values())
        
        for task in self.tasks.values():
            print(f"{task.name.ljust(max_name_length)} | ", end="")
            for day in range(project_duration + 1):
                if task.early_start <= day < task.early_finish:
                    print("█", end="")
                else:
                    print("░", end="")
            print(f" | ({task.duration} днів)")
    
    def print_task_table(self):
        print(f"\n{'='*80}")
        print(f"ТАБЛИЦЯ ЗАВДАНЬ - {self.name}")
        print(f"{'='*80}")
        print(f"{'Завдання':<20} {'Трив':<6} {'Залежності':<20} {'ES':<5} {'EF':<5} {'LS':<5} {'LF':<5} {'Slack':<6}")
        print(f"{'-'*80}")
        
        for task in self.tasks.values():
            deps = ', '.join(task.dependencies) if task.dependencies else '-'
            print(f"{task.name:<20} {task.duration:<6} {deps:<20} {task.early_start:<5} "
                  f"{task.early_finish:<5} {task.late_start:<5} {task.late_finish:<5} {task.slack:<6}")
    
    def print_resource_allocation(self, resources):
        print(f"\n{'='*70}")
        print(f"РОЗПОДІЛ РЕСУРСІВ - {self.name}")
        print(f"{'='*70}")
        
        for task_name, task_resources in resources.items():
            if task_name in self.tasks:
                print(f"\n{task_name}:")
                for resource, quantity in task_resources.items():
                    print(f"  - {resource}: {quantity}")

class Resource:
    def __init__(self, name, type, cost_per_day=None):
        self.name = name
        self.type = type  # human, software, hardware
        self.cost_per_day = cost_per_day

class Risk:
    def __init__(self, name, probability, impact, mitigation_strategy):
        self.name = name
        self.probability = probability  # 0-1
        self.impact = impact  # low, medium, high
        self.mitigation_strategy = mitigation_strategy
        self.risk_score = self.calculate_risk_score()
    
    def calculate_risk_score(self):
        impact_score = {'low': 1, 'medium': 2, 'high': 3}[self.impact]
        return self.probability * impact_score

def main():
    print("="*70)
    print("СИСТЕМА УПРАВЛІННЯ ПРОЄКТОМ TASKMASTER")
    print("="*70)
    
    # Створення проєкту
    project = ProjectScheduler("TaskMaster - Веб-додаток для керування завданнями")
    
    # Додавання завдань
    tasks = [
        ProjectTask("Аналіз вимог", 5),
        ProjectTask("Прототип інтерфейсу", 4, ["Аналіз вимог"]),
        ProjectTask("Проєктування БД", 3, ["Аналіз вимог"]),
        ProjectTask("Налаштування середовища", 2, ["Аналіз вимог"]),
        ProjectTask("Розробка бекенду", 10, ["Проєктування БД", "Налаштування середовища"]),
        ProjectTask("Розробка API", 7, ["Розробка бекенду"]),
        ProjectTask("Розробка фронтенду", 12, ["Прототип інтерфейсу", "Розробка API"]),
        ProjectTask("Інтеграція", 5, ["Розробка фронтенду", "Розробка API"]),
        ProjectTask("Тестування", 6, ["Інтеграція"]),
        ProjectTask("Виправлення помилок", 4, ["Тестування"]),
        ProjectTask("Деплой", 3, ["Виправлення помилок"]),
        ProjectTask("Документація", 4, ["Тестування"]),
        ProjectTask("Презентація", 2, ["Деплой", "Документація"])
    ]
    
    for task in tasks:
        project.add_task(task)
    
    # Розрахунок критичного шляху
    critical_path, duration = project.calculate_critical_path()
    
    # Виведення результатів
    project.print_task_table()
    
    print(f"\nКРИТИЧНИЙ ШЛЯХ:")
    print(f"{' → '.join(critical_path)}")
    print(f"Загальна тривалість проєкту: {duration} днів")
    
    project.print_gantt_chart()
    
    # Ресурси
    resources = {
        "Аналіз вимог": {"Project Manager": 1, "Аналітик": 1},
        "Прототип інтерфейсу": {"UI/UX Designer": 1},
        "Проєктування БД": {"Backend Developer": 1, "DBA": 1},
        "Налаштування середовища": {"DevOps": 1},
        "Розробка бекенду": {"Backend Developer": 2},
        "Розробка API": {"Backend Developer": 2},
        "Розробка фронтенду": {"Frontend Developer": 2},
        "Інтеграція": {"Backend Developer": 1, "Frontend Developer": 1},
        "Тестування": {"QA Engineer": 2},
        "Виправлення помилок": {"Backend Developer": 1, "Frontend Developer": 1},
        "Деплой": {"DevOps": 1},
        "Документація": {"Technical Writer": 1},
        "Презентація": {"Project Manager": 1}
    }
    
    project.print_resource_allocation(resources)
    
    # Ризики
    print(f"\n{'='*60}")
    print("УПРАВЛІННЯ РИЗИКАМИ")
    print(f"{'='*60}")
    
    risks = [
        Risk("Технічні проблеми", 0.4, "high", "Резерв часу, код-рев'ю, спліт-тестування"),
        Risk("Відставання від графіка", 0.6, "high", "Щоденні стендапи, корекція пріоритетів"),
        Risk("Зміна вимог", 0.5, "medium", "Гнучка методологія, пріоритезація"),
        Risk("Проблеми з інтеграцією", 0.3, "high", "Раннє тестування, CI/CD"),
        Risk("Хвороба членів команди", 0.2, "medium", "Крос-функціональність, документація")
    ]
    
    print(f"\n{'Ризик':<30} {'Ймовірність':<12} {'Вплив':<8} {'Оцінка':<8} {'Стратегія'}")
    print(f"{'-'*90}")
    
    for risk in risks:
        print(f"{risk.name:<30} {risk.probability:<12} {risk.impact:<8} "
              f"{risk.risk_score:<8.1f} {risk.mitigation_strategy}")
    
    # Звіт по проєкту
    print(f"\n{'='*60}")
    print("ПІДСУМКОВИЙ ЗВІТ")
    print(f"{'='*60}")
    print(f"Проєкт: TaskMaster")
    print(f"Тривалість: {duration} днів ({duration//5} тижнів)")
    print(f"Кількість завдань: {len(project.tasks)}")
    print(f"Критичний шлях: {' → '.join(critical_path)}")
    print(f"Критичних завдань: {len(critical_path)}")
    print(f"Ресурси: 7 спеціалістів + інструменти")
    print(f"Ризиків: {len(risks)}")
    print(f"Статус: Готовий до виконання")

if __name__ == "__main__":
    main()