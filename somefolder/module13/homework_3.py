# Задача 1. Возможности компьютера
print()
# В одной IT-компании тестируют возможности различных языков программирования, компиляторов и, конечно же, компьютеров. 
# Компания дала вам задачу понять, какое самое маленькое возможное число можно получить путём постоянного деления числа на 2. 
# Изначально число равно единице. Также, помимо самого числа, компания просит вывести количество делений. Реализуйте такую программу.

n = 1
count = 0
while n != 0:
    n /= 2
    count += 1
    print(n)
print("Кол-во итераций: ", count)