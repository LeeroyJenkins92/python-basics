print('Задача 7. Стипендия')
print()
#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input('Введите размер стипендии: '))
expenses = int(input('Введите кол-во расходов: '))
inflation = 0
total_grant = 0


for n in range(1, 10 + 1, 1):
    total_grant += educational_grant
    if n > 1:
        inflation = expenses * 3 / 100
        expenses += inflation
total_expenses = expenses * 10

if total_expenses > total_grant:
    diff = total_expenses - total_grant
    print("Уважаемые родители, дайте денег: ", diff)
else:
    print("Денег хватает")
        

