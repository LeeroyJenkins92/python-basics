# Задача 1. Сумма чисел 2
print()
# Пользователь вводит число N. 
# Напишите функцию summa_n, которая принимает одно целое положительное число N и находит сумму всех чисел от 1 до N включительно. 
# Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.

num = int(input("Введите число: "))  

def summa_n(num):
    summ = 0
    for n in range(1, num + 1):
        summ += n
    return summ

newsumm = summa_n(num)
print(newsumm)
totalsum = summa_n(newsumm)
print(totalsum)