import os
os.system('cls')

class Time:
    def __init__(self, h, m, s):
        if h > 23 or m > 59 or s > 59:
            raise ValueError('Valuse shoud be in range: Hour(0,23), Minute(0,59), Second(0,59)')
        
        self.hour = h
        self.minute = m
        self.second = s

    def __str__(self) -> str:
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'
    

t1 = Time(20, 10, 30)
t2 = Time(20, 10, 30)

print(t1)
print(t2)
print('='*10)
