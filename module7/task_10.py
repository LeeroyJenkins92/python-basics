print('Задача 10.')
print()
#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# 
# Вводится число N,
# далее еще N − 1 чисел: 
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

all = int(input('Введите общее кол-во карточек: '))
summ = 0
last_summ = 0

for card in range(1, all + 1) :
    summ += card
for card in range(all - 1):
    last_card = int(input('Введите номер оставшихся карточек: '))
    summ -= last_card
print("Номер потерявщейся карты: ", summ)
