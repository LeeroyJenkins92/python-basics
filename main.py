print('Задача 7. Поездка по кругу')
print()

speed_v = int(input('Введите скорость Васи (в км/ч): '))
time_t = int(input('Введите время поездки Васи (в часах): '))

distance = (speed_v * time_t) % 115
print("Вася остановился на километре №", distance)