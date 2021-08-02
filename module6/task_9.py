print('Задача 9. Игра «Угадай число»')
print()

num_wished = int(input('загадайте число: '))
num_selected = 0
attempt = 0

while num_wished != num_selected:
    attempt += 1
    num_selected = int(input('введите число: '))
    if num_selected < num_wished :
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif num_selected > num_wished :
        print("Число больше, чем нужно. Попробуйте ещё раз!")
print("вы угадали! загаданное число ", attempt)


# В одном из домашних заданий мы делали задачу, 
# где папа-программист написал для сына программу, которая просит его угадать число.
# Недостаток программы был в том, 
# что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. 
# Теперь, когда мы знаем гораздо больше,
# пришло время исправить этот недостаток и заодно немного улучшить саму игру.
 
# Напишите программу-игру,
# которая запрашивает у пользователя число до тех пор,
# пока он его не отгадает.
# Выводите сообщения в соответствии с примером.
 
# Пример (загадали число 7):
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4