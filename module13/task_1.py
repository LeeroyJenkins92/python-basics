print('Задача 1. Урок информатики 2')
print()
# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
# 
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
# 
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
# 
# Пример 1:
# 
# Введитечисло: 92345
# 
# Формат плавающей точки: x = 9.2345 * 10 ** 4
# 
# Пример 2:
# 
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

num = float(input("Введите число: "))
mantissa_left = 0
mantissa_right = 0

def left(num, mantissa_left):
    while num > 10:
        num /= 10
        mantissa_left += 1
    return num, mantissa_left
def right(num, mantissa_right):
    while num < 1:
        num *= 10
        mantissa_right -= 1
    return num, mantissa_right

if num >= 1e0:
    left(num, mantissa_left)
    print("Формат плавающей точки:", round(num, 2), "* 10 **", mantissa_left)
else:
    right(num, mantissa_right)
    print("Формат плавающей точки:", round(num, 2), "* 10 **", mantissa_right)
# я не понимаю, как вернуть из функции несколько значений в основную программу.
# Как их теперь вывести в принте в данном случае?



