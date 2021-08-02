print('Задача 6. Игра в кубики МАСТЕР')
print()

money = int(input('Введите исходное кол-во денег: '))
summ = 0

while money < 10000:
    dice = int(input('Введите число на кубике от 1 до 6: '))
    if dice > 6 or dice < 1:
        print("Введите корректное число")
    elif dice == 3:
        money = 0
        print("YOU LOST EVERYTHING! YOUR MONEY = ", money)
        break
    else:
        money += 500
        print("Вы выиграли 500 рублей", "Итоговая сумма: ", money)
