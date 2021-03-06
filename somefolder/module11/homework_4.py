# Задача 2. Компьютерное зрение

# Вы участвуете в разработке робота, который играет в шахматы на реальной, физической шахматной доске размером 0.8 х 0.8 метра. 
# Робот смотрит камерой на доску и видит расположение фигур в вещественных числах с очень высокой точностью.

# Напишите программу, в которую вводятся вещественные координаты шахматной фигуры, 
# а программа определяет в какой клетке доски находится эта фигура. Каждая клетка доски имеет размер 10х10 см и целочисленные координаты, состоящие из двух чисел. 
# Например левая верхняя клетка имеет целые координаты (0, 0), справа от неё клетка (1, 0) а снизу (0, 1). Также обеспечьте контроль ввода: нельзя выходить за границы доски.

# Модифицируйте программу “Компьютерное зрение” так, чтобы она выдавала не только номера клетки, 
# в которой находится фигура но и две вещественных поправки: на сколько нужно подвинуть фигуру по горизонтали и вертикали для того чтобы она оказалась по центру своей клетки.

# Пример:

# Введите местоположение фигуры
# По горизонтали: 0.731
# По вертикали: 0.149

# Фигура находится в клетке (7, 1)

# Введите местоположение фигуры
# По горизонтали: 0.833
# По вертикали: -0.132

# Клетки с такой координатой не существует

x = float(input("Введите расположение по горизонтали: "))
y = float(input("Введите расположение по вертикали: "))
maxx = 0.8

while x < 0 or y < 0 or x > maxx or y > maxx:
    print("Указано некорректное значение элемента")
    x = float(input("Введите расположение по горизонтали: "))
    y = float(input("Введите расположение по вертикали: "))

dotx,doty = x * 10, y * 10
xSquare = int(x * 10)
ySquare = int(y * 10)

print("Фигура находится в: ", xSquare, ySquare)

xMove = round((xSquare + 0.5) - dotx, 2)
yMove = round((ySquare + 0.5) - doty, 2)

print("Фигуру необходимо подвинуть на: ",xMove / 10, yMove / 10)