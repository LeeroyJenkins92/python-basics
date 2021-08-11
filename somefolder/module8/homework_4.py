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
# Саша просыпается когда угодно, но в 23 часа уже точно идёт спать. 
# Питается Саша следующим образом: каждые 3 часа он выпивает литр воды и съедает N калорий. Пить и есть он, кстати, начинает сразу как только проснётся. 
# Напишите программу, которая считает сколько он выпьет литров воды и сколько калорий он съест перед тем как пойдёт спать.

wake = int(input('Когда проснулся Саша?: '))
water = 0
summ = 0

for hours in range(wake, 23, 3):
    water += 1
    print("Время", hours, "часов")
    cals = int(input('Сколько каллорий наел Саша?: '))
    summ += cals

print("Выпил всего воды: ", water)
print("Наел всего еды: ", summ)
