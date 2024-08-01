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