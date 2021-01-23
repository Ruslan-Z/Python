count = int(input('Введите количество элементов списка'))
my_list =[]
i = 0
a = 0
while i < count:
    my_list.append(input('Введите следующее значение списка: '))
    i += 1
for elem in range(int(len(my_list)/2)):
        my_list[a], my_list[a + 1] = my_list [a + 1], my_list[a]
        a += 2
print(my_list)
