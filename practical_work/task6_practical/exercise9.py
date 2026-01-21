import random
import string
length = int(input("Введіть довжину пароля: "))
password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
print(f"Згенерований пароль: {password}")