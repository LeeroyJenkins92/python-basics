print('Задача 4. Театр')
print()
# Планируется построить театр под открытым небом,
# но для начала нужно хотя бы примерно понять сколько должно быть рядов,
# сидений в них и какое лучше сделать расстояние между рядами.
#
# Напишите программу,
# которая получает на вход кол-во рядов, сидений и свободных метров между рядами,
# а затем выводит примерный макет театра на экран.

# Сцена
# Введите кол-во рядов: 5
# Введите кол-во сидений ряду: 7
# Введите кол-во метров между рядами: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======

row = int(input("Введите кол-во рядов: "))
sit = int(input("Введите кол-во сидений в ряду: "))
meters = int(input("Введите кол-во свободных метров между рядами: "))

for stripes in range(1, row + 1, 1) :
    print("="*sit, end=" ")
    print("*"*meters, end=" ")
    print("="*sit, end=" \n")
