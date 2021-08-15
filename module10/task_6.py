print('Задача 6. Сумма факториалов')
print()
# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 

n = int(input('Введите число N: '))
#n = 4
f = 1
summ = 0
count = 0
total = 0

for fac in range(1, n + 1):
        for num in range(1, fac + 1):
                while num > count:
                        f *= num
                        count += 1
                        summ += f
print("Сумма факториалов данного числа: ",summ)
