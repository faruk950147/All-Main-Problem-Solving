class Account:
    def __init__(self, owner, pin, balance=0):
        self.owner = owner
        self.pin = pin
        self.balance = balance

    def verify_pin(self, pin):
        return pin == self.pin

    def check_balance(self, pin):
        if self.verify_pin(pin):
            print(f"Balance for {self.owner}: {self.balance}")
        else:
            print("Invalid PIN")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Total balance: {self.balance}")

    def withdraw(self, amount, pin):
        if self.verify_pin(pin):
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print(f"Withdrawn {amount}. Total balance: {self.balance}")
        else:
            print("Invalid PIN")

    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.pin = new_pin
            print("PIN changed successfully")
        else:
            print("Invalid old PIN")


class ATM:
    def __init__(self, account):
        self.account = account

    def run(self):
        while True:
            print("\n\t*** How Can I Help You ***")
            print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Change PIN\n5. Exit")
            choice = input("Choose option: ")

            if choice == '1':
                pin = input("Enter your PIN: ")
                self.account.check_balance(pin)

            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                self.account.deposit(amount)

            elif choice == '3':
                pin = input("Enter your PIN: ")
                amount = float(input("Enter withdraw amount: "))
                self.account.withdraw(amount, pin)

            elif choice == '4':
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                self.account.change_pin(old_pin, new_pin)

            elif choice == '5':
                print("Thank you for using ATM!")
                break

            else:
                print("Invalid option.")


account = Account("Raid", '1234', 1000)
atm = ATM(account)
atm.run()
