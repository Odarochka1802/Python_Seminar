# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях. Известно,
# что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них
# пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг
# друга верните истину, а если бьют - ложь.

def validate_queens(positions):
    for i in range(8):
        for j in range(i + 1, 8):
            if positions[i] == positions[j] or \
                    positions[i] - i == positions[j] - j or \
                    positions[i] + i == positions[j] + j:
                return False
    return True
