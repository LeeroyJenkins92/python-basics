print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
n = 0

def summ(n1, n2):
    summ = n1 + n2 
    print("\nСумма перевернутых чисел %.1d и %.1d равна: " % (n1, n2),summ)
    revsumm(summ)

def revsumm(summ):
    n = summ
    revsumm = 0
    while summ > 0:
        digit = summ % 10
        summ //= 10
        revsumm *= 10
        revsumm += digit
    print("\nЧисло наоборот от числа %.1d составляет: " % (n), revsumm)

def rev1(num1):
    n = num1
    n1 = 0
    while num1 > 0:
        digit = num1 % 10
        num1 //= 10
        n1 *= 10
        n1 += digit
    print("\nЧисло наоборот от числа %.1d составляет: " % (n), n1)
    rev2(num2, n1)


def rev2(num2, n1):
    n = num2
    n2 = 0
    while num2 > 0:
        digit = num2 % 10
        num2 //= 10
        n2 *= 10
        n2 += digit
    print("\nЧисло наоборот от числа %.1d составляет: " % (n), n2)
    summ(n1, n2)
rev1(num1)
