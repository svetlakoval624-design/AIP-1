# #Задание 15.1)
# print("===Задание 15.1===")
#
# import tkinter as tk
# import requests
#
# API_KEY = "2d22a2d9ba43bec304baa1a56e186243"
#
# def get_weather():
#     city = city_entry.get().strip()
#     if not city:
#         result_label.config(text="Введите название города!")
#         return
#
#     url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric",
#         "lang": "ru"
#     }
#
#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#
#         if data.get("cod") != 200:
#             result_label.config(text=f"Ошибка: {data.get('message', 'Неизвестная ошибка')}")
#             return
#
#         temp = data["main"]["temp"]
#         feels_like = data["main"]["feels_like"]
#         description = data["weather"][0]["description"]
#         humidity = data["main"]["humidity"]
#         wind_speed = data["wind"]["speed"]
#
#         text = f"Температура: {temp}°C\n"
#         text += f"Ощущается как: {feels_like}°C\n"
#         text += f"Влажность: {humidity}%\n"
#         text += f"Ветер: {wind_speed} м/с\n"
#         text += f"{description.capitalize()}"
#
#         result_label.config(text=text)
#
#     except Exception as e:
#         result_label.config(text=f"Не удалось получить данные.\nОшибка: {e}")
#
#
# #Создание графического интерфейса
# root = tk.Tk()
# root.title("Погода")
# root.geometry("400x350")
#
# #Виджеты
# label = tk.Label(root, text="Введите город:", font=("Arial", 14))
# label.pack(pady=5)
#
# city_entry = tk.Entry(root, width=30, font=("Arial", 12))
# city_entry.pack(pady=5)
#
# button = tk.Button(root, text="Узнать погоду", font=("Arial", 12), command=get_weather)
# button.pack(pady=10)
#
# result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
# result_label.pack(pady=10)
#
# root.mainloop()
#

#Задание 15.2)
print("===Задание 15.2===")

import tkinter as tk
from tkinter import messagebox
import requests
import random


def get_random_fact():

    url = "https://api.api-ninjas.com/v1/facts?limit=1"

    headers = {'X-Api-Key': 'ваш_ключ_здесь'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0:
                fact = data[0].get('fact', 'Факт не найден')
                result_label.config(text=f"Исторический факт:\n\n{fact}")
            else:
                result_label.config(text="Факт не найден")
        else:
            #Запасной вариант без API ключа
            facts = [
                "Первая в мире фотография была сделана в 1826 году.",
                "Великая Китайская стена видна из космоса.",
                "Пирамиды Египта были построены около 4500 лет назад.",
                "Первая книга была напечатана в 1455 году.",
                "Рим был основан в 753 году до н.э.",
                "Первая война была записана в 2700 году до н.э.",
                "Шоколад появился более 3000 лет назад.",
                "Первая железная дорога была построена в 1825 году."
            ]
            result_label.config(text=f"Исторический факт:\n\n{random.choice(facts)}")

    except Exception as e:
        #Запасной вариант при ошибке
        facts = [
            "Первая в мире фотография была сделана в 1826 году.",
            "Великая Китайская стена видна из космоса.",
            "Пирамиды Египта были построены около 4500 лет назад.",
            "Первая книга была напечатана в 1455 году.",
            "Рим был основан в 753 году до н.э."
        ]
        result_label.config(text=f"Исторический факт:\n\n{random.choice(facts)}")


def get_city_landmarks():
    city = entry_city.get().strip()
    if not city:
        messagebox.showwarning("Ошибка", "Введите название города!")
        return

    landmarks = {
        "москва": "Красная площадь, Кремль, Собор Василия Блаженного, Третьяковская галерея",
        "санкт-петербург": "Эрмитаж, Петергоф, Дворцовая площадь, Исаакиевский собор",
        "лондон": "Биг-Бен, Тауэрский мост, Букингемский дворец, Лондонский глаз",
        "париж": "Эйфелева башня, Лувр, Нотр-Дам, Елисейские поля",
        "рим": "Колизей, Пантеон, Собор Святого Петра, Фонтан Треви",
        "нью-йорк": "Статуя Свободы, Эмпайр-стейт-билдинг, Центральный парк, Таймс-сквер",
        "токио": "Гора Фудзи, Императорский дворец, Храм Сэнсо-дзи, Башня Токио",
    }

    city_lower = city.lower()
    if city_lower in landmarks:
        text = f"Достопримечательности города {city.title()}:\n\n{landmarks[city_lower]}"
        result_label.config(text=text)
    else:
        result_label.config(
            text=f"Извините, данные о достопримечательностях\nгорода '{city}' временно отсутствуют.\n"
                 f"Попробуйте: Москва, Санкт-Петербург, Лондон,\nПариж, Рим, Нью-Йорк, Токио"
        )


#Создаем интерфейс
root = tk.Tk()
root.title("Исторические факты и достопримечательности")
root.geometry("500x450")
root.config(padx=20, pady=20)

tk.Label(root, text="Введите название города:", font=("Arial", 12)).pack(pady=5)

entry_city = tk.Entry(root, font=("Arial", 12), width=30)
entry_city.pack(pady=5)
entry_city.focus()

btn_landmarks = tk.Button(root, text="Узнать достопримечательности",
                          font=("Arial", 12), bg="#2196F3", fg="white",
                          command=get_city_landmarks)
btn_landmarks.pack(pady=5)

btn_fact = tk.Button(root, text="Случайный исторический факт",
                     font=("Arial", 12), bg="#FF9800", fg="white",
                     command=get_random_fact)
btn_fact.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left",
                        wraplength=450)
result_label.pack(pady=10)

root.mainloop()