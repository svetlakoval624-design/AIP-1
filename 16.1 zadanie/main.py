#main.py
import tkinter as tk
from tkinter import messagebox
from currency_converter import CurrencyConverter


def converter():
    try:
        c = CurrencyConverter()

        in_cur = entry_in_cur.get().upper().strip()
        out_cur = entry_out_cur.get().upper().strip()
        in_sum = float(entry_sum.get())

        result = c.convert(in_sum, in_cur, out_cur)
        label_result.config(text=f"Результат: {round(result, 2)} {out_cur}")

    except ValueError:
        label_result.config(text="Ошибка: введите число!")
    except Exception as e:
        label_result.config(text="Ошибка: проверьте валюту")


root = tk.Tk()
root.title("Конвертер валют")
root.geometry("400x350")
root.config(bg="#22222e")

#Заголовок
tk.Label(root, text="Конвертер валют", font=("Arial", 20, "bold"),
         fg="#fb5b5d", bg="#22222e").pack(pady=20)

#Поля
tk.Label(root, text="Из валюты (USD, EUR, RUB)", fg="white", bg="#22222e").pack()
entry_in_cur = tk.Entry(root, font=("Arial", 14))
entry_in_cur.pack(pady=5)

tk.Label(root, text="Сумма", fg="white", bg="#22222e").pack()
entry_sum = tk.Entry(root, font=("Arial", 14))
entry_sum.pack(pady=5)

tk.Label(root, text="В валюту (USD, EUR, RUB)", fg="white", bg="#22222e").pack()
entry_out_cur = tk.Entry(root, font=("Arial", 14))
entry_out_cur.pack(pady=5)

#Кнопка
tk.Button(root, text="Конвертировать", font=("Arial", 14),
          bg="#fb5b5d", fg="white", command=converter).pack(pady=15)

#Результат
label_result = tk.Label(root, text="", font=("Arial", 14, "bold"),
                        fg="white", bg="#22222e")
label_result.pack(pady=10)

root.mainloop()