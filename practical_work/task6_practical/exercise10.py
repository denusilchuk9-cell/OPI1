seconds = int(input("Введіть кількість секунд: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60
print(f"{seconds} секунд = {hours}:{minutes}:{secs}")