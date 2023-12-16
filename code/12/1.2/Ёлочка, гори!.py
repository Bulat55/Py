# text = '''
# раз
# два
# три
# '''[1:-1].split('\n')
#
# val1, val2, val3 = text


for val1 in '01':
    for val2 in '02':
        for val3 in '03':
            print(val1, val2, val3, end='\t')
            if val1 == '1':
                if val2 == '2':
                    if val3 == '3':
                        print('ГОРИ')
                    else:
                        print('НЕ ГОРИ')
                else:
                    print('НЕ ГОРИ')
            else:
                print('НЕ ГОРИ')


