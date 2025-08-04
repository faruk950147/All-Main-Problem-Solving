import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# main window
root = tk.Tk()
root.title("Calculator")

# input field
entry = tk.Entry(root, width=20, font=('Arial', 18), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# button creation
for (text, row, col) in buttons:
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
              command=lambda text=text: button_click(text)).grid(row=row, column=col) # command=lambda automatically function calling so we don't need to call it manually  

root.mainloop()
