print('Задача 6. Игра в кубики')
print()

num1 = int(input('Kostya rolls the dice: '))
num2 = int(input('Owner rolls the dice: '))


if num1 >= num2:
    print("Overall: ",num1 - num2)
    print("Kostya should pay")
else:
    print("Overall: ",num1 + num2)
    print("Owner should pay")
print("Game over")
