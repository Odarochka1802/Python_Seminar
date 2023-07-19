# 2. Напишите функцию, которая принимает на вход строку — абсолютный путь
# до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла,
# расширение файла.
import os


def path_parse(stroka):
    filepath, file_extension = os.path.splitext(stroka)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)


path_, name, extension = path_parse(r'C:\python3\file.py')
print(f'The path to the file: {path_}\nFile name: {name}\nFile extension: {extension}')
