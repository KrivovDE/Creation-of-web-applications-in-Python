## Задача 8. Бегущая строка
### Что нужно сделать
В одной из практических работ вы писали для табло программу,
которая циклически сдвигает элементы списка чисел вправо на K позиций.
В этот раз вы работаете с двумя строками. Нужно проверить, не равна ли на самом деле одна другой.
Возможно, одна из них просто немного сдвинута.

Пользователь вводит две строки. Напишите программу, которая определяет,
можно ли первую строку получить из второй циклическим сдвигом.

Опционально: если получить можно, то выведите значение этого сдвига.

Пример 1:

```
Первая строка: abcd
Вторая строка: cdab

Первая строка получается из второй со сдвигом 2.
```

Пример 2:

```
Первая строка: abcd
Вторая строка: cdba

Первую строку нельзя получить из второй с помощью циклического сдвига.
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода.
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
