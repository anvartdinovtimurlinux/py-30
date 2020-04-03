from collections import Counter
from typing import Callable
import json
import xml.etree.ElementTree as ET


def get_top_words(words: list, top_words_count: int, predicate: Callable[[str], bool]) -> list:
    words_by_predicate = list(map(str.lower, filter(predicate, words)))
    most_common_words = Counter(words_by_predicate).most_common(top_words_count)
    return [word[0] for word in most_common_words]


def get_list_from_json(path_to_file: str) -> list:
    with open(path_to_file) as f:
        news = json.load(f)
    word_from_news = [item['description'].split() for item in news['rss']['channel']['items']]
    return sum(word_from_news, [])


def get_list_from_xml(path_to_file: str) -> list:
    tree = ET.parse(path_to_file)
    root = tree.getroot()
    xml_items = root.findall('channel/item')
    xml_items_list = [item.find('description').text.split() for item in xml_items]
    return sum(xml_items_list, [])


def min_len(length: int) -> Callable[[str], bool]:
    def func(word: str) -> bool:
        return len(word) > length
    return func


def show_statictics(path_to_file: str, top_words_count: int, min_length_word: int) -> None:
    get_list_from_file = get_list_from_xml if path_to_file[-3:] == 'xml' else get_list_from_json
    news_from_file = get_list_from_file(path_to_file)
    top_words_from_file = get_top_words(news_from_file, top_words_count, min_len(min_length_word))

    print(f'Топ {top_words_count} слов (длиной более {min_length_word} символов) из файла {path_to_file}:')
    for i, top_word in enumerate(top_words_from_file):
        print(f'\t{i + 1}) {top_word}')


if __name__ == '__main__':
    show_statictics('newsafr.json', 10, 6)
    print()
    show_statictics('newsafr.xml', 12, 8)

    # news_from_json = get_list_from_json('newsafr.json')
    # top_words_from_json = get_top_words(news_from_json, 10, min_len(6))
    # print('Топ 10 слов новостей из файла newsafr.json:')
    # for i, top_word in enumerate(top_words_from_json):
    #     print(f'\t{i + 1}) {top_word}')
    #
    # print()
    #
    # news_from_xml = get_list_from_xml('newsafr.xml')
    # top_words_from_xml = get_top_words(news_from_xml, 10, min_len(6))
    # print('Топ 10 слов новостей из файла newsafr.xml:')
    # for i, top_word in enumerate(top_words_from_xml):
    #     print(f'\t{i + 1}) {top_word}')
