print('Задача 9. Пирамидка 2')
print()
# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input('Введите количество уровней пирамиды: '))
numeral = 1
for row in range(height):
    print(row)
    space = height - row - 1
    print('   ' * space, end = '')
    for col in range(row+1):
        print(numeral, end = '    ')
        numeral += 2
    print()