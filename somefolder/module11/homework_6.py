# Задача 3. Мега-калькулятор

# Кеша учится в третьем классе, и уже умеет программировать на питоне. 
# Как и многие его одноклассники, он очень любит сразу применять все полученные знания на практике. 
# Вчера Кеша узнал про модуль math и его основные возможности, поэтому решил написать мега-калькулятор, который бы применял сразу все функции к введенному пользователем числу. 
# Чтобы ничего не забыть, он пользуется шпаргалкой, которую прикрепили к уроку

# Напишите программу, которая получает от пользователя вещественное число, по очереди применяет к нему функции модуля Math и выводит результат:

# округляет вниз
# округляет вверх
# берет модуль числа
# извлекает квадратный корень
# возводит экспоненту в степень, равную числу
# считает натуральный логарифм числа
# считает логарифм числа по основанию 2
# считает логарифм числа по основанию 10
# считает синус и косинус числа

# И так как Кеша самый умный в классе, он решил попробовать посчитать факториал числа. Для этого ему пришлось придумать и реализовать контроль ввода: факториал вычисляется, только если введенное число было натуральным.

import math
while True:
    num = float(input("введите число: "))
    print("Округляет вниз: ", math.floor(num))
    print("Округляет вверх: ", math.ceil(num))
    print("берет модуль числа: ", abs(num))
    print("извлекает квадратный корень: ", math.sqrt(num))
    print("возводит экспоненту в степень, равную числу: ", math.exp(num))
    print("считает натуральный логарифм числа: ", math.log(num))
    print("считает натуральный логарифм числа по основанию 2: ", math.log(num, 2))
    print("считает натуральный логарифм числа по основанию 10: ", math.log(num, 10))
    print("считает синус угла: ", math.sin(num))
    print("считает косинус угла: ", math.cos(num))


