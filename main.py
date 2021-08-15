print('Задача 9. Пирамидка 2')
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