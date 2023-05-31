# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
from typing import Tuple

# Имена файлов для отображения
FILE_1 = "d:\\path1\\sub_path1\\file_1.png"
FILE_2 = "d:\\path2\\sub_path2\\file_2.txt"
FILE_3 = "d:\\path3\\sub_path3\\file_3.docx"


def split_path(path: str) -> tuple[str, str, str]:
    """Парсинг абсолютного пути на каталог, имя и расширение файла"""
    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext


def main():
    print(split_path(FILE_1))
    print(split_path(FILE_2))
    print(split_path(FILE_3))


if __name__ == "__main__":
    main()
