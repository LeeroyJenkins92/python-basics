# Задача 2. Провизия

# Одна государственная компания поставляет еду на разные труднодоступные базы (полярные, горные и так далее) в разных уголках страны.
# В компании для удобства расчёта количества еды была реализована такая программа:

# Скопируйте программу в реплит и модифицируйте её: напишите функцию, которая заменит повторяющийся код внутри основной программы.

def count():
    a = int(input())
    b = int(input())
    print("Всего", a+b, "шт.")

print("Сколько мешков рыбы и мяса?")
count()
print("Сколько буханок белого и чёрного хлеба?")
count()
print("Сколько вёдер воды и молока?")
count()