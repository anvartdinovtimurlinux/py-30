from collections import Counter
from typing import Callable
import json
import xml.etree.ElementTree as ET


def get_top_words(words: list, top_words_count: int, predicate: Callable[[str], bool]) -> list:
    """Программа получает список слов и возвращает список из самых часто встречающихся

    :param words: список слов
    :type words: list
    :param top_words_count: требуемое количество слов для возврата
    :type top_words_count: int
    :param predicate: функция-предикат, определяющая минимальную длину слова
    :type predicate: Callable[[str], bool]
    :return: список самых часто встречающихся слов
    :rtype: list
    """

    words_by_predicate = list(map(str.lower, filter(predicate, words)))
    most_common_words = Counter(words_by_predicate).most_common(top_words_count)
    return [word[0] for word in most_common_words]


def get_list_from_json(path_to_file: str) -> list:
    """Функция принимает JSON файл и возвращает список слов из него

    :param path_to_file: путь к файлу
    :type path_to_file: str
    :return: список слов из файла
    :rtype: list
    """

    with open(path_to_file) as f:
        news = json.load(f)
    word_from_news = [item['description'].split() for item in news['rss']['channel']['items']]
    return sum(word_from_news, [])


def get_list_from_xml(path_to_file: str) -> list:
    """Функция принимает XML файл и возвращает список слов из него

        :param path_to_file: путь к файлу
        :type path_to_file: str
        :return: список слов из файла
        :rtype: list
    """

    tree = ET.parse(path_to_file)
    root = tree.getroot()
    xml_items = root.findall('channel/item')
    xml_items_list = [item.find('description').text.split() for item in xml_items]
    return sum(xml_items_list, [])


def min_len(length: int) -> Callable[[str], bool]:
    """Функция возвращает предикат, который будет определять минимальную длину слова

    :param length: Слова, чья длина больше length, будут возвращать True
    :type length: int
    :return: функция-предикат, определяющая минимальную длину слова
    :rtype: Callable[[str], bool]
    """

    def func(word: str) -> bool:
        return len(word) > length
    return func


def show_statictics(path_to_file: str, top_words_count: int, min_length_word: int) -> None:
    """Функция выводит на экран самые распространенные слова из переданного файла.

    :param path_to_file: путь к файлу
    :type path_to_file: str
    :param top_words_count: количество самых распространенных слов к показу
    :type top_words_count: int
    :param min_length_word: рассматриваются слова, длинной выше этого значения
    :type min_length_word: int
    :return: программа просто выводит значения на экран
    :rtype: None
    """

    get_list_from_file = get_list_from_xml if path_to_file[-3:] == 'xml' else get_list_from_json
    news_from_file = get_list_from_file(path_to_file)
    top_words_from_file = get_top_words(news_from_file, top_words_count, min_len(min_length_word))

    print(f'Топ {top_words_count} слов (длиной более {min_length_word} символов) из файла {path_to_file}:')
    for i, top_word in enumerate(top_words_from_file):
        print(f'\t{i + 1}) {top_word}')


if __name__ == '__main__':
    show_statictics('newsafr.json', top_words_count=10, min_length_word=6)
    print()
    show_statictics('newsafr.xml', top_words_count=12, min_length_word=8)
