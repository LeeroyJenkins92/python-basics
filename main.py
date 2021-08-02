print('Я не могу написать симфонию, я не смогу создать шедевр, но если ты загадаешь число, я отгадаю его. Прошу тебя загадать число.')
first = 1
last = 100
try_count = 0
while True:
  N = (first + last) // 2
  try_count += 1
  print('Твое число равно/большe/меньше, чем ', N, '?')
  tryy = int(input('Введи свой ответ: 1 - равно; 2 - больше; 3 - меньше. '))
  if tryy == 2:
    first = N
  elif tryy == 3:
    last = N
  else:
    print('Я угадал с ', try_count, ' попытки!!! Твое число -', N)
    break 