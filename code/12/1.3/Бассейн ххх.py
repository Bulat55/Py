a = float(input("Введите длину бассейна (метры): "))
b = float(input("Введите ширину бассейна (метры): "))
c = float(input("Введите глубину бассейна (метры): "))
d = float(input("Введите скорость налива воды (м3/час): "))

volume = a * b * c

hours = volume / d

print(f"Бассейн будет заполнен через {hours} час(ов).")