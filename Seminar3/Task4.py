# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import itertools

def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'tent': 5, 'water': 5, 'food': 4, 'clothes': 2, 'first aid kit': 1, 'guitar': 2, 'flashlight': 1, 'matches': 0.3, 'umbrella': 0.6}
max_weight = 15
print(pack_backpack(items, max_weight))
# Вот здесь прям натупила, извините за слэнг. Вернула только те ,
# которые подходят условию, но можно было бы без условия на равность максимальному весу и
# вышли все комбинации возможные.
# Тут, наверное, с производительностью будут проблемы
lst=[]
result = []
def powerset(list_name):
    s = list(list_name)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))
for i in powerset(items.keys()):
    lst.append(i)

for i in lst:
    s=0
    for j in i:
        s+=items[j]
    if s==max_weight:
        result.append(i)
print(result)