number = int(input("Введите начальное число: "))
numberk = number + 1
for i in range(4):
    
    number += numberk
    numberk+=1
    
    number *= numberk
    numberk+=1

print("Результат:", number)