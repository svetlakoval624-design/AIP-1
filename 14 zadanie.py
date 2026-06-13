#Задание 14.1)
print("===Задание 14.1===")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное"]

    def show_flavors(self):
        print("Сорта мороженого:", self.flavors)

ice_cream = IceCreamStand("Мороженое", "Десертная")
ice_cream.show_flavors()


#Задание 14.2)
print("===Задание 14.2===")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Ванильное", "Шоколадное", "Клубничное"]
        self.location = location
        self.working_hours = working_hours
        self.popsicles = []
        self.soft = []

    def show_flavors(self):
        print("Сорта:", self.flavors)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Добавлен сорт: {flavor}")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Удалён сорт: {flavor}")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Да, {flavor} есть в меню")
        else:
            print(f"Нет, {flavor} отсутствует")

    def add_popsicle(self, flavor):
        self.popsicles.append(flavor)
        print(f"Добавлено мороженое на палочке: {flavor}")

    def add_soft(self, flavor):
        self.soft.append(flavor)
        print(f"Добавлено мягкое мороженое: {flavor}")


shop = IceCreamStand("Мороженое", "Десертная", "ул. Центральная, 15", "10:00-22:00")
shop.show_flavors()
shop.add_flavor("Мятное")
shop.remove_flavor("Клубничное")
shop.check_flavor("Шоколадное")
shop.add_popsicle("Эскимо")
shop.add_soft("Ванильное мягкое")

#Задание 14.3
print("===Задание 14.3===")
import tkinter as tk
from tkinter import messagebox

class IceCreamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Кафе-Мороженое")
        self.root.geometry("400x500")

        self.shop = IceCreamStand("Мороженое", "Десертная", "Центральная, 15", "10:00-22:00")

        tk.Label(root, text="КАФЕ-МОРОЖЕНОЕ", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Сорта мороженого:").pack()
        self.listbox = tk.Listbox(root, height=6)
        self.listbox.pack(pady=5, padx=20, fill="both", expand=True)
        self.update_list()

        frame1 = tk.Frame(root)
        frame1.pack(pady=5)

        self.entry = tk.Entry(frame1, width=15)
        self.entry.pack(side="left", padx=5)

        tk.Button(frame1, text="Добавить", command=self.add_flavor, bg="lightgreen").pack(side="left", padx=2)
        tk.Button(frame1, text="Удалить", command=self.remove_flavor, bg="lightcoral").pack(side="left", padx=2)
        tk.Button(frame1, text="Проверить", command=self.check_flavor, bg="lightskyblue").pack(side="left", padx=2)

        tk.Label(root, text="Мороженое на палочке:").pack()
        self.listbox2 = tk.Listbox(root, height=3)
        self.listbox2.pack(pady=5, padx=20, fill="both", expand=True)

        frame2 = tk.Frame(root)
        frame2.pack(pady=5)

        self.entry2 = tk.Entry(frame2, width=15)
        self.entry2.pack(side="left", padx=5)

        tk.Button(frame2, text="Добавить", command=self.add_popsicle, bg="lightgreen").pack(side="left", padx=2)
        tk.Button(frame2, text="Удалить", command=self.remove_popsicle, bg="lightcoral").pack(side="left", padx=2)

        self.update_popsicle_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for flavor in self.shop.flavors:
            self.listbox.insert(tk.END, flavor)

    def update_popsicle_list(self):
        self.listbox2.delete(0, tk.END)
        for item in self.shop.popsicles:
            self.listbox2.insert(tk.END, item)

    def add_flavor(self):
        flavor = self.entry.get()
        if flavor:
            self.shop.add_flavor(flavor)
            self.update_list()
            self.entry.delete(0, tk.END)

    def remove_flavor(self):
        selection = self.listbox.curselection()
        if selection:
            flavor = self.shop.flavors[selection[0]]
            self.shop.remove_flavor(flavor)
            self.update_list()

    def check_flavor(self):
        flavor = self.entry.get()
        if flavor:
            if flavor in self.shop.flavors:
                messagebox.showinfo("Результат", f"{flavor} есть в меню")
            else:
                messagebox.showinfo("Результат", f"{flavor} отсутствует")

    def add_popsicle(self):
        flavor = self.entry2.get()
        if flavor:
            self.shop.add_popsicle(flavor)
            self.update_popsicle_list()
            self.entry2.delete(0, tk.END)

    def remove_popsicle(self):
        selection = self.listbox2.curselection()
        if selection:
            item = self.shop.popsicles[selection[0]]
            self.shop.popsicles.remove(item)
            self.update_popsicle_list()


root = tk.Tk()
app = IceCreamApp(root)
root.mainloop()