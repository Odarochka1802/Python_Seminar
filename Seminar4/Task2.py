# 2. Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента, а значение —
# имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def key_parameters(**kwargs):
    dict = {}
    for k, v in kwargs.items():
        if v.__hash__ is not None:
            dict[v] = k
        else:
            dict["".join([str(i) for i in v])] = k
    return dict


print(key_parameters(action='VOOOOOM', voltage=1000000, l=['dds', 4, '324'], s=('eer', '32e', 4),
                     d = {4:"ttt"}))
