# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
import random

spisok_vechey = ['vech1', 'vech2', 'vech3','vech4','vech5','vech6','vech7','vech8','vech9']

slovar ={
    'friend1': tuple(random.sample(spisok_vechey, 3)),
    'friend2': tuple(random.sample(spisok_vechey, 4)),
    'friend3': tuple(random.sample(spisok_vechey, 3))
}
for k,v in slovar.items():
    print(f" Друг {k} взял такие вещи: {v}")

#Есть у всех
un = set()
for friend, vech in slovar.items():
    un = set(vech) | un

print(f"Взяли все друзья: {un} ")

#Уникальные вещи
un = set.difference(*[set(vech) for friend, vech in slovar.items()])
spisok_unic_vechey = []
for i in un:
    for friend, vech in slovar.items():
        if i in vech:
            spisok_unic_vechey.append(f"Только {friend} взял {i}")
if spisok_unic_vechey:
    print(*spisok_unic_vechey)
else:
    print("Нет уникальных вещей")

#У всех кроме одного
d=[]
for k,v in slovar.items():
    for i in v:
        d.append(i)

d={k: d.count(k) for k in d}

result_sp =[]
for k,v in d.items():
    if v==len(slovar)-1:
        result_sp.append(k)
for k,v in slovar.items():
    for i in result_sp:
        if i not in v:
            print(f"У {k} отсутствует {i} а у других друзей присутствует")