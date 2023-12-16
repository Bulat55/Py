number = input("Введите трехзначное число: ")

digit1 = int(number[0])
digit2 = int(number[1])
digit3 = int(number[2])

sum_high = digit1 + digit2
sum_low = digit2 + digit3

new_number = str(max(sum_high, sum_low)) + str(min(sum_high, sum_low))

print(new_number)