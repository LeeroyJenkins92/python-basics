print('Задача 7. Великий и могучий')
print()
# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на своём языке.
# 
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
# 
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5

text = input("ВВедите текст: ")
count = 0
summ = 0

for letters in text :
    if letters != " " :
        count += 1
        print(count)
        if count > summ:
            summ = count
    else:
        count = 0
print(summ)

