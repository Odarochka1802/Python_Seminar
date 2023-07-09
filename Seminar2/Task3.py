from fractions import Fraction
from math import lcm, gcd


def sum_mult_fraction(a: str, b: str):
    numerator1, denominator1 = map(int, a.split('/'))
    numerator2, denominator2 = map(int, b.split('/'))

    # Вычисляем сумму дробей
    bd = lcm(denominator1, denominator2)
    rn = bd // denominator1 * numerator1 + bd // denominator2 * numerator2
    g2 = gcd(rn, bd)
    n = rn // g2
    d = bd // g2
    sum_frac = n, d

    # Вычисляем произведение дробей
    prod_frac_num = numerator1 * numerator2
    prod_frac_denom = denominator1 * denominator2
    g2 = gcd(prod_frac_num, prod_frac_denom)
    mult_frac = (prod_frac_num // g2, prod_frac_denom // g2)

    return sum_frac, mult_frac


a = input("Введите первую дробь: ")
b = input("Введите вторую дробь: ")

sum_frac, mult_frac = sum_mult_fraction(a, b)

a_f = Fraction(a)
b_f = Fraction(b)
print(f'{a_f + b_f}=={sum_frac[0]}/{sum_frac[1]}, {a_f * b_f}=={mult_frac[0]}/{mult_frac[1]}')
