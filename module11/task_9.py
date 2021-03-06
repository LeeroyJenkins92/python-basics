print('Задача 9. Уравнение')
print()
# Даны действительные коэффициенты a, b, c,
# при этом a≠0. 
# Решите квадратное уравнение ax^2+bx+c=0 и выведите все его корни.
# 
# Если уравнение имеет два корня,
# выведите два корня в порядке возрастания,
# если один корень — выведите одно число, 
# если нет корней — не выводите ничего

import math

a = float(input("Введите число А: "))
while a < 0:
    print("Указано некорректное значение элемента")
    dot_x = float(input("Введите число А: "))
b = float(input("Введите число B: "))
c = float(input("Введите число C: "))

discr = b ** 2 - 4 * a * c

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = ",x1,"\nx2 = ",x2)
elif discr == 0:
    x = -b / (2 * a)
    print("x = ", x)
else:
    print("Корней нет")
