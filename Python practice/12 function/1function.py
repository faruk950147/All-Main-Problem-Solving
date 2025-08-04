# def display():
#     print("Hello World")
#     def printText():
#         print("Hello World 2")
#     return printText

# display()()

def display():
    print("Hello World")
    def printText():
        print("Hello World 2")
    return printText

alias_display = display()
alias_display()
