import string


def our_hex(n: int) -> string:
    str_d = '0123456789abcdef'
    hex_n = ''
    while n > 0:
        hex_n = str_d[n % 16] + hex_n
        n //= 16
    return hex_n


n = int(input('Введите число: '))
print(f"0x{our_hex(n)} == {hex(n)}")
