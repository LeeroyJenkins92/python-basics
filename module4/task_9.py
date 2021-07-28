print('Задача 9. Плохой циферблат')
print()

mileage = int(input('Введите пробег автомобиля: '))
day = int(input('Введите номер дня: '))

if mileage >= 100 and mileage <= 999:
    a,b,c = (mileage // 100)%10, (mileage // 10)%10, mileage % 10
    sum = a + b + c
    if sum > day:
        print("Сброс")
        print("Текущий пробег: ", mileage * 0)
    else:
        print("Сегодня не сломался")
        print("Текущий пробег: ", mileage)
else:
    print("Число пробега должно быть ОБЯЗАТЕЛЬНО 3ех значным")
    print("Текущий пробег: ", mileage)
