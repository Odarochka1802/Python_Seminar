import argparse
import logging
from venv import logger

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s\n")


def our_hex(n):
    str_d = '0123456789abcdef'
    hex_n = ''
    while n > 0:
        hex_n = str_d[n % 16] + hex_n
        n //= 16
    return hex_n


if __name__ == "__main__":
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Convert a decimal number to hexadecimal.')
    parser.add_argument('number', type=int, help='The decimal number to convert.')

    # Парсинг аргументов командной строки
    args = parser.parse_args()

    try:
        number = args.number
        hex_number = our_hex(number)

        logger.info(f"0x{hex_number} == {hex(number)}")

    except Exception as e:
        logger.exception("An error occurred:")