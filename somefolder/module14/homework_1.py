print("Введите первую точку")

x1 = float(input('X: '))

y1 = float(input('Y: '))

print("\nВведите вторую точку")

x2 = float(input('X: '))

y2 = float(input('Y: '))

x_diff = abs(x1 - x2)

y_diff = abs(y1 - y2)
if x_diff > y_diff:
    k = y_diff / x_diff
else:
    k = x_diff / y_diff

b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")

print("y = ", k, " * x + ", b)
