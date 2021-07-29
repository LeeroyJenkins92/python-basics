print('Задача 9. Прогрессивный налог 2')
print()

profit = int(input('Введите доход: '))

if profit < 10000 :
    tax = profit * 13 / 100
    print("Размер налога 13% равен: ", tax)
elif profit >= 10000 and profit <= 50000 :
    profit -= 10000
    tax = (profit * 20 / 100) + (10000 * 13 / 100)
    print("Размер налога 20% равен: ", tax)
else:
    profit -= 50000
    tax = (profit * 30 / 100) + (40000 * 20 / 100) + (10000 * 13 / 100)
    print("Размер налога 30% равен: ", tax)
    