def my_func(a, b):
    result = 1
    for i in range(abs(b)):
        result *= a
    if b >= 0:
        return result
    else:
        return 1 / result


print(my_func(int(input("Первое значение: ")), int(input("Второе значение: "))))
