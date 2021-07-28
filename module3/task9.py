print('Задача 9. В обратном порядке')
print()

num = int(input('Введите 4ех значное число: '))

a = num % 10
b = (num // 10) % 10
c = (num // 100)%10
d = num // 1000

revert = a * 1000 + b * 100 + c * 10 + d
print(revert)