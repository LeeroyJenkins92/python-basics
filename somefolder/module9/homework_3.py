# Задача 3. Табло
# Петя пишет компьютерную спортивную игру,
# где каждый “гол” это десять очков. 
# Он хочет сделать красивое табло с градацией этих очков.

# Пользователь вводит число N (N >= 0). Реализуйте программу, которая выводит в одну строчку каждое десятое число, 
# разделяя их символами “-=-”. Эти же символы стоят перед первым числом и после последнего.

# Пример:
# Введите число: 50
# -=- 0 -=- 10 -=- 20 -=- 30 -=- 40 -=- 50 -=-
print()

n = int(input("Введите число: "))

for num in range(0, n + 1, 10) :
    print("-=-", num, end=" ")
print(end="-=-" )
