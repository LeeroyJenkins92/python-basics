#Задача 3. Квадраты нечётных чисел
#Вводится число N. Напишите программу, которая выводит квадраты нечетных чисел от 1 до N. Нельзя использовать условные операторы. 
# Можно использовать цикл while, но постарайтесь всё-таки решить с помощью конструкции for in range. 
#Не нужно искать решение в интернете, попробуйте подумать сами, в следующем уроке мы обязательно разберём эту задачу.

num = int(input('Введите число: '))

for n in range(1, num // 2 + num%2 + 1):
    n = (n * 2) + 1
    print(n, "** 2 =", n ** 2)
