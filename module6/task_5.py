print('Задача 5. Счастливый билетик')
print()
# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?

num = int(input('Введите шестизначный номер билета: '))
num1 = num // 1000
num2 = num % 1000
last_summ = 0
first_summ = 0
if num >= 100000:
    last_num = (num2 // 100) + (num2 // 10 % 10) + (num2 % 10)
    last_summ += last_num
    first_num = (num1 // 100) + (num1 // 10 % 10) + (num1 % 10)
    first_summ += first_num
    if first_summ == last_summ:
            print("счастливый билет!")
    else:
            print("билет несчастливый")
else:
    print("неверный номер билета")