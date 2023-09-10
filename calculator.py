import tkinter as tk
from tkinter import ttk
def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = display.get()
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)
root = tk.Tk()
root.title("CALCULATOR")
display = tk.Entry(root, font=("Arial", 24))
display.grid(row=0, column=0, columnspan=4)
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "+",
    "=", "(", ")"
]
row, col = 1, 0
for text in button_texts:
    button = ttk.Button(root, text=text, style="TButton")
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
style = ttk.Style()
style.configure("TButton", font=("Arial", 18))
root.mainloop()
