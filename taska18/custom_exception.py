class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Негативне число не допускається: {value}")

def process_positive_numbers():
    numbers = []
    while True:
        try:
            value = input("Введіть додатнє число (або 'stop' для завершення): ")
            if value.lower() == 'stop':
                break
            
            num = float(value)
            if num < 0:
                raise NegativeNumberError(num)
            
            numbers.append(num)
            print(f"Додано число: {num}")
            
        except NegativeNumberError as e:
            print(f"Помилка: {e}")
        except ValueError:
            print("Помилка: введіть коректне число!")
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"Середнє додатніх чисел: {average}")
    else:
        print("Не введено жодного додатнього числа.")

if __name__ == "__main__":
    process_positive_numbers()