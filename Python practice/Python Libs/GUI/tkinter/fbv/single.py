import tkinter as tk

def button_click(value):
    print(f"You clicked: {value}")

root = tk.Tk()
root.title("Single Button")

# main window
btn = tk.Button(root, text="7", font=('Arial', 20), width=5, command=lambda: button_click("7")) # command=lambda: button_click("7") what i do work and command=lambda automatically function calling so we don't need to call it manually  
btn.pack(padx=20, pady=20)

root.mainloop()
