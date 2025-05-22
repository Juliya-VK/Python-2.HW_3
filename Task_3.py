"""Задание 2. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант. Верните все возможные варианты комплектации рюкзака."""

# Словарь с вещами и их массой
items = {
    "палатка": 3.5,
    "спальник": 1.5,
    "котелок": 0.7,
    "еда": 2.0,
    "вода": 1.5,
    "фонарик": 0.3,
    "аптечка": 0.5,
    "карта": 0.1,
}

# Максимальная грузоподъёмность рюкзака
max_weight = 5.0

# Преобразуем словарь в список кортежей для удобства
items_list = list(items.items())

# Список для хранения всех возможных вариантов
valid_combinations = []

# Перебираем все возможные комбинации вещей
from itertools import combinations

for r in range(1, len(items_list) + 1):
    for combo in combinations(items_list, r):
        total_weight = sum(item[1] for item in combo)
        if total_weight <= max_weight:
            valid_combinations.append(combo)

# Выводим все возможные варианты
print("Все возможные варианты комплектации рюкзака:")
for i, combo in enumerate(valid_combinations, 1):
    items_names = [item[0] for item in combo]
    total_weight = sum(item[1] for item in combo)
    print(f"{i}. Вещи: {items_names}, Общий вес: {total_weight} кг")

# Если нужно просто один допустимый вариант, можно взять первый из списка
if valid_combinations:
    first_combo = valid_combinations[0]
    print("\nОдин допустимый вариант:")
    print("Вещи:", [item[0] for item in first_combo])
    print("Общий вес:", sum(item[1] for item in first_combo), "кг")
else:
    print("Невозможно уложиться в максимальный вес!")
    