# # text = '''
# # 1
# # 2
# # 3
# # '''[1:-1].split('\n')
# #
# # if text[0] == 'раз':
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
#
#
for val1 in ('раз', '==='):
    for val2 in '02':
        for val3 in '03':
            print(val1, val2, val3, end='\t')
            if val1 == "раз" and val2 == "2" and val3 == "3":
                print('ГОРИ')
            else:
                print('НЕ ГОРИ')


# # Считываем три строки
# str1 = input()
# str2 = input()
# str3 = input()
#
# # Проверяем, если все три строки равны "раз", "два", "три" или "1", "2", "3"
# if (str1 in ["раз", "1"]) and (str2 in ["два", "2"]) and (str3 in ["три", "3"]):
#     print("ГОРИ")
# else:
#     print("НЕ ГОРИ")x
#

