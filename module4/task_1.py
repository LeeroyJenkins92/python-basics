print('Задача 1. Датчик погоды')
print()

rain = int(input('Введите цифру 1, если пошёл дождь: '))

if rain == 1:
    print("Пошёл дождь. Возьмите зонтик!")
else:   #дождь либо есть либо нет, поэтому решил использовать именно такую конструкцию, вместо еще одного оператора IF
    print("Дождя нет =)")

