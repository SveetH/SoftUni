from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("600x250")


# calculates between inches , centimeters and meters.

def calculate():
    try:
        first_value = float(first_entry.get())
        c_1 = click_1.get()
        c_2 = click_2.get()
        try:
            if c_1 == "cm" and c_2 == "inch":
                result = f"{float(first_value) / 2.54:.2f} inches"
                result_label.config(text=result, bg="black", fg="white")
            elif c_1 == "cm" and c_2 == "m":
                result = f"{float(first_value) / 100:.2f} meters"
                result_label.config(text=result, bg="black", fg="white")
            elif c_1 == "inch" and c_2 == "cm":
                result = f"{float(first_value) * 2.54:.2f} centimeters"
                result_label.config(text=result, bg="black", fg="white")
            elif c_1 == "inch" and c_2 == "m":
                result = f"{float(first_value) * 2.54 / 100:.2f} meters"
                result_label.config(text=result, bg="black", fg="white")
            elif c_1 == "m" and c_2 == "inch":
                result = f"{float(first_value) / 2.54 * 100:.2f} inches"
                result_label.config(text=result, bg="black", fg="white")
            elif c_1 == "m" and c_2 == "cm":
                result = f"{float(first_value) * 100:.2f} centimeters"
                result_label.config(text=result, bg="black", fg="white")
        except ValueError:
            result_label.config(text="incorrect type", bg="white", fg="black")
    except ValueError:
        result_label.config(text="Not number/s", bg="white", fg="black")


click_1 = StringVar()
click_1.set("cm")
menu_1 = OptionMenu(root, click_1, "cm", "m", "inch")
menu_1.grid(row=0, column=0, padx=100, pady=20)

click_2 = StringVar()
click_2.set("inch")
menu_2 = tk.OptionMenu(root, click_2, "cm", "m", "inch")
menu_2.grid(row=0, column=1, padx=50, pady=20)

first_entry = Entry(root)
first_entry.grid(row=1, column=0, padx=100, pady=20)

result_label = tk.Label(root, text="Result... ", bg="green", fg="white")
result_label.grid(row=2, column=0, padx=100, pady=20)

calculate_button = tk.Button(root, text="convert", bg="green", fg="white")
calculate_button.grid(row=2, column=1, padx=50, pady=20)
calculate_button.config(command=calculate)

root.mainloop()
