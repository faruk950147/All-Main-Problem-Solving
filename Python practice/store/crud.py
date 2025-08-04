def create(lst):
    item = input("Enter item to add: ")
    if item:
        lst.append(item)
        print(f"'{item}' added successfully.")
    else:
        print("Item cannot be empty.")

def read(items):
    if not items:
        print("No items found.")
    else:
        print("Current items:")
        for i, item in enumerate(items):
            print(f"{i}: {item}")

def update(items):
    read(items)
    if not items:
        return
    index = int(input("Enter index of item to update: "))
    if 0 <= index < len(items):
        new_value = input("Enter new value: ")
        old_value = items[index]
        items[index] = new_value
        print(f"Item '{old_value}' updated to '{new_value}'.")
    else:
        print("Invalid index!")

def delete(items):
    read(items)
    if not items:
        return
    index = int(input("Enter index of item to delete: "))
    if 0 <= index < len(items):
        removed_item = items.pop(index)
        print(f"Item '{removed_item}' deleted.")
    else:
        print("Invalid index!")

def main():
    items = []
    while True:
        print("\n--- CRUD Menu ---")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create(items)
        elif choice == '2':
            read(items)
        elif choice == '3':
            update(items)
        elif choice == '4':
            delete(items)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

