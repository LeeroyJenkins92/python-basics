print('Задача 5. Недоделка 2')
print()
# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

first_n = int(input("Введите первое число: "))
second_n = int(input("Введите второе число: "))
count = 0

def first_n_check(first_n, count):
    temp = first_n
    while temp > 0:
        count += 1
        temp //= 10
    if count < 3:
        print("Указано некорректное значение элемента")
        quit()
    else:
        summ1(first_n, count)

def second_n_check(second_n, count):
    temp = second_n
    while temp > 0:
        count += 1
        temp //= 10
    if count < 4:
        print("Указано некорректное значение элемента")
        quit()
    else:
        summ2(second_n, count)

def summ1(first_n, count):
    last_digit = first_n % 10
    first_digit = first_n // 10 ** (count - 1)
    between_digits = first_n % 10 ** (count - 1) // 10
    first_n = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
    print('\nИзменённое первое число:', first_n)
    return first_n

def summ2(second_n, count):   
    last_digit = second_n % 10
    first_digit = second_n // 10 ** (count - 1)
    between_digits = second_n % 10 ** (count - 1) // 10
    second_n = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
    print('Изменённое второе число:', second_n)
    return second_n

first_n_check(first_n, count)
second_n_check(second_n, count)
print('\nСумма чисел:', summ1(first_n, count) + summ2(second_n, count))