print('Задача 7. Наибольшая сумма цифр')
print()
# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

numcount = int(input('Введите кол-во чисел: '))
prevsumm = 0
summ = 0
bignum = 0

for num in range(numcount):
    print("Введите", num, "-e число ")
    number = int(input())
    if number > bignum:
        bignum = number
    while number < 0:
        number = int(input('число не может быть отрицательным! введите число повторно: '))
        if number > bignum:
            bignum = number
    while number > 0:
        digit = number % 10
        prevsumm += digit
        if summ < prevsumm:
            summ = prevsumm
        number //= 10
        prevsumm = 0

print("Сумма: ",summ, "Большее число: ", bignum)    