import customtkinter as ctk
from tkinter import messagebox


app = ctk.CTk()
app.title("Advanced Unit Converter")
app.geometry("400x400")


def length_conversion():
    try:
        meters = float(entry_value.get())
        if unit_choice.get() == "Length (m to km)":
            result_value = meters / 1000
            result.set(f"{meters} meters = {result_value} kilometers")
        elif unit_choice.get() == "Length (m to cm)":
            result_value = meters * 100
            result.set(f"{meters} meters = {result_value} centimeters")
        elif unit_choice.get() == "Length (m to inches)":
            result_value = meters * 39.3701
            result.set(f"{meters} meters = {result_value:.2f} inches")
        elif unit_choice.get() == "Length (m to feet)":
            result_value = meters * 3.28084
            result.set(f"{meters} meters = {result_value:.2f} feet")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def weight_conversion():
    try:
        kilograms = float(entry_value.get())
        if unit_choice.get() == "Weight (kg to g)":
            result_value = kilograms * 1000
            result.set(f"{kilograms} kilograms = {result_value} grams")
        elif unit_choice.get() == "Weight (kg to lbs)":
            result_value = kilograms * 2.20462
            result.set(f"{kilograms} kilograms = {result_value:.2f} pounds")
        elif unit_choice.get() == "Weight (kg to oz)":
            result_value = kilograms * 35.274
            result.set(f"{kilograms} kilograms = {result_value:.2f} ounces")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def temperature_conversion():
    try:
        celsius = float(entry_value.get())
        if unit_choice.get() == "Temperature (C to F)":
            result_value = (celsius * 9/5) + 32
            result.set(f"{celsius}°C = {result_value:.2f}°F")
        elif unit_choice.get() == "Temperature (C to K)":
            result_value = celsius + 273.15
            result.set(f"{celsius}°C = {result_value:.2f}K")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def convert():
    conversion_type = unit_choice.get()
    if "Length" in conversion_type:
        length_conversion()
    elif "Weight" in conversion_type:
        weight_conversion()
    elif "Temperature" in conversion_type:
        temperature_conversion()




label_value = ctk.CTkLabel(app, text="Enter Value:")
label_value.pack(pady=10)

entry_value = ctk.CTkEntry(app, placeholder_text="Enter a number")
entry_value.pack(pady=10)


unit_choice = ctk.CTkOptionMenu(app, values=[
    "Length (m to km)", "Length (m to cm)", "Length (m to inches)", "Length (m to feet)",
    "Weight (kg to g)", "Weight (kg to lbs)", "Weight (kg to oz)",
    "Temperature (C to F)", "Temperature (C to K)"
])
unit_choice.pack(pady=10)
unit_choice.set("Length (m to km)")  


convert_button = ctk.CTkButton(app, text="Convert", command=convert)
convert_button.pack(pady=10)


result = ctk.StringVar()
label_result = ctk.CTkLabel(app, textvariable=result)
label_result.pack(pady=10)


app.mainloop()
