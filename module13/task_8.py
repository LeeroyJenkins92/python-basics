print('Задача 8. Сумма ряда')
print()
# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

def summ(precision, x):
  previous = i = 0
  current = fn = xn = 1
  while abs(current - previous) > precision:
    previous = current
    xn *= x * x
    i += 1
    fn *= 2 * i * (2 * i - 1)
    current += (-1 if i % 2 else 1) * xn / fn
  return current

print("Сумма ряда =", summ(float(input("Введите точность: ")), float(input("Введите X: "))))