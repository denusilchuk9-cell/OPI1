number = input("Введіть число: ")
sum_digits = sum(int(digit) for digit in number)
print(f"Сума цифр числа {number}: {sum_digits}")