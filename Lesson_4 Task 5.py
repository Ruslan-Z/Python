from functools import reduce
def func(a, b):
    return a * b
print(f'Список четных значений {[b for b in range(99, 1001) if b % 2 == 0]}')
print(f'Получившееся произведение:  {reduce(func, [b for b in range(99, 1001) if b % 2 == 0])}')
