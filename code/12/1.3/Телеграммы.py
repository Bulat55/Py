message = input("Введите сообщение: ")

cost = len(message) * 40

rubles = cost // 100
kopecks = cost % 100

print(f"{rubles} р. {kopecks} коп.")