# def greet(lang):
#     def eng():
#         return "Hello " + lang

#     def ban():
#         return "Hello " + lang

#     if lang == "en":
#         return eng()
#     else:
#         return ban()


# s = greet("en")
# print(s)


def something(greeting, name):
    def getFirstName():
        if name:
            return name.split(" ")[0]
        return ""
    return greeting + " " + getFirstName()

print(something("Hello", "John Doe"))