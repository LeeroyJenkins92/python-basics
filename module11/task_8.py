print("Задача 8. Часы")
print()
# С начала суток часовая стрелка повернулась на угол в α градусов.
# Определите на какой угол повернулась минутная стрелка с начала последнего часа. Входные и выходные данные — действительные числа.

# При решении этой задачи нельзя пользоваться условными операторами и циклами.

hour_angle = float(input("Введите угол: "))

min_angle = round(hour_angle % 30 * 12, 2)



print("Минутная стрелка повернулась на: ", min_angle, "градусов")
