# Задача 2. Театр
# Ваню заставили пойти в театр на балет. Ему стало там настолько скучно, что он придумал себе очень странное развлечение: считать сумму номеров каждого пятого стула в рядах.

# Напишите программу для вычисления суммы каждого пятого числа, лежащего в диапазоне от единицы до N. Использовать условный оператор нельзя.

# Пример:

# Введите число: 21
# Номер стула: 1
# Номер стула: 6
# Номер стула: 11
# Номер стула: 16
# Номер стула: 21
# Сумма: 55

num = int(input('Введите число: '))
summ = 0

for n in range(1, num + 1, 5):
    print("Номер стула: ", n)
    summ += n
print("Сумма: ", summ)
