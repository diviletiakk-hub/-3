number = int(input("Введите число: "))

if number > 0:
    if number % 2 == 0:
        print(f"Число {number} — четное")
    else:
        print(f"Число {number} — нечетное")
    if number % 3 == 0:
        print(f"Число {number} — делится на 3")
    else:
        print(f"Число {number} — не делится на 3")
elif number < 0:
    if number % 2 == 0:
        print(f"Число {number} — четное")
    else:
        print(f"Число {number} — нечетное")

    if number % 3 == 0:
        print(f"Число {number} — делится на 3")
    else:
        print(f"Число {number} — не делится на 3")
    print(f"Число {number} — отрицательное")
else:
    print(f"Число {number} — равно 0")
