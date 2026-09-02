# Task 5: Encapsulation and Abstraction

from abc import ABC, abstractmethod


# Abstract Parent Class
class BankAccount(ABC):

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance       # Private attribute

    # Encapsulation: Method to access private balance
    def get_balance(self):
        return self.__balance

    # Encapsulation: Method to modify private balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount.")

    # Abstract method
    @abstractmethod
    def account_type(self):
        pass


# Child Class
class SavingsAccount(BankAccount):

    # Implementing the abstract method
    def account_type(self):
        print("Account Type: Savings Account")

    # Specific method for savings account
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self._BankAccount__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount.")


# Creating objects
account1 = SavingsAccount("Ayesha", "ACC101", 10000)
account2 = SavingsAccount("Rahul", "ACC102", 15000)


# Displaying account information
print("Account 1")
print("Account Holder:", account1.account_holder)
print("Account Number:", account1.account_number)
account1.account_type()

print("Initial Balance:", account1.get_balance())

# Depositing money
account1.deposit(2000)
print("Balance after deposit:", account1.get_balance())

# Withdrawing money
account1.withdraw(3000)
print("Balance after withdrawal:", account1.get_balance())

print("\nAccount 2")
print("Account Holder:", account2.account_holder)
print("Account Number:", account2.account_number)
account2.account_type()
print("Balance:", account2.get_balance())