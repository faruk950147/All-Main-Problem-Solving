class CRUD:
    def __init__(self, lst):
        self.lst = lst

    def create(self, item):
        if item:
            self.lst.append(item)
            print(f"'{item}' added successfully.")
        else:
            print("Item cannot be empty.")

    def read(self):
        if not self.lst:
            print("No items found.")
        else:
            print("Current items:")
            for i, item in enumerate(self.lst):
                print(f"{i}: {item}")

    def update(self, index, new_item):
        if not new_item:
            print("Item cannot be empty.")
            return
        if 0 <= index < len(self.lst): # check index is valid 0 less than index less than length of list
            old_item = self.lst[index]
            self.lst[index] = new_item
            print(f"Item '{old_item}' updated to '{new_item}'.")
        else:
            print("Invalid index!")

    def delete(self, index):
        if not self.lst:
            print("No items to delete.")
            return
        if 0 <= index < len(self.lst): # check index is valid 0 less than index less than length of list
            removed_item = self.lst.pop(index)
            print(f"Item '{removed_item}' deleted successfully.")
        else:
            print("Invalid index!")


class Operation:
    def __init__(self, crud):
        self.crud = crud

    def run(self):
        menu = """
        --- CRUD Menu ---
        1. Create
        2. Read
        3. Update
        4. Delete
        5. Exit
        """
        while True:
            print(menu)
            choice = input("Choose an option (1-5): ").strip()

            if choice in ['1', '2', '3', '4', '5']:
                if choice == '1':
                    item = input("Enter item: ").strip()
                    self.crud.create(item)

                elif choice == '2':
                    self.crud.read()

                elif choice == '3':
                    try:
                        index = int(input("Enter index of item to update: ").strip())
                    except ValueError:
                        print("Invalid input! Please enter a valid integer index.")
                        continue
                    new_item = input("Enter new item: ").strip()
                    self.crud.update(index, new_item)

                elif choice == '4':
                    try:
                        index = int(input("Enter index of item to delete: ").strip())
                    except ValueError:
                        print("Invalid input! Please enter a valid integer index.")
                        continue
                    self.crud.delete(index)

                elif choice == '5':
                    print("Exiting program. Goodbye!")
                    break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    crud = CRUD(["Apple", "Banana", "Cherry"]) #you can add items here or empty list crud = CRUD([])
    operation = Operation(crud)
    operation.run()