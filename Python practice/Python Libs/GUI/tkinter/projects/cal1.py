import tkinter as tk

# def click(event):
#     text = event.widget.cget("text")
#     if text == "=":
#         try:
#             result = eval(str(screen.get()))
#             screen_var.set(result)
#         except Exception as e:
#             screen_var.set("Error")
#     elif text == "C":
#         screen_var.set("")
#     else:
#         screen_var.set(screen.get() + text)

# root = tk.Tk()
# root.title("Tkinter Calculator")
# root.geometry("300x400")

# # Display Screen
# screen_var = tk.StringVar()
# screen = tk.Entry(root, textvar=screen_var, font="Arial 20 bold", justify="right")
# screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# # Buttons Frame
# button_frame = tk.Frame(root)
# button_frame.pack()

# buttons = [
#     ["7", "8", "9", "/"],
#     ["4", "5", "6", "*"],
#     ["1", "2", "3", "-"],
#     ["0", "C", "=", "+"]
# ]

# for row in buttons:
#     row_frame = tk.Frame(button_frame)
#     row_frame.pack(expand=True, fill="both")
#     for btn_text in row:
#         btn = tk.Button(row_frame, text=btn_text, font="Arial 18", relief="ridge", border=2)
#         btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
#         btn.bind("<Button-1>", click)

# root.mainloop()
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Class Calculator")
        self.root.geometry("300x400")

        self.screen_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display Screen
        self.screen = tk.Entry(self.root, textvar=self.screen_var, font="Arial 20 bold", justify="right")
        self.screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"]
        ]

        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(expand=True, fill="both")
            for btn_text in row:
                btn = tk.Button(row_frame, text=btn_text, font="Arial 18", relief="ridge", border=2)
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
                btn.bind("<Button-1>", self.click)

    def click(self, event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = eval(str(self.screen_var.get()))
                self.screen_var.set(result)
            except Exception as e:
                self.screen_var.set("Error")
        elif text == "C":
            self.screen_var.set("")
        else:
            self.screen_var.set(self.screen_var.get() + text)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
