from typing import Set, List, Tuple

set_a: Set[int] = {1, 2, 3, 4}
set_b: Set[int] = {3, 4, 5, 6, 7}
# ---------------------------------------------------------------------

# res_1: set = set_a & set_b
#
# res_2: set = set_a.intersection(set_b)
#
# print(res_1, res_2)
# # ---------------------------------------------------------------------
#
# res_3: set = set_a | set_b
#
# res_4: set = set_a.union(set_b)
#
# print(res_3, res_4)

# ---------------------------------------------------------------------

# res_4: set = set_a - set_b
#
# res_5: set = set_b - set_a
#
# print(res_4, res_5)

# ---------------------------------------------------------------------

# res_6: set = set_b ^ set_a
#
# print(res_6)

# ---------------------------------------------------------------------
# mylist: List[int] = [2021, 2020, 2019, 2018, 2017, 2016]
# mytuple: Tuple[int, ...] = (2021, 2020, 2016)
# mystr: str = 'abcdddd'
#
# myset: Set[int] = {2009, 2010, 2016}
#
# print(myset.union(mystr))              # объединяем со строкой
# print(myset.intersection(mylist))      # пересекаем со списком
# print(myset.difference(mytuple))       # находим разность с кортежем


# ---------------------------------------------------------------------
myset1: Set[int] = {1, 2, 3, 4, 5, 6}
myset2: Set[int] = {2, 3, 4, 5}
myset3: Set[int] = {5, 6, 7, 8}
#
# union1: Set[int] = myset1.union(myset2, myset3)
# union2: Set[int] = myset1 | myset2 | myset3
#
# difference1: Set[int] = myset1.difference(myset2, myset3)
# difference2: Set[int] = myset1 - myset2 - myset3       # порядок выполнения слева-направо
#
# print(union1 == union2)
# print(difference1 == difference2)


# ---------------------------------------------------------------------
# symdifference: Set[int] = myset1 ^ myset2 ^ myset3  # порядок выполнения слева-направо
#
# symdifference = myset1.symmetric_difference(myset2, myset3) #TypeError: symmetric_difference() takes exactly one argument (2 given)
#
# print(symdifference)
# ---------------------------------------------------------------------

# digits: Set[int] = set()
#
# for c in input():
#     digits.add(int(c))
#
# digits = {int(c) for c in input()}
# ---------------------------------------------------------------------


# # 1. Создать множество, заполненное квадратами целых чисел от 0 до 9 можно так:
# squares = {i ** 2 for i in range(10)}
#
# # 2. Создать множество, заполненное кубами целых чисел от 10 до 20 можно так:
# cubes = {i ** 3 for i in range(10, 21)}
#
# # 3. Создать множество, заполненное символами строки можно так:
# chars = {c for c in 'abcdefg'}
#
# # 4. требуется создать множество, заполненное только цифрами некоторой строки
# _digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}
# ---------------------------------------------------------------------

# a: set = set('Python')
# b: frozenset = frozenset('Python')
# print(a == b)
# print(type(a))
# print(type(b))

# ---------------------------------------------------------------------
# Подвиг
# Вводится строка, содержащая латинские символы, пробелы и цифры.
# Необходимо выделить из нее все неповторяющиеся цифры (символы от 0 до 9)
# и вывести на экран в одну строку через пробел их в порядке возрастания значений.
# Если цифры отсутствуют, то вывести слово НЕТ.

# entered_str: Set[str] = set([x for x in input() if x.isdigit()])
#
# if entered_str:
#     print(*sorted(entered_str))
# else:
#     print('НЕТ')


# ---------------------------------------------------------------------
# Подвиг
# Вводятся два списка городов каждый с новой строки (в строке названия через пробел), которые объехал Сергей
# в 1-й и 2-й годы своего путешествия по России. Требуется определить, включал ли его маршрут
# во 2-й год все города 1-го года путешествия? Если это так, то вывести ДА, иначе - НЕТ.

# city_1: Set[str] = set(input().split())
# city_2: Set[str] = set(input().split())
#
# print('ДА' if city_1 <= city_2 else 'НЕТ')
# # ---------------------------------------------------------------------
# # Подвиг
# # Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел).
# # Необходимо выбрать и отобразить на экране уникальные числа, присутствующие в первом или втором списках,
# # но отсутствующие одновременно в обоих. Результат выведите на экран.
#
# setA: Set[int] = set(map(int, input().split()))
# setB: Set[int] = set(map(int, input().split()))
#
# s = setA ^ setB
# print(*sorted(s))


# ---------------------------------------------------------------------


