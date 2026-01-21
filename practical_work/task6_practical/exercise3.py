weight = float(input("Введіть вагу (кг): "))
height = float(input("Введіть зріст (м): "))
bmi = weight / (height ** 2)
print(f"Ваш ІМТ: {bmi:.2f}")