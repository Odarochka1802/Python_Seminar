import logging
import os
import argparse
from venv import logger

logging.basicConfig(level=logging.INFO, filename="py_log2.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s\n")

def path_parse(stroka):
    try:
        filepath, file_extension = os.path.splitext(stroka)
        dirname, filename = os.path.split(filepath)
        return dirname, filename, file_extension
    except Exception as e:
        logger.error(f'An error occurred: {e}')
        return None, None, None


if __name__ == '__main__':
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Parse file path.')
    parser.add_argument('file_path', type=str, help='The path to the file.')

    # Парсинг аргументов командной строки
    args = parser.parse_args()

    file_path = args.file_path

    dirname, name, extension = path_parse(file_path)

    if dirname and name and extension:
        logger.info(f'The path to the file: {dirname}\nFile name: {name}\nFile extension: {extension}')
    else:
        logger.exception('An error occurred. Please check the input file path.')