july_city = input()
august_city = input()

if (july_city == "Тула" and august_city != "Пенза") or (august_city == "Тула" and july_city != "Пенза"):
    print("ДА")
else:
    print("НЕТ")