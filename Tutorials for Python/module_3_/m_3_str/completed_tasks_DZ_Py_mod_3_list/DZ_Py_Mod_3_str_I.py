# Задание 1
# Пользователь вводит с клавиатуры строку.
# - Произведите поворот строки.
# - Посчитайте количество букв, цифр в строке.
# Пользователь вводит с клавиатуры строку
# Полученный результат выведите на экран.


import re
line = input("Введите буквы и цифры и я все посчитаю, а в подарок поменяю все с ног на голову: ")
stroka_rewers = line[::-1]
line_numbers = len(re.findall('[0-9]', line))
line_letters = len(re.findall('[A-я]', line))
print("Переворачиваем сторону: ", stroka_rewers)
print("Всего цифр: ", line_numbers)
print("Всего букв: ", line_letters)

# Задание 2
# Пользователь вводит с клавиатуры строку и символ или слово для поиска.
# Посчитайте сколько раз в строке встречается этот символ или слово,
# Полученный результат выведите на экран.
#
zona_poiska = input("Введите срооку: ")
search = input("Введите что найти: ")
zona_poiska_ok = zona_poiska.count(search)
print(zona_poiska_ok)


# Задание 3
# Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены. Произведите в строке замену одного слова на другое.
# Полученную строку отобразите на экране.
#
line = input("Введите строку: ")
word = input("Введите слово для поиска: ")
replacement = input("Введите слово для замены: ")
replacement_ok = line.replace(word, replacement)
print(replacement_ok)

# Задание 4
# Есть некоторый текст.
# Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в тексте.
# Полученный результат выведите на экран.

import re
text = '''В Python 3.12 появилась поддержка perf profiling. В этой статье
рассмотрим, как это помогает сократить время выполнения Python-
скрипта с 36 секунд до 0,8! мы рассмотрим Linux-инструмент perf, а
также графики Flame Graph (добавить пояснение: способ визуализации
процессорного времени, потраченного на функции), посмотрим на
дизассемблированный код и займемся поиском ошибок.
загляните на соответствующую страницу официальной документации
Python и в список изменений. Для этой статьи из документов по
ссылкам выше важно следующее:
Профилировщик perf для Linux является мощным инструментом,
который позволяет профилировать и получать информацию о
производительности приложения. У perf богатая экосистема
инструментов, которые помогают с анализом данных, которые он
производит.
основная проблема при использовании профилировщика perf с
приложениями Python состоит в том, что perf позволяет получить
информацию только о нативных символах, то есть об именах функций
и процедур, написанных на C. Это значит, что имена и названия файлов
функций Python в вашем коде в выводе perf не появятся.
начиная с Python 3.12, интерпретатор может работать в специальном
режиме, который позволяет функциям Python появляться в выводе
профилировщика perf! при включенном режиме интерпретатор
вставляет небольшой фрагмент кода, скомпилированный на лету, перед
выполнением каждой функции Python и обучает perf взаимосвязи
между этим фрагментом кода и связанной с ним функцией Python с
помощью файлов perf map.'''
text_up = ""
for i in re.split(r'([.!?]\s+)', text):
    text_up += i[0].upper() + i[1:]
text_numbers = len(re.findall('[0-9]', text))
text_signs = len(re.findall('[.|,|!|?|:|;]', text))
text_exclamation_mark = len(re.findall('[!]', text))
print(text_up.strip())
print("Всего цыфр: ", text_numbers)
print("Всего знаков препинания: ", text_signs)
print("Восклицательный знак встречается: ", text_exclamation_mark)
