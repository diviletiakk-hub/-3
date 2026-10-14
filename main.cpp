#include <iostream>

int main() {
    int number;
    std::cout << "Введите число: ";
    std::cin >> number;

    if (number > 0) {
        // проверка чётности
        if (number % 2 == 0) {
            std::cout << "Число " << number << " — чётное\n";
        } else {
            std::cout << "Число " << number << " — нечётное\n";
        }

        // проверка делимости на 3
        if (number % 3 == 0) {
            std::cout << "Число " << number << " — делится на 3\n";
        } else {
            std::cout << "Число " << number << " — не делится на 3\n";
        }

        // знак
        std::cout << "Число " << number << " — положительное\n";
    }
    else if (number < 0) {
        if (number % 2 == 0) {
            std::cout << "Число " << number << " — чётное\n";
        } else {
            std::cout << "Число " << number << " — нечётное\n";
        }

        if (number % 3 == 0) {
            std::cout << "Число " << number << " — делится на 3\n";
        } else {
            std::cout << "Число " << number << " — не делится на 3\n";
        }

        std::cout << "Число " << number << " — отрицательное\n";
    }
    else {
        std::cout << "Число " << number << " — равно 0\n";
    }

    return 0;
}