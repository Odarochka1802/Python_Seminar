# 3. Напишите однострочный генератор словаря, который принимает на вход три
# списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида «10.25%». В результате получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка
# умноженная на процент премии
import random

names = ['Андрей', 'Елена', 'Юлия', 'Роберт', 'Валерия', 'Амбер']
salaryes = [random.randint(1500, 2500) for i in range(len(names))]
premiums = [str("%.2f" % (random.uniform(10, 23))) + '%' for i in range(len(names))]
print(f'Employees: {names}\nSalary: {salaryes}\nPremium{premiums}')
our_dict = {name: ("%.2f" % (salary * float(premium[:-1]) / 100 + salary)) for name, salary, premium in zip(names, salaryes, premiums)}
print(our_dict)
