print('Задача 4. Календари')
print()
# Ваня увлекается историей, а в особенности календарями.
# Он изучает календари разных времён, эпох и народностей. 
# Для исследования ему нужно посчитать,
# у кого сколько было месяцев с чётным количеством дней.

# Напишите программу,
# которая считает количество только чётных чисел в последовательности 
# (последовательность заканчивается при вводе нуля)
# и выводит ответ на экран.

num = int(input('Введите положительное число: '))
summ = 0

while num != 0:
    last_num = num % 10
    summ += last_num
    # num = int(input('Введите положительное число: '))
    if num % 2 == 0:
        summ += 1
        print("Кол-во четных чисел ", summ)

print("Нарушена последовательность")
