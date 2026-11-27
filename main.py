import re

def is_palindrome(text: str) -> bool:
    """Проверяет, является ли строка палиндромом."""
    # Очистка: только буквы и цифры, нижний регистр
    cleaned = re.sub(r'[^\w]', '', text.lower())
    return cleaned == cleaned[::-1]

# Тесты
tests = [
    "А роза упала на лапу Азора",
    "Madam, I'm Adam",
    "Hello, World!",
    "12321",
    "racecar"
]

for text in tests:
    result = "палиндром" if is_palindrome(text) else "не палиндром"
    print(f"'{text}' — {result}")