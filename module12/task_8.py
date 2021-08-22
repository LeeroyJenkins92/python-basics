print('Задача 8. НОД')
print()
#Напишите функцию, вычисляющую наибольший общий делитель двух чисел
import math
def euclid():
    num1 = int(input("Введите 1ое число: "))
    num2 = int(input("Введите 2ое число: "))
    out(num1, num2)
def out(num1, num2):
    biggest = int(((num1 + num2) + abs(num1 - num2)) / 2)
    smallest = int(((num1 + num2) - abs(num1 - num2)) / 2)
    print(math.gcd(biggest, smallest))
euclid()
