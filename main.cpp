#include <iomanip>
#include <iostream>
#include <string>

int main() {
    double a, b;
    std::cout << "Введите длину: ";
    if (!(std::cin >> a)) {
        std::cout << "Ошибка! Нужно ввести число, а не текст!\n";
        return 1;
    }
    std::cout << "Введите ширину: ";
    if (!(std::cin >> b)) {
        std::cout << "Ошибка! Нужно ввести число, а не текст!\n";
        return 1;
    }
    if (a <= 0 || b <= 0) {
        std::cout << "Числа должны быть положительными!\n";
        return 1;
    }
    double S = a * b;
    double P = (a + b) * 2;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Площадь: " << S << "\n";
    std::cout << "Периметр: " << P << "\n";
    return 0;
}