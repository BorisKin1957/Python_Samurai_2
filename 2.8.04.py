users = {
    "Николя": ["кружка", "стакан", "рюмка"],
    "Брагин Вовчик": ["лифчик", "косметика", "тостер", "плюшевый мишка"],
    "Хайзенберг": ["мерная колба", "спирт", "огурчик"],
    "Ирина Михайловна": ["тостер", "микроволновка", "несущая стена"],
    "Кратос": ["топор", "доспехи", "умная колонка", "тостер"]
}

itis, names = input(), []
for name, products in users.items():
    if itis in products:
        names.append(name)

print(f'{itis} в корзине у {", ".join(names)}' if names else f'{itis} отсутствует в корзинах пользователей')