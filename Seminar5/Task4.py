# 4. Создайте функцию генератор чисел Фибоначчи.
def iter_fibb(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


n = 5
t = iter_fibb(n)
[print(next(t)) for i in range(n)]
print(("Здесь функция фибоначчи с ограничением в условиию. Усли убрать аргументы - будет выдавать безгранично"))
