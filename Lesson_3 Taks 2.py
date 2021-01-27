def exe_2(**kwargs):
    return list(kwargs.values())


print(exe_2(name=input('Введите имя: '), surname=input('Введите фамилию: '), year=input('Введите дату рождения: '),
            city=input('Укажите город проживания: '), email=input('Введите email: '),
            telephone=input('Укажите номер телефона: ')))
