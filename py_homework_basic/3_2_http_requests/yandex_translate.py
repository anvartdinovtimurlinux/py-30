import requests


def translate_text(text: str, lang: str) -> str:
    """Функция принимает строку, переводит ее и возвращает результат
    :param text: оригинальная строка
    :type text: str
    :param lang: переведенная строка
    :type lang: str
    :return: str
    """

    API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': API_KEY,
        'text': text,
        'lang': lang,
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    print(json_)  # удалить перед заливкой на гит
    return json_['text'][0]


def translate_file(path_to_file_from: str, path_to_file__to: str, from_lang: str, to_lang: str = 'ru') -> None:
    """Функция переводит текст из файла и сохраняет результат в файл
    :param path_to_file_from: путь к файлу с оригинальным текстом
    :type path_to_file__to: str
    :param path_to_file__to: путь к файлу с результатом перевода
    :type path_to_file_from: str
    :param from_lang: язык оригинального текста
    :type from_lang: str
    :param to_lang: языка перевода
    :type to_lang: str
    :return: None
    """

    translate_list = []
    with open(path_to_file_from, 'r', encoding='utf-8') as f:
        for untranslated_str in f:
            translate_str = translate_text(untranslated_str, f'{from_lang}-{to_lang}')
            translate_list.append(translate_str)

    with open(path_to_file__to, 'a', encoding='utf-8') as f:
        for translate_str in translate_list:
            f.write(translate_str)
        f.write('\n')


if __name__ == '__main__':
    translate_file('FR.txt', 'fr-ru.txt', 'fr', 'ru')
