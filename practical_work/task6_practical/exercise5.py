year = int(input("Введіть рік: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} - високосний рік")
else:
    print(f"{year} - не високосний рік")