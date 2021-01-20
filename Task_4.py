number = int(input('Введите целое положительное число:'))
max_number = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max_number:
        max_number = number % 10
    if number > 9:
        continue
    else:
        print('В Вашем числе максимальной является цифра:', max_number)
        break