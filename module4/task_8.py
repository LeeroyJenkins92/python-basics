print('Задача 8. Тяжёлая жизнь')
print()

hours = int(input('Введите кол-во отработанных часов: '))
balance = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))
zp = 200 * hours / 2 ** 3 + hours

if zp >= (balance + food):
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать!")
