test_string = '''
0
'''[1:-1].split('\n')[::-1]

def input(promt=''):
    if promt:
        print(promt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp

value = int(input("Фартингов: "))

pens = 4
shilling = 48
pound = 960

def calc(value0):
    res_str = ''

    if value0 >= 960:
        pound = value0 // 960
        value0 -= (960 * pound)
        res_str = f'Фунтов: {pound}\n'

    if value0 >=48:
         shilling = value0 // 48
         value0 -= (960 * shilling)
         res_str = f'Шилиногов: {shilling}\n'

    if value0 >= 4:
        pens = value0 // 4
        value0 -= (4 * pens)
        res_str += f'Пенсов: {pens}\n'

    if 0 < value0 < 4:
        res_str += f'Фартингов: {value0}\n'

        return res_str


if pound > 0:
    print(f"Фунтов: {pound}")
if shilling > 0:
    print(f"Шилингов: {shilling}")
if pens > 0:
    print(f"Пенсов: {pens}")
if value > 0:
    print(f"Фартингов: {value}")