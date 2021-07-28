print('Задача 7. Поездка по кругу')
print()

value_v = int(input('Введите скорость Васи (в км/ч): '))
value_t = int(input('Введите время поездки Васи (в часах): '))

formula = (value_v * value_t) % 115
print("Вася остановился на километре №", formula)
