import tkinter as tk
from tkinter.messagebox import showerror

window = tk.Tk()

window.title("My Calculator")
window.geometry("350x500")
window.resizable(False, False)

window.configure(bg="#202124")

display = tk.Entry(
    window,
    font=("Arial", 26),
    justify="right",
    bg="#303134",
    fg="black",
    bd=0,
    state="normal"
)
display.insert(0, "0")
display.pack(
    padx=15,
    pady=25,
    ipady=15,
    fill="x"
)
display.config(state="readonly")

buttons_frame = tk.Frame(
    window,
    bg='#202124'
)
buttons_frame.pack(
    padx=15,
    pady=10,
    fill="both",
    expand=True
)

first_number = ""
second_number = ""
operator = ""
current_number = ""
new_input = False

def button_click(value):
    global current_number
    global first_number
    global second_number
    global operator
    global new_input
    if value == "C":
        first_number = ""
        second_number = ""
        operator = ""
        new_input = False
        current_number = ''
        display.config(state="normal")
        display.delete(0, tk.END)
        display.insert(0, "0")
        display.config(state="readonly")
    elif value == "⌫":
        current_number = current_number[:-1]
        display.config(state="normal")
        display.delete(0, tk.END)
        if len(current_number) == 0:
            display.insert(0, "0")
        else:
            display.insert(0, current_number)
        display.config(state="readonly")
    elif value == '%':
        result = f'{float(current_number) / 100:g}'
        current_number = str(result)
        display.config(state="normal")
        display.delete(0, tk.END)
        display.insert(0, result)
        display.config(state="readonly")
    elif value == '=':
        if first_number == "" or current_number == "":
            tk.messagebox.showwarning(
                title="Внимание",
                message="Введите оба числа!"
            )
            return
        new_input = True
        display.config(state="normal")
        second_number = float(current_number)
        first_number = float(first_number)
        result = 0
        if operator == '+':
            result = first_number + second_number
        elif operator == '/':
            if second_number != 0:
                result = round(first_number / second_number, 2)
            else:
                tk.messagebox.showerror(title="Ошибка", message="На ноль делить нельзя", icon=tk.messagebox.ERROR)
        elif operator == 'x':
            result = first_number * second_number
        else:
            result = first_number - second_number

        current_number = f"{result:g}"
        display.delete(0, tk.END)
        display.insert(0, current_number)
        display.config(state="readonly")
    elif value in ['+', '-', '/', 'x', '%']:
        display.config(state="normal")
        first_number = current_number
        operator = value
        current_number = ''
        new_input = False
        display.config(state="readonly")
    elif value == ".":
        if current_number == "":
            current_number = "0."
        elif "." not in current_number:
            current_number += "."
        display.config(state="normal")
        display.delete(0, tk.END)
        display.insert(0, current_number)
        display.config(state="readonly")
    else:
        if new_input:
            current_number = value
            new_input = False
        else:
            current_number = current_number + value

        display.config(state="normal")
        display.delete(0, tk.END)
        display.insert(0, current_number)
        display.config(state="readonly")


buttons = [
    ['C', '⌫', '%', '/'],
    ['7', '8', '9', 'x'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '']
]
for row_index, row in enumerate(buttons):
    for column_index, text in enumerate(row):
        button = tk.Button(
            buttons_frame,
            text=text,
            font=('Arial', 18),
            bg='#303134',
            fg="white",
            command=lambda value=text: button_click(value)
        )
        button.grid(
            row=row_index,
            column=column_index,
            padx=5,
            pady=5,
            sticky='nsew'
        )

for i in range(5):
    buttons_frame.grid_columnconfigure(i, weight=1)
    buttons_frame.grid_rowconfigure(i, weight=1)

window.mainloop()