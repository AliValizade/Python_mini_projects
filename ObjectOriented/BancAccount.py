import os
os.system('cls')

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"The balance of {self.name}'s bank account is: {self.balance} "
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, balance={self.balance})'
    
    def __add__(self, other):
        balances = self.balance + other.balance
        names = self.name + '/' + other.name
        return BankAccount(names, balances)
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __iadd__(self, other):
        self.balance += other.balance
        other.balance = 0
        print(f'All balance of {other.name} transferd to {self.name}.✅')
        return self
    
    def transfer(self, other, amount):
        if self.balance < amount:
            print('The account balance is insufficient!❌')
            return
        self.balance -= amount
        other.balance += amount
        print(f'{amount}$ transferd from {self.name} to {other.name}.✅')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'The account balance is insufficient!❌ Withdrawable balance: {self.balance}')
            return
        self.balance -= amount
        print(f"The {amount}$ withdraw from {self.name}'s account.✅")

    def deposit(self, amount):
        if amount < 0:
            print('Amount should be positive!❌')
            return
        self.balance += amount
        print(f"The {amount}$ deposit to {self.name}'s account.✅")
    
    
a = BankAccount('ali', 5000)
b = BankAccount('sara', 1000)
c = BankAccount('kia')

print(a)
print(b)
print(repr(c))
print('='*10)
print(repr(a + b))
print(a == b)
print('='*10)
a += b
print(a)
print(b)
print('='*10)

a.transfer(b, 600)
print(a)
print(b)
print('='*10)
a.withdraw(4000)
print(a)
print('='*10)
b.deposit(1200)
print(b)