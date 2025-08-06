# def add(a: int, b: int) -> int:
#     return a + b

# if __name__ == "__main__":
#     print(add(1, 2))


def process_items(items: list[str]) -> None:
    for item in items:
        print(item)

if __name__ == "__main__":
    process_items(["apple", "banana", "cherry"])