# import os
# abs_path = os.path.abspath('my_file')
# print(abs_path)


# file = open('/Users/ШАГ/Course creating web applications with Python/Tutorials for Python/module_7/my_file.txt')
#
#
# try:
#     file = open('my_file2.txt')
# except FileNotFoundError:
#     print('Невозможно открыть файл')
#
#
# file = open('out.txt', 'w')

# _____________________________________________________
# try:
#     file = open('my_file.txt', encoding='utf-8')
#     print(file.read(13))
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# _____________________________________________________

# try:
#     file = open('my_file.txt', encoding='utf-8')
#     print(file.readline(), end="")
#     print(file.readline(), end="")
#     # for line in file:
#     #     print(line, end="")
# except FileNotFoundError:
#     print('Невозможно открыть файл')

# _____________________________________________________
# try:
#     file = open('my_file.txt')
#     try:
#         s = file.readlines()
#         print(s)
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Невозможно открыть файл')
# _____________________________________________________
# file = open("out.txt", "w")
# file.write("Hello World\n!")
#
# # file.write("Привет мир!")
#
# file.write("Hello1\n")
# file.write("Hello2\n")
# file.write("Hello3\n")

# _____________________________________________________
# file = open("out.txt", "a")
# file.writelines(["Hello1\n", "Hello2\n"])
# _____________________________________________________
# import pickle
#
# books = [
#     ("Евгений Онегин", "Пушкин А.С.", 200),
#     ("Муму", "Тургенев И.С.", 250),
#     ("Мастер и Маргарита", "Булгаков М.А.", 500),
#     ("Мертвые души", "Гоголь Н.В.", 190)
# ]
#
# try:
#     file = open("out.bin", "wb")
#     try:
#         pickle.dump(books, file)
#
#         bs = pickle.load(file)
#         print(bs)
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Невозможно открыть файл')

# _____________________________________________________
# import pickle
# book1 = ["Евгений Онегин", "Пушкин А.С.", 200]
# book2 = ["Муму", "Тургенев И.С.", 250]
# book3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
# book4 = ["Мертвые души", "Гоголь Н.В.", 190]
# try:
#     file = open("out.bin", "wb")
#     try:
#         pickle.dump(book1, file)
#         pickle.dump(book2, file)
#         pickle.dump(book3, file)
#         pickle.dump(book4, file)
#
#         # b1 = pickle.load(file)
#         # b2 = pickle.load(file)
#         # b3 = pickle.load(file)
#         # b4 = pickle.load(file)
#         #
#         # print(b1, b2, b3, b4, sep="\n")
#
#     finally:
#         file.close()
# except FileNotFoundError:
#     print("Невозможно открыть файл")

# _____________________________________________________





















