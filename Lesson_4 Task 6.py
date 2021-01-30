# a
from itertools import count

for i in count(int(input('Введите первое число последовательности '))):
    print(i)



# б

from itertools import cycle

my_list = [6445, True, 123, False, None, {1, 2, 3}]
for i in cycle(my_list):
    print(i)


# Везде бесконечная последовательность