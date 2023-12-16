# text = '''
# # один
# # два
# # три
# # '''[1:-1].split('\n')
# #
# # if text[0] == 'раз' or 'один':
# #     if text[1] == 'два':
# #         if text[2] == 'три':
# #             print('Гори')
# #         else:
# #             print('Не гори')
# #     else:
# #         print('Не гори')
# # elif text[0] == '1':
# #     if text[1] == '2':
# #         if text[2] == '3':
# #             print('Гори')
# #         else:
# #             print('Не гори')
# #     else:
# #         print('Не гори')
# # else:
# #     print('Не гори')


for val1 in ('один', '===='):
    val1 = "один" if val1 == "раз" else val1
    # val2 = "два" if val2 == "два" else val2
    # val3 = "три" if val3 == "три" else val3
    for val2 in '02':
        for val3 in '03':
            print(val1, val2, val3, end='\t')
            if (val1 in ["один", "1"]) and (val2 in ["два", "2"]) and (val3 in ["три", "3"]):
                print('ГОРИ')
            else:
                print('НЕ ГОРИ')