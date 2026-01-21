month = int(input("Введіть номер місяця (1-12): "))
if 3 <= month <= 5:
    season = "весна"
elif 6 <= month <= 8:
    season = "літо"
elif 9 <= month <= 11:
    season = "осінь"
else:
    season = "зима"
print(f"Місяць {month} - це {season}")