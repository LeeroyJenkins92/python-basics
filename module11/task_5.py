print('Задача 5. Простые числа')
print()
#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.

seqnum = int(input('Сколько будет чисел: '))
count = 0

for num in range(seqnum):
    print("Введите", num, "-e число ")
    number = int(input())
    while number < 0:
        number = int(input('число не может быть отрицательным! введите число повторно: '))
    prime = True
    for n in range(2, number):
        if number % n == 0:
            prime = False
            break
    if prime:
        count += 1
    print()
print("количество простых чисел в заданной последовательности: ", count)
