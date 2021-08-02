print('Задача 1. Калькулятор опыта')
print()

exp = int(input('Введите кол-во опыта: '))
if exp >= 5000:
    print("Ваш уровень:4")
elif exp < 5000 and exp >= 2500:
    print("Ваш уровень:3")
elif exp < 2500 and exp >= 1000:
    print("Ваш уровень:2")
else:
    print("Ваш уровень:1")
