## Задача 1. Lorem ipsum
### Что нужно сделать
Для макетов веб-страниц часто используется какой-нибудь текст-рыба — это условный,
зачастую бессмысленный текст-заполнитель. Пусть дан следующий сгенерированный текст:

```python
text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate
"""
```
Напишите программу, которая обрабатывает этот текст и выводит список слов, состоящих ровно из четырёх букв.

Результат:
```
['amet', 'elit', 'eget', 'quam', 'quis', 'quis', 'enim', 'pede']
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Решение опирается на использование регулярных выражений и их методов.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
