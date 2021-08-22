print('Задача 9. Недоделка')
print()
# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришли
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

import random

def main_menu():
    print("Привет, мешок с костями, давай сыграем!")
    game = int(input("Выбирай игру: \n1 - Камень\\Ножницы\\Бумага \n2 - угадай число?: \n"))
    if game == 1:
        rock_paper_scissors()
    elif game == 2:
        guess_the_number()
    else:
        print("указано некорректно значение элемента\n")
        main_menu()

def rock_paper_scissors():
    comp_count = 0
    human_count = 0
    inventory = ["камень", "ножницы", "бумага"]
    print("Правила знакомы с детства, впереди три раунда, начинаем...")
    for battle in range(1, 4):
        human_choice = input('камень , ножницы или бумага? Что ты выберешь?\n')
        comp_choice = random.choice(inventory)
        while human_choice not in inventory:
            print("Не понимаю, что ты говоришь, напиши еще раз!\n")
            human_choice = input('камень , ножницы или бумага? Что ты выберешь?\n')
            comp_choice = random.choice(inventory)
        while human_choice == comp_choice:
            print("Хватит загадывать то же, что и я! Переигрываем раунд!")
            human_choice = input('камень , ножницы или бумага? Что ты выберешь?\n')
            comp_choice = random.choice(inventory)
        if human_choice == "камень" and comp_choice == "бумага" or human_choice == "ножницы" and comp_choice == "камень" or human_choice == "бумага" and comp_choice == "ножницы":
            print("Раунд мой!")
            print()
            comp_count += 1
            if comp_count == 2 and human_count == 0:
                print("Суперкомпьютер одержал победу над человеком, со счетом %.1d : %.1d" % (comp_count,human_count))
                break
        else:
            print("Ты выиграл раунд :(")
            print()
            human_count += 1
            if human_count == 2 and comp_count == 0:
                print("Человек вырвал победу из лап бездушной машины, со счетом %.1d : %.1d" % (human_count,comp_count))
                break
    if comp_count > human_count and human_count != 0:
        print("Суперкомпьютер одержал победу над человеком, со счетом %.1d : %.1d" % (comp_count,human_count))
    elif human_count > comp_count and comp_count != 0:
        print("Человек вырвал победу из лап бездушной машины, со счетом %.1d : %.1d" % (human_count,comp_count))
    print()
    main_menu()

def guess_the_number():
    count = 3
    print("Может хоть в угадывании чисел ты преуспеешь, пробуй отгадать число от 1 до 10, которое я загадал!")
    print("И помни, у тебя есть три попытки!")
    comp_choice = random.randint(1,10)
    while count != 0:
        human_choice = int(input("Выбирай число: "))
        if human_choice != comp_choice:
            count -= 1
            if count == 0:
                print("Ты проиграл, возвращаюсь в главное меню...")
                break
            print("НЕ угадал! У тебя есть еще %.1d попытки" % (count))
        else:
            print("В этот раз ты победил! Возвращаюсь в главное меню...")
            break
    print()
    main_menu()

main_menu()



