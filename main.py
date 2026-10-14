number = int(input("Введите число: "))

if number % 2 == 0:
    print(f"Число {number} — четное")
    print(f'Число {number} - не делится на 3')
elif number % 3 == 0:
    print(f'Число {number} - делится на 3')
    print(f"Число {number} — нечетное")
else:
    print(f"Число {number} — нечетное")
    print(f'Число {number} - не делится на 3')
