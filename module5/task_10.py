print('Задача 10. Почта')
print()

num = int(input('Введите время в часах от 0 до 23: '))

# Первый способ

if (num >= 8) and (num < 10) or (num > 12) and (num < 14) or (num >= 15) and (num < 18) or (num > 20) and (num < 22) :
    print("Можно получить посылку")
else:
    print("Почта не работает")

#Второй способ

if (num < 8) or (num >= 10) and (num < 13) or (num == 14) or (num >= 18) and (num < 21) or (num >= 22) :
    print("Посылку получить нельзя")
else:
    print("Посылку получить можно!")
