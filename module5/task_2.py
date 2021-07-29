print('Задача 2. Максимум из трёх чисел')
print()

num1 = int(input('Введите 1ое число: '))
num2 = int(input('Введите 2ое число: '))
num3 = int(input('Введите 3e число: '))

if num3 < num1 and num2 < num1 :
    print(num1)
elif num3 < num2 and num1 < num2 :
    print(num2)
else:
    print(num3)