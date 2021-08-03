print('Задача 5. Факториал')
print()
# Мы всё ближе и ближе подбираемся к серьёзной математике.
# Одна из классических задач - задача на нахождение факториала числа.
# И в будущем мы с ней ещё встретимся.
# 
# Дано натуральное число N. Напишите программу, которая находит N! (N факториал)
# 
# Запись N! означает следующее:
# 
# N! = 1 * 2 * 3 * 4 * 5 * … * N
# 
# Пример:
# 
# Введите число: 5
# Факториал числа 5 равен 120

num = int(input('Введите число: '))
start = 1
factorial = 1
last = num

for num in range(start, last + 1):
        factorial *= num
        print("Факториал числа ",num, "равен", factorial)