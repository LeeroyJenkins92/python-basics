print('Задача 9. Выражение')
print()

#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 

x = int(input('Введите значение X: '))
diff1 = 1

for num in range(1, 64, 2):
    if num == 5:
        continue
    diff1 *= (x - num)
    
    print(diff1)

