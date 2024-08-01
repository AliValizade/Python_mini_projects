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
    
    
    



a = BankAccount('ali', 5000)
b = BankAccount('sara', 1000)
c = BankAccount('kia')

print(a)
print(b)
print(repr(c))