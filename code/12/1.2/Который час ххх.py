try:
    time = int(input('Введите время:'))
    if time > 4 and time < 11:
        print('Утро')
    elif time > 10 and time < 18:
        print('День')
    elif time > 17 and time < 23:
        print('Вечер')
    elif time > 2 and time < 24 or time < 5:
        print('Ночь')
    else:
        print('Ошибка')
except:
    print('Ошибка, неккоректное время')