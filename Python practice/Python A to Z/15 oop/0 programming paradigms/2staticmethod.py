# What is a static method?
# A static method is a method that is bound to the class, not the instance of the class.
# A static method does not take 'self' or 'cls' as the first parameter.
# A static method cannot access or modify instance variables or instance methods.
# A static method cannot access or modify class variables or class methods using 'cls'.
# However, it can access class variables using the class name directly.
# Static methods are used to perform utility tasks that are independent of class or instance state.

class BankAccount:
    bank_name = "Bank of America"
    rate_of_interest = 12.25

    @staticmethod
    def get_bank_name():
        # This is a static method because it doesn't use self or cls
        # It accesses a class variable using the class name
        return BankAccount.bank_name

    @staticmethod
    def get_rate_of_interest(principal, time):
        # This is a static method because it doesn't use self or cls
        # It performs a calculation using parameters and a class variable accessed via the class name
        return (principal * time * BankAccount.rate_of_interest) / 100

# Static methods can be called using the class name directly, without creating an object
print(BankAccount.get_bank_name())               # Output: Bank of America
print(BankAccount.get_rate_of_interest(1000, 1)) # Output: 122.5
