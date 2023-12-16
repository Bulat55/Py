text = '''
нет
нет
'''[1:-1].split('\n')

if text[0] == text[1]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')