word = input("Введіть слово: ").lower()
if word == word[::-1]:
    print(f"'{word}' - паліндром")
else:
    print(f"'{word}' - не паліндром")