my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {my_list}')
count = int(input("Введите число: "))
while count != 100: #погуглил... в данном случае 100 - это любое произвольное число.
    for el in range(len(my_list)):
        if my_list[el] == count:
            my_list.insert(el + 1, count)
            break
        elif my_list[0] < count:
            my_list.insert(0, count)
        elif my_list[-1] > count:
            my_list.append(count)
        elif my_list[el] > count and my_list[el + 1] < count:
            my_list.insert(el + 1, count)
    print(f"текущий список - {my_list}")
    count = int(input("Введите число "))
