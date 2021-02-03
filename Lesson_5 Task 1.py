
my_f = open('test.txt', 'w')
line = input('Введите текст')
while line:
    my_f.writelines(line)
    line = input('Введите текст')
    # Если не ничего не вводим, то выходим из цикла.
    if not line:
        break
my_f.close()
