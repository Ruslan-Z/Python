def func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'

print(func((int(input('Введите первое число: '))), (int(input('Введите второе число: ')))))