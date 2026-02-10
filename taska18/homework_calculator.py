class CalculationError(Exception):
    pass

class InvalidOperatorError(CalculationError):
    def __init__(self, operator):
        self.operator = operator
        super().__init__(f"Невідомий оператор: {operator}")

class NumberOutOfRangeError(CalculationError):
    def __init__(self, number, min_val, max_val):
        self.number = number
        super().__init__(f"Число {number} не в діапазоні {min_val}-{max_val}")

class AdvancedCalculator:
    def __init__(self, min_value=-1000, max_value=1000):
        self.min_value = min_value
        self.max_value = max_value
    
    def validate_number(self, num):
        if not (self.min_value <= num <= self.max_value):
            raise NumberOutOfRangeError(num, self.min_value, self.max_value)
    
    def calculate(self):
        print("Розширений калькулятор")
        print("Доступні операції: +, -, *, /, ^ (степінь), % (залишок)")
        
        while True:
            try:
                num1 = float(input("Введіть перше число: "))
                self.validate_number(num1)
                
                operator = input("Введіть оператор: ")
                if operator not in ['+', '-', '*', '/', '^', '%']:
                    raise InvalidOperatorError(operator)
                
                num2 = float(input("Введіть друге число: "))
                self.validate_number(num2)
                
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    if num2 == 0:
                        raise ZeroDivisionError("Ділення на нуль неможливе!")
                    result = num1 / num2
                elif operator == '^':
                    result = num1 ** num2
                elif operator == '%':
                    if num2 == 0:
                        raise ZeroDivisionError("Залишок від ділення на нуль не визначено!")
                    result = num1 % num2
                
                self.validate_number(result)
                print(f"Результат: {result:.2f}")
                
                choice = input("Продовжити? (так/ні): ").lower()
                if choice != 'так':
                    print("Дякую за використання калькулятора!")
                    break
                    
            except ValueError:
                print("Помилка: введіть коректні числа!")
            except ZeroDivisionError as e:
                print(f"Помилка: {e}")
            except InvalidOperatorError as e:
                print(f"Помилка: {e}")
            except NumberOutOfRangeError as e:
                print(f"Помилка: {e}")
            except OverflowError:
                print("Помилка: результат занадто великий!")
            except Exception as e:
                print(f"Несподівана помилка: {type(e).__name__}")
            finally:
                print("-" * 40)

if __name__ == "__main__":
    calc = AdvancedCalculator()
    calc.calculate()