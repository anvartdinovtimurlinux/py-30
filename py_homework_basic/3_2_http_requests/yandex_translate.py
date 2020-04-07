import requests


def translate_text(text: str, lang: str) -> str:
    """Функция принимает строку, переводит ее и возвращает результат
    :param text: оригинальная строка
    :type text: str
    :param lang: направление перевода в формате 'fr-ru'
    :type lang: str
    :return: переведенная строка
    :rtype: str
    """

    TRANSLATE_API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
    TRANSLATE_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': TRANSLATE_API_KEY,
        'text': text,
        'lang': lang,
    }

    response = requests.get(TRANSLATE_URL, params=params)
    json_ = response.json()
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
        print('Файл с переводом успешно создан')


def upload_file_to_yandex(path_to_file: str) -> None:
    """функция принимает путь к файлу и загружает его на Яндекс Диск
    :param path_to_file: путь к файлу
    :type path_to_file: str
    :return: None
    """

    DISK_API_KEY = 'AgAAAAAUYK24AADLWxPpeySqGUjrm5nE6MlEKn0'
    DISK_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    headers = {
        'Authorization': f'OAuth {DISK_API_KEY}',
    }
    params = {
        'path': f'/test_for_netology/{path_to_file}',
        'overwrite': True,
    }

    response_get_link = requests.get(DISK_URL, headers=headers, params=params)
    if response_get_link.status_code >= 400:
        print(f'Ошибка - {response_get_link.status_code}')
        return

    link_to_upload = response_get_link.json()['href']
    with open(path_to_file, 'rb') as f:
        response_upload_file = requests.put(link_to_upload, files={'file': f})
        if response_upload_file.status_code >= 400:
            print(f'Упс, что-то пошло не так - {response_upload_file.status_code}')
            return
        print('Файл успешно загружен')


if __name__ == '__main__':
    translate_file('FR.txt', 'fr-ru.txt', 'fr', 'ru')
    upload_file_to_yandex('fr-ru.txt')
