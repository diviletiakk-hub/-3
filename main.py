try:
    a = float(input("Ширина: "))
    b = float(input("Длина: "))
    if a <= 0 or b <= 0:
        print("Числа должны быть положительными!")
    else:
        S = a * b
        P = (a + b) * 2
        print(f"Площадь: {S:.2f}")
        print(f"Периметр: {P:.2f}")
except ValueError:
    print("Ошибка! Нужно ввести число, а не текст!")
