def salary():
    a = int(input('Введите выработку работника в часах : '))
    b = int(input('Введите ставку за 1 час: '))
    c = int(input('Введите размер премии: '))
    sal = a * b
    return sal + c
print(f'Размер заработной платы составил: {salary() }')
