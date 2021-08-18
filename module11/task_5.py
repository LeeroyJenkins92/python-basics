print('Задача 5. Вот это объёмы!')
print()
# Для курсовой работы по физике
# Андрею нужно сравнить объёмы двух планет: Земли и какой-нибудь случайной,
# которая может в теории существовать в нашей вселенной.
# Андрей хорошо разбирается в формулах,
# а вот считать что-то, а уж тем более самому - это явно не его.
# Объём Земли ему известен заранее  - это 10.8321 * 10 ** 11 км3
# 
# А вот объём случайной планеты ему нужно будет посчитать.
# Благо, у него есть формула
# 
# V = 4/3 πR ** 3
# 
# где V - это объём, π - число пи, а R - радиус планеты.
# 
# Напишите программу, 
# которая получает на вход радиус случайной планеты
# и выводит на экран во сколько раз планета Земля меньше или больше по объёму.
# Ответ округлите до трёх знаков после запятой
 
# Пример:
# Введите радиус случайной планеты: 3389.5
# Объём планеты Земля больше в 6.641 раз

# Пример 2:
# Введите радиус случайной планеты: 7000
# Объём планеты Земля меньше в (1/0.754) = 1.326 раз

import math
some_planet_radius = float(input("Введите радиус случайной планеты: "))
earth = 10.8321 * 10 ** 11
some_planet_volume = 4 / 3 * math.pi * some_planet_radius ** 3
diff = round(earth / some_planet_volume, 3)
if earth > some_planet_volume:
    print("Объём планеты Земля больше в ", diff, "раз")
else:
    print("Объём планеты Земля меньше в ", round(1 / diff, 3), "раз")



