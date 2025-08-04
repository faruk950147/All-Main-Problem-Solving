
class Account:
    def __init__(self):
        self.balance = 0
        self.owner = ""
        self.account_number = ""
    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from the balance.")
    def get_balance(self):
        print(f"Current balance: {self.balance}")
    
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from the balance.")
    def get_balance(self):
        print(f"Current balance: {self.balance}")