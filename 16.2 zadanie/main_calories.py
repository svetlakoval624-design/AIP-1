# Калькулятор калорий - с большим выводом результата
import tkinter as tk
from tkinter import ttk


def calculate():
    try:
        age = int(entry_age.get())
        weight = float(entry_weight.get().replace(',', '.'))
        height = float(entry_height.get().replace(',', '.'))
        gender = combo_gender.get()
        activity = combo_activity.current()

        if age <= 0 or weight <= 0 or height <= 0:
            label_result.config(text="Введите числа больше 0!")
            return

        if gender == "Мужской":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        activity_factors = [1.2, 1.375, 1.55, 1.725]
        calories = bmr * activity_factors[activity]

        # Большой и заметный вывод
        label_result.config(
            text=f"{round(calories)} ккал/день\n\nБазовый метаболизм: {round(bmr)} ккал",
            font=("Arial", 18, "bold"),
            fg="#4682B4"
        )

    except ValueError:
        label_result.config(text="Ошибка!\nВведите только цифры!", font=("Arial", 14, "bold"), fg="red")
    except Exception as e:
        label_result.config(text=f"Ошибка: {e}", font=("Arial", 14, "bold"), fg="red")


# Окно
root = tk.Tk()
root.title("Калькулятор калорий")
root.geometry("480x600")
root.config(bg="#F0F8FF")

# Заголовок
tk.Label(root, text="Калькулятор калорий", font=("Arial", 22, "bold"),
         bg="#F0F8FF", fg="#4682B4").pack(pady=15)

# Возраст
tk.Label(root, text="Возраст (лет):", font=("Arial", 12), bg="#F0F8FF").pack()
entry_age = tk.Entry(root, font=("Arial", 14), width=20, justify="center")
entry_age.pack(pady=5)

# Вес
tk.Label(root, text="Вес (кг):", font=("Arial", 12), bg="#F0F8FF").pack()
entry_weight = tk.Entry(root, font=("Arial", 14), width=20, justify="center")
entry_weight.pack(pady=5)

# Рост
tk.Label(root, text="Рост (см):", font=("Arial", 12), bg="#F0F8FF").pack()
entry_height = tk.Entry(root, font=("Arial", 14), width=20, justify="center")
entry_height.pack(pady=5)

# Пол
tk.Label(root, text="Пол:", font=("Arial", 12), bg="#F0F8FF").pack()
combo_gender = ttk.Combobox(root, values=["Мужской", "Женский"], font=("Arial", 12), width=18)
combo_gender.set("Мужской")
combo_gender.pack(pady=5)

# Активность
tk.Label(root, text="Уровень активности:", font=("Arial", 12), bg="#F0F8FF").pack()
combo_activity = ttk.Combobox(root, values=[
    "Минимальная (сидячий образ жизни)",
    "Низкая (1-2 раза в неделю)",
    "Средняя (3-4 раза в неделю)",
    "Высокая (ежедневно)"
], font=("Arial", 10), width=30)
combo_activity.current(0)
combo_activity.pack(pady=5)

# Кнопка
tk.Button(root, text="Рассчитать", font=("Arial", 16, "bold"),
          bg="#4682B4", fg="white", command=calculate,
          width=25, height=1).pack(pady=15)

# Рамка для результата (чтобы было видно)
frame_result = tk.Frame(root, bg="#FFFFFF", relief=tk.RIDGE, bd=3)
frame_result.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

# Результат (БОЛЬШОЙ И ЗАМЕТНЫЙ)
label_result = tk.Label(
    frame_result,
    text="Введите данные\nи нажмите 'Рассчитать'",
    font=("Arial", 16, "bold"),
    bg="#FFFFFF",
    fg="#999999",
    justify="center",
    height=4
)
label_result.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()