print('Задача 4. Урок информатики 3')
print()
# Наконец-то учитель смог объяснить детям,
# что такое эта «плавающая точка». Однако долго его радость не продлилась, 
# ведь на следующем уроке нужно будет объяснить такие страшные слова, 
# как «экспоненциальное», «мантисса» и «порядок».
 
# Хоть старшеклассники и знакомы с экспонентой,
# учитель всё равно не уверен, что здесь всё будет понятно. 
# Поэтому для наглядности он также написал программу.

# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу, 
# которая выводит отдельно мантиссу и отдельно порядок этого числа.

num = input("Введите число в экспоненциальной форме: ")
isMantissa = True
before_e, after_e="", ""

for numbers in num:
    if numbers == 'e':
        isMantissa = False
    elif isMantissa:
        before_e += numbers
    else:
        after_e += numbers
print("Мантисса числа %s составляет" % num, before_e)
print("Порядок числа %s составляет" % num, after_e)