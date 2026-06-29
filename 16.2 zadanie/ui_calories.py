# ui_calories.py - Интерфейс калькулятора калорий
import tkinter as tk
from tkinter import ttk


def setup_ui(root):
    root.title("Калькулятор калорий")
    root.geometry("450x500")
    root.config(bg="#F0F8FF")

    # Заголовок
    label_title = tk.Label(root, text="Калькулятор калорий",
                           font=("Arial", 20, "bold"),
                           bg="#F0F8FF", fg="#4682B4")
    label_title.pack(pady=20)

    # Возраст
    label_age = tk.Label(root, text="Возраст (лет):", font=("Arial", 12), bg="#F0F8FF")
    label_age.pack()

    entry_age = tk.Entry(root, font=("Arial", 14), width=20, justify="center")
    entry_age.pack(pady=5)

    # Вес
    label_weight = tk.Label(root, text="Вес (кг):", font=("Arial", 12), bg="#F0F8FF")
    label_weight.pack()

    entry_weight = tk.Entry(root, font=("Arial", 14), width=20, justify="center")
    entry_weight.pack(pady=5)

    # Рост
    label_height = tk.Label(root, text="Рост (см):", font=("Arial", 12), bg="#F0F8FF")
    label_height.pack()

    entry_height = tk.Entry(root, font=("Arial", 14), width=20, justify="center")
    entry_height.pack(pady=5)

    # Пол
    label_gender = tk.Label(root, text="Пол:", font=("Arial", 12), bg="#F0F8FF")
    label_gender.pack()

    combo_gender = ttk.Combobox(root, values=["Мужской", "Женский"],
                                font=("Arial", 12), width=18)
    combo_gender.set("Мужской")
    combo_gender.pack(pady=5)

    # Активность
    label_activity = tk.Label(root, text="Уровень активности:", font=("Arial", 12), bg="#F0F8FF")
    label_activity.pack()

    combo_activity = ttk.Combobox(root, values=[
        "Минимальная (сидячий образ жизни)",
        "Низкая (1-2 раза в неделю)",
        "Средняя (3-4 раза в неделю)",
        "Высокая (ежедневно)"
    ], font=("Arial", 10), width=30)
    combo_activity.current(0)
    combo_activity.pack(pady=5)

    # Кнопка
    btn_calc = tk.Button(root, text="Рассчитать", font=("Arial", 16, "bold"),
                         bg="#4682B4", fg="white", width=20, height=1)
    btn_calc.pack(pady=20)

    # Результат
    label_result = tk.Label(root, text="Введите данные и нажмите 'Рассчитать'",
                            font=("Arial", 13, "bold"), bg="#E8F4FD",
                            fg="#2C3E50", wraplength=400, justify="center")
    label_result.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Возвращаем все виджеты для использования в main
    return {
        'entry_age': entry_age,
        'entry_weight': entry_weight,
        'entry_height': entry_height,
        'combo_gender': combo_gender,
        'combo_activity': combo_activity,
        'btn_calc': btn_calc,
        'label_result': label_result
    }