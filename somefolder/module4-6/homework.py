money = int(input('Введите исходное кол-во денег: '))
cheese = 60
icecr = 20

if money >= 60:
    money -= cheese
    print("На сыр денег хватило")
    if money >= icecr:
        print("И на мороженное тоже!")
else:
    print("Нужно больше золота!")

