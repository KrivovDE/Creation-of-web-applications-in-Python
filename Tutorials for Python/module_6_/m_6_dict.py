# languages = ['Python', 'C#', 'Java', 'C++']
# creators = ['Гвидо ван Россум', 'Андерс Хейлсберг', 'Джеймс Гослинг', 'Бьёрн Страуструп']
#
# print('Создателем языка', languages[0], 'является', creators[0])
#
# # #--------------------------------------------------
# languages = [('Python', 'Гвидо ван Россум'),
#              ('C#', 'Андерс Хейлсберг'),
#              ('Java', 'Джеймс Гослинг'),
#              ('C++', 'Бьёрн Страуструп')]
#
# print('Создателем языка', languages[2][0], 'является', languages[2][1])
#
# for item in languages:
#     if item[0] == 'C++':
#         print('Создателем языка', item[0], 'является', item[1])

# #--------------------------------------------------
# languages = {'Python': 'Гвидо ван Россум',
#              'C#': 'Андерс Хейлсберг',
#              'Java': 'Джеймс Гослинг',
#              'C++': 'Бьёрн Страуструп'
#              }
# print('Создателем языка Python является', languages['Python'])

# #--------------------------------------------------

# d = {"house": "дом",
#      "car": "машина",
#      "tree": "дерево",
#      "road": "дорога",
#      "river": "река"
#      }
#
# print(d["house"])
# print(d[100])
#
# d2 = dict(house="дом", car="машина",
#           tree="дерево",
#           road="дорога",
#           river="река"
#           )
#
# # d2 = dict(1 = "дом", 2 = "машина")
#
# #--------------------------------------------------
# lst = [[2, "неудовлетворительно"], [3, "удовлетворительно"], [4, "хорошо"], [5, "отлично"]]
# d3 = dict(lst)
#
# a = dict.fromkeys(["+7", "+6", "+5", "+4"])
#
# c = dict.fromkeys(["+7", "+6", "+5", "+4"], "код страны")
# --------------------------------------------------
# d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
# --------------------------------------------------
# d = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 5}
# for x in d:
#      print(x)


# --------------------------------------------------
# d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}

# d2 = d.copy()
# d2["list"] = [5,6,7]
# print(d)
# print(d2)

# --------------------------------------------------
# d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}

# d.get("list")
# d["list"]
# print(d.get(3))

# --------------------------------------------------
# d = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 5}
#
# print(d.setdefault("list"))
# print((d.setdefault(3)))
# print(d)
#
#
# #--------------------------------------------------
# d.pop(3)
# d.pop("abc")
# d.pop("abc", False)
#

# --------------------------------------------------
# d = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 5}
#
# # for x in d:
# #     print(x, end=' ')
# # print()
# #
# # for x in d.keys():
# #     print(x, end=' ')
# # print()
# #
# # for x in d.values():
# #     print(x, end=' ')
#
# # --------------------------------------------------
# for key, value in d.items():
#     print(key, value)


# --------------------------------------------------
# info = {'name': 'Timur',
#         'age': 28,
#         'job': 'Teacher',
#         'city': 'Moscow',
#         'email': 'timyr-guev@yandex.ru'}
#
# print(info['name'])
# print(info['email'])


# --------------------------------------------------
# Подвиг.
# Вводятся данные в формате ключ=значение в одну строчку через пробел. Необходимо на их основе создать словарь d,
# затем удалить из этого словаря ключи 'False' и '3', если они существуют. Ключами и значениями словаря являются строки.
# Вывести полученный словарь на экран.
# лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина

# lst_in = input().split()
#
# d = {}
# for i in lst_in:
#     k, v = i.split('=')
#     d[k] = v
# if 'False' in d and '3' in d:
#     del d['False']
#     del d['3']
# print(*sorted(d.items()))

# d = dict([i.split('=') for i in input().split()])
#
# del_values = ['False', '3']
#
# for i in del_values:
#     if i in d:
#         del d[i]
#
# print(*sorted(d.items()))
# --------------------------------------------------


# Подвиг.
# Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д.
# Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров
# (следующих в том же порядке, что и во входной строке) с соответствующими кодами. Полученный словарь вывести
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890


# lst = input().split()
# d = {}
# for s in lst:
#     c = s[:2]
#     if c in d:
#         d[c].append(s)
#     else:
#         d[c] = [s]
# print(*sorted(d.items()))















