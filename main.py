def count_words(text: str) -> int:
    """Подсчитывает количество слов в тексте."""
    return len(text.split())

# Использование
text = input("Введите текст: ")
print(f"Количество слов: {count_words(text)}")

# С учётом пунктуации
import re
def count_words_clean(text: str) -> int:
    """Подсчитывает слова, игнорируя пунктуацию."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)

text = "Привет, мир! Как дела?"
print(f"Слов (с пунктуацией): {count_words(text)}")        # 4
print(f"Слов (без пунктуации): {count_words_clean(text)}") # 4