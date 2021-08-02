print('Задача 7. Костя хочет выигрывать')
print()

num1 = int(input('Введите 1ое число: '))
num2 = int(input('Введите 2ое число: '))
num3 = int(input('Введите 3e число: '))

if (num1 == num2) and (num1 == num3) :
    print(3)
elif (num1 == num2) or (num1 == num3) or (num2 == num3) :
    print(2)
else:
    print(0)
