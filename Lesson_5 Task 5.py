# Не сумел решить - нашел похожее решение в интернете. На вебинаре проработаю. Не особо понял зачем здесь Try&Expect
def summary():
    try:
        with open('Number_for_5_task.txt.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()