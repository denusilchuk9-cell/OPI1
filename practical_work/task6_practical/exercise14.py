price = float(input("Введіть ціну товару: "))
discount = float(input("Введіть знижку (%): "))
final_price = price * (1 - discount/100)
print(f"Ціна зі знижкою: {final_price:.2f}")