print('Задача 4. С заботой о природе')
print()
# Огромный заповедник поделён на большое количество секторов.
# И у каждого сектора есть номер.
# Мы ответственны за группу секторов с номерами с 30-го по 35-ый
# и нам нужно следить за тем, чтобы посетителей в каждом секторе было меньше 10.
# А заодно и фиксировать для общей статистики, сколько раз это правило было нарушено.
# 
# Напишите программу,
# которая для каждого сектора запрашивает текущее количество людей в нём,
# и если оно больше 10, то фиксирует нарушение.
# В конце выведите количество нарушений
# 
# Пример:
# 
# Людей в 30 секторе: 7
# Всё спокойно.
# Людей в 31 секторе: 11
# Нарушение! Слишком много людей в секторе!
# Людей в 32 секторе: 100
# Нарушение! Слишком много людей в секторе!
# Людей в 33 секторе: 10
# Всё спокойно.
# Людей в 34 секторе: 0
# Всё спокойно.
# Людей в 35 секторе: 1
# Всё спокойно.
# Количество нарушений: 2

sector_first = 30
sector_last = 35
alarm = 0
error = 0

for sector in range(sector_first, sector_last + 1) :
    ppls = int(input('Введите кол-во людей в секторе: '))
    while ppls < 0 :
        ppls = int(input('Указано некорректное значение элемента, введите повторно: '))
        print(sector)
        error += 1                                                          
    print("Людей в", sector, "секторе :", ppls)
    if ppls > 10:
        alarm += 1
        print("Нарушение! Слишком много людей в секторе!")
    else:
        print("Всё спокойно.")
if error == 0:
    print("Количество нарушений:", alarm)

# сделал костыль на проверку вводимых данных. Если введут ошибочно отрицательное число людей, что невозможно, программа завершит работу.
# в идеале сделать так, чтобы выводилась ошибка и итерация в цикле повторилась - не знаю как так сделать :(