text = '''
qwerty112233
qwerty1999@gmail.com
'''[1:-1].split('\n')

if '@' not in text[0]:
    if '@' in text[1]:
        print('OK')
    else:
        print('Некорректный адрес')
else:
    print('Некорректный логин')