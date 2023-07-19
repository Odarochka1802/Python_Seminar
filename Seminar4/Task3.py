# 3. Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
import datetime

total_cash = 0
count = 0


def operations_history(operations, sum_operations, total, flag=True):
    with open('operations_history.txt', 'a+', encoding='utf-8') as history:
        now = datetime.datetime.now()
        if flag:
            history.write(
                f'Successfully {now.strftime("%d-%m-%Y %H:%M")}\n{operations}: {sum_operations}.\nTotal:\n{total}.\n\n')
        else:
            history.write(f'Operation failed: insufficient funds! {now.strftime("%d-%m-%Y %H:%M")}\n{operations}: {sum_operations}.\nTotal:\n{total}.\n\n')


def tax_amount_check(total_cash):
    if total_cash > 5_000_000:
        total_cash *= 0.9


def our_pirnt():
    print("На вашем счету ", total_cash)
    print('''Выберете действие: 
            1. Пополнить
            2. Снять
            3. Выйти
            ''')


def add_cash():
    add = int(input("Внесите сумму кратную 50: "))
    while add % 50 != 0:
        print("Неверная сумма")
        add = int(input("Внесите сумму кратную 50! \nЧтобы вернуться в предыдущее меню нажмите  0 "))
        if add == 0: break
    return add


def withdrawal(total_cash):
    take = int(input("Введите сумму кратную 50: "))
    while take % 50 != 0:
        print("Неверная сумма")
        take = int(input("Введите сумму кратную 50: \nДля выхода нажмите 0 "))
        if take == 0: break
    percent = take * 1.5 * 0.01
    if percent < 30:
        percent = 30
    if percent > 600:
        percent = 600

    if total_cash < (take + percent):
        return None,take
    else:
        total_cash -= (take + percent)
    return total_cash,take


def operation_selection():
    action = input("Введите номер операции: ")
    global count
    global total_cash

    match action:
        case "1":
            add = add_cash()
            total_cash += add
            count += 1
            operations_history("Refill", add, total_cash, flag=True)

        case "2":
            f = withdrawal(total_cash)

            if f[0]:
                total_cash = f[0]
                count += 1
                operations_history("Cash withdrawal", f[1], total_cash)
            else:
                print("Insufficient funds")
                operations_history("Cash withdrawal", f[1], total_cash, flag=False)

        case "3":
            print("На вашем счету ", total_cash)
            print("Выход")
            quit()

    if count == 3:
        total_cash *= 1.03
        count = 0


while True:
    tax_amount_check(total_cash)

    our_pirnt()

    operation_selection()
