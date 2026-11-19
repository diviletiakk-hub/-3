numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]

# Через словарь с подсчётом
from collections import Counter
counts = Counter(numbers)
duplicates = [num for num, count in counts.items() if count > 1]

print(f"Дубликаты: {duplicates}")  # [1, 2, 3]

# Через множества
seen = set()
duplicates2 = set()
for num in numbers:
    if num in seen:
        duplicates2.add(num)
    seen.add(num)

print(f"Дубликаты: {list(duplicates2)}")