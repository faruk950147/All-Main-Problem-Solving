from tkinter import *
from unittest import result


# def buttonClick(number):
#     global operator
#     operator = operator + str(number)
#     input_value.set(operator)


# def buttonClear():
#     global operator
#     operator = ""
#     input_value.set("")


# def buttonEqual():
#     global operator
#     result = str(eval(operator))
#     input_value.set(result)
#     operator = ""


# main = Tk()
# main.title("Calculator")

# operator = ""
# input_value = StringVar()
# display_text = Entry(main, font=("arial", 20, "bold"), textvariable=input_value, bd=30, insertwidth=4,
#                      bg="powder blue", justify=RIGHT)
# display_text.grid(columnspan=4)

# # Row 1 7 8 9 +

# btn_7 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="7", command=lambda: buttonClick(7))
# btn_7.grid(row=1, column=0)

# btn_8 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="8", command=lambda: buttonClick(8))
# btn_8.grid(row=1, column=1)

# btn_9 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="9", command=lambda: buttonClick(9))
# btn_9.grid(row=1, column=2)

# btn_add = Button(main, padx=16, bd=8, fg="black",
#                  font=("arial", 20, "bold"), text="+", command=lambda: buttonClick("+"))
# btn_add.grid(row=1, column=3)

# # Row 2 - 4 5 6 -

# btn_4 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="4", command=lambda: buttonClick(4))
# btn_4.grid(row=2, column=0)

# btn_5 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="5", command=lambda: buttonClick(5))
# btn_5.grid(row=2, column=1)

# btn_6 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="6", command=lambda: buttonClick(6))
# btn_6.grid(row=2, column=2)

# btn_sub = Button(main, padx=16, bd=8, fg="black",
#                  font=("arial", 20, "bold"), text="-", command=lambda: buttonClick("-"))
# btn_sub.grid(row=2, column=3)

# # Row 3 - 1 2 3 *

# btn_1 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="4", command=lambda: buttonClick(1))
# btn_1.grid(row=3, column=0)

# btn_2 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="5", command=lambda: buttonClick(2))
# btn_2.grid(row=3, column=1)

# btn_3 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="6", command=lambda: buttonClick(3))
# btn_3.grid(row=3, column=2)

# btn_mul = Button(main, padx=16, bd=8, fg="black",
#                  font=("arial", 20, "bold"), text="*", command=lambda: buttonClick("*"))
# btn_mul.grid(row=3, column=3)

# # Row 4 - 0 C = /

# btn_0 = Button(main, padx=16, bd=8, fg="black",
#                font=("arial", 20, "bold"), text="0", command=lambda: buttonClick(0))
# btn_0.grid(row=4, column=0)

# btn_clear = Button(main, padx=16, bd=8, fg="black",
#                    font=("arial", 20, "bold"), text="C", command=buttonClear)
# btn_clear.grid(row=4, column=1)

# btn_equal = Button(main, padx=16, bd=8, fg="black",
#                    font=("arial", 20, "bold"), text="=", command=buttonEqual)
# btn_equal.grid(row=4, column=2)

# btn_div = Button(main, padx=16, bd=8, fg="black",
#                  font=("arial", 20, "bold"), text="/", command=lambda: buttonClick("/"))
# btn_div.grid(row=4, column=3)

# # main.mainloop()

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.operator = ""
        self.input_value = StringVar()

        self.display_text = Entry(root, font=("arial", 20, "bold"), textvariable=self.input_value,
                                  bd=30, insertwidth=4, bg="powder blue", justify=RIGHT)
        self.display_text.grid(columnspan=4)

        self.create_buttons()

    def buttonClick(self, number):
        self.operator += str(number)
        self.input_value.set(self.operator)

    def buttonClear(self):
        self.operator = ""
        self.input_value.set("")

    def buttonEqual(self):
        try:
            result = str(eval(self.operator))
            self.input_value.set(result)
            self.operator = ""
        except:
            self.input_value.set("Error")
            self.operator = ""

    def create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3),
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.buttonClick(x) if x not in ["C", "="] else (
                self.buttonClear() if x == "C" else self.buttonEqual()
            )
            Button(self.root, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
                   text=text, command=action).grid(row=row, column=col)

if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    root.mainloop()
