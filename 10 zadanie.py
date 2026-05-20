#Задание 10.1)
from PIL import Image

def crop_birthday_card(image_path, output_path="cardd.jpg"):
    try:
        img = Image.open(image_path)
        print(f"Оригинальный размер: {img.size}")

        width, height = img.size

        top = int(height * 0.30)
        bottom = int(height * 0.85)
        left = int(width * 0.05)
        right = int(width * 0.95)

        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)
        print(f"Обрезанный размер: {cropped_img.size}")
        print(f"Сохранено как: {output_path}")
        cropped_img.show()

    except FileNotFoundError:
        print(f"Ошибка: Файл {image_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

crop_birthday_card("birthday.jpg", "cardd.jpg")

#Задание 10.2)
from PIL import Image
import os

#словарь праздников и файлов
greeting_cards = {
    "день рождения": "birthday.jpg",
    "новый год": "new_year.jpg",
    "8 марта": "8 march.jpg",
    "1 мая": "1 may.jpg",
    "9 мая":"9 may.jpg",
    "свадьба": "wedding.jpg"
}

print("Доступные праздники:")
for holiday in greeting_cards:
    print(f"{holiday}")

user_choice = input("К какому празднику нужна открытка:").lower().strip()

if user_choice in greeting_cards:
    filename = greeting_cards[user_choice]

    if os.path.exists(filename):
        img = Image.open(filename)
        print(f"Открытка к празднику '{user_choice}':")
        img.show()
    else:
        print(f"Файл '{filename}' не найден в папке с программой")
else:
    print(f"Праздника '{user_choice}' нет в списке")

#Задание 10.3)
from PIL import Image, ImageDraw, ImageFont
import os

#словарь праздников и файлов
greeting_cards = {
    "день рождения": "birthday.jpg",
    "новый год": "new_year.jpg",
    "8 марта": "8 march.jpg",
    "1 мая": "1 may.jpg",
    "9 мая": "9 may.jpg",
    "свадьба": "wedding.jpg"
}

print("Доступные праздники:")
for holiday in greeting_cards:
    print(f"{holiday}")

user_choice = input("К какому празднику нужна открытка:").lower().strip()

if user_choice in greeting_cards:
    filename = greeting_cards[user_choice]

    if os.path.exists(filename):
        original_img = Image.open(filename)
        print(f"Открытка к празднику '{user_choice}':")
        original_img.show()

        name = input("Введите имя того, кого хотите поздравить: ").strip()

        if name:
            img_copy = original_img.copy()
            draw = ImageDraw.Draw(img_copy)

            text = f"{name}, поздравляю!"

            #Поиск жирного шрифта
            font = None
            font_size = 50

            font_paths = [
                "C:/Windows/Fonts/arialbd.ttf",
                "C:/Windows/Fonts/timesbd.ttf",
                "C:/Windows/Fonts/verdanab.ttf",
            ]

            for path in font_paths:
                try:
                    font = ImageFont.truetype(path, font_size)
                    break
                except:
                    continue

            if font is None:
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()

            #Позиция: по центру вверху
            width, height = img_copy.size

            try:
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
            except:
                text_width, text_height = draw.textsize(text, font=font)

            x = (width - text_width) // 2
            y = 30

            #цвет текста (золотой)
            text_color = (255, 215, 0)

            #Тень
            draw.text((x + 2, y + 2), text, font=font, fill=(0, 0, 0))
            draw.text((x, y), text, font=font, fill=text_color)

            #сохранение
            output_filename = f"greeting_{user_choice.replace(' ', '_')}.png"
            img_copy.save(output_filename, "PNG")
            print(f"\nСохранено как: {output_filename}")
            img_copy.show()
        else:
            print("Имя не введено!")
    else:
        print(f"Файл '{filename}' не найден")
else:
    print(f"Праздника '{user_choice}' нет в списке")