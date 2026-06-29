# #Задание 12.1)
# print("===Задание 12.1===")
# import json
#
# def task_12_1():
#     with open('products.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#
#     for product in data['products']:
#         print(f"Название: {product['name']}")
#         print(f"Цена: {product['price']}")
#         print(f"Вес: {product['weight']}")
#
#         if product['available']:
#             print("В наличии")
#         else:
#             print("Нет в наличии!")
#
#         print()
#
#
# task_12_1()

# #Задание 12.2)
# print("===Задание 12.2===")
# import json
# import os
#
#
# def task_12_2():
#     filename = 'products.json'
#
#     if not os.path.exists(filename) or os.path.getsize(filename) == 0:
#         initial_data = {
#             "products": [
#                 {"name": "Шоколад", "price": 50, "available": True, "weight": 100},
#                 {"name": "Кофе", "price": 100, "available": False, "weight": 250},
#                 {"name": "Чай", "price": 70, "available": True, "weight": 50}
#             ]
#         }
#         with open(filename, 'w', encoding='utf-8') as file:
#             json.dump(initial_data, file, ensure_ascii=False, indent=2)
#
# #Запрашиваем у пользователя данные
#     print("Добавление нового продукта:")
#     name = input("Введите название продукта: ")
#     price = int(input("Введите цену: "))
#     weight = int(input("Введите вес: "))
#     available_input = input("В наличии (да/нет): ").lower()
#     available = True if available_input == 'да' else False
#
#
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#
# #Добавляем новый продукт
#     new_product = {
#         "name": name,
#         "price": price,
#         "available": available,
#         "weight": weight
#     }
#     data['products'].append(new_product)
#
# #Сохраняем обратно в файл
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=2)
#
#     print("\nПродукт добавлен!\n")
#
# #Выводим все продукты
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#
#     for product in data['products']:
#         print(f"Название: {product['name']}")
#         print(f"Цена: {product['price']}")
#         print(f"Вес: {product['weight']}")
#
#         if product['available']:
#             print("В наличии")
#         else:
#             print("Нет в наличии!")
#
#         print()
#
#
# task_12_2()

#Задание 12.3)
print("===Задание 12.3===")

import os

def task_12_3():
#Проверяем наличие входного файла
    if not os.path.exists('en-ru.txt'):
        print("Файл en-ru.txt не найден!")
        return

    ru_en_dict = {}

    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            #Разделяем английский и русский варианты
            parts = line.split(' - ')
            if len(parts) != 2:
                continue

            english_words = parts[0].strip()
            russian_words = parts[1].strip()

            #Разбиваем русские слова по запятой
            russian_list = [word.strip() for word in russian_words.split(',')]

            #Добавляем в словарь
            for russian in russian_list:
                if russian in ru_en_dict:
                    ru_en_dict[russian].append(english_words)
                else:
                    ru_en_dict[russian] = [english_words]

    #Сортируем по алфавиту
    sorted_keys = sorted(ru_en_dict.keys())

    #Записываем в файл ru-en.txt
    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for key in sorted_keys:
            # Сортируем английские варианты
            english_list = sorted(ru_en_dict[key])
            # Объединяем через запятую с пробелом
            english_str = ', '.join(english_list)
            file.write(f"{key} – {english_str}\n")

    print("Файл ru-en.txt создан успешно!")


task_12_3()
