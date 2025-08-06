class ProcessItems:
    def __init__(self, items:list[str]):
        self.items = items

    def process(self) -> list[str]:
        return [i.upper() for i in self.items]

if __name__ == "__main__":
    process_items = ProcessItems(["apple", "banana", "cherry"])
    print(process_items.process())
# class Adder:
#     def __init__(self, lst:list[int]):
#         self.lst = lst

#     def add(self) -> int:
#         total = 0
#         for i in self.lst:
#             total += i
#         return total
    
#     def add2(self) -> int:
#         return sum(self.lst)

# if __name__ == "__main__":
#     adder = Adder([1, 2, 3, 4, 5])
#     print(adder.add())
#     print(adder.add2())

# class User:
#     def __init__(self):
#         self.name : str = "John"
#         self.age : int = 30
#         self.email : str = "john@example.com"

#     def __str__(self) -> str:
#         return f"User(name={self.name}, age={self.age}, email={self.email})"

# if __name__ == "__main__":
#     user = User()
#     print(user)

# class User:
#     def __init__(self, name: str, age: int, email: str):
#         self.name = name
#         self.age = age
#         self.email = email

#     def __str__(self) -> str:
#         return f"User(name={self.name}, age={self.age}, email={self.email})"

# if __name__ == "__main__":
#     user = User("John", 30, "john@example.com")
#     print(user)

