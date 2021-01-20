user_choice = int(input('Введите любое количество секунд, а моя программа преобразует их в часы и минуты:'))
hour = user_choice // 3600
minutes = (user_choice - hour * 3600) // 60
seconds = user_choice % 60
# print(' {:02}:{:02}:{:02}:'.format(hour, minutes, seconds)) - такое решение нашел в интерете-
#не знаю по какому принципу оно работает, но оно работает.
print(f' {hour}:{minutes}:{seconds}')
