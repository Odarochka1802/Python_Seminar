# Дан список повторяющихся элементов. Вернуть список с
# дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint
from collections import Counter
lst = [randint(0, 10) for i in range(20)]
print("Создали рандомный список с повторяющимеся элементами")
print(lst)

c = Counter(lst)
print("С помощью модуля collections создадим словарь где ключ - это наше число, а значение - колличечтво повторенний")
print(c)
lst_result = [ k for k,v in c.items() if v>1]
print("С помощью генератора списка создали список с определенным условием")
print(lst_result)


# или просто
print("Второй вариант")
counter = {}

for elem in lst:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}
print("Здесь выводим только ключи")
print(doubles.keys())