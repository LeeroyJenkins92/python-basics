print('Задача 9. Выражение')
print()

#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 

x = int(input('Введите число X: '))
summ1 = 1
summ2 = 1
for num in range (1, 7):
    summ1 *= x - (2 ** num - 1)
for num in range (1, 7):
    summ2 *= x - (2 ** num)
print('Выражение равно: ', summ1 / summ2)

