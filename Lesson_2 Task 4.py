stroka = input('Введите имена победителей в зависимости от занятого ими места')
word = []
number = 1
for i in range(stroka.count(' ') + 1):
    word = stroka.split()
    if len(str(word)) <= 10:
        print(f' {number} {word [i]}')
        number += 1
    else:
        print(f' {number} {word [i] [0:10]}')
        number += 1