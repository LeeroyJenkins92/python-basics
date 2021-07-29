print('Задача 3. Функция')
print()

y = 0
x = int(input('Введите значение Х: '))

if x > 0:
    y = x - 12
    print("Угрек равен: ", y)
elif x == 0 :
    y = 5
    print("Угрек равен: ", y)
else:
    y = x ** 2
    print("Угрек равен: ", y)
