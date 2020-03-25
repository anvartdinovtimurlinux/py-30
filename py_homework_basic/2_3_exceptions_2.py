documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "5455 028765", "name": "Василий Гупкин"},
    {"type": "passport", "number": "5400 028765"},
    {"type": "passport", "number": "5455 002299", "name": "маленький зеленый человечек"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def get_owner(doc_num):
    """
    Функция принимает номер документа и
    возвращает имя человека, которому он принадлежит
    """
    for doc in documents:
        if doc['number'] == doc_num:
            return doc.get('name', 'У этого документа не указан владелец')

    return 'Такой документ в каталоге отсутствует'


def get_type(doc_num):
    """
    Функция принимает номер документа и
    возвращает тип документа
    """
    for doc in documents:
        if doc['number'] == doc_num:
            return doc.get('type', 'У этого документа не указан тип')

    return 'Такой документ в каталоге отсутствует'


def show_documents():
    """
    выведет список всех документов,
    каждый документ на своей строке в формате
    passport "2207 876234" "Василий Гупкин"
    """
    for doc in documents:
        doc_type = doc.get('type', 'тип отсутствует')
        doc_number = doc.get('number', 'номер отсутствует')
        doc_name = doc.get('name', 'имя отсутствует')
        print(f'{doc_type} "{doc_number}" "{doc_name}"')


def get_shell(doc_num):
    """
    Функция принимает номер документа и
    возвращает полку, на которой он находится
    """
    for shell, document in directories.items():
        if doc_num in document:
            return shell

    return 'Такой документ в каталоге отсутствует'


def add_document(doc_num, doc_type, doc_owner, doc_shell):
    """
    Функция принимает номер документа, тип, владельца, номер полки и
    добавляет его в documents и directories
    """
    if doc_shell in directories:
        document = {"type": doc_type, "number": doc_num, "name": doc_owner}
        documents.append(document)
        directories[doc_shell].append(doc_num)
        print('Документ успешно добавлен')
    else:
        print('Полки с таким номером не существует')
        answer = input('Создать эту полку и добавить в нее документ Y/N? ').lower()
        if answer == 'y':
            add_shell(doc_shell)
            add_document(doc_num, doc_type, doc_owner, doc_shell)


def delete_document(doc_num):
    """
    Функция принимает номер документа и
    удаляет документ из documents и directories
    """
    doc_for_delete = None
    for doc in documents:
        if doc['number'] == doc_num:
            doc_for_delete = doc

    if doc_for_delete:
        documents.remove(doc_for_delete)
        directories[get_shell(doc_num)].remove(doc_num)
        print('Документ успешно удален')
    else:
        print('Такой документ в каталоге отсутствует')


def move_document(doc_num, new_shell):
    """
    Функция принимает номер документа,
    полку на которую нужно переместить документ,
    и перемещает документ
    """
    if get_shell(doc_num) != 'Такой документ в каталоге отсутствует':
        doc_type = get_type(doc_num)
        doc_owner = get_owner(doc_num)
        delete_document(doc_num)
        add_document(doc_num, doc_type, doc_owner, new_shell)
    else:
        print('Такого документа в каталоге не обнаружено')


def add_shell(new_shell):
    """
    Функция принимает номер новой полки и
    создает ее
    """
    if new_shell in directories:
        print('Такая полка уже есть')
    else:
        directories[new_shell] = []
        print('Полка создана')


def show_help():
    print('Список команд, поддерживаемых программой:')
    print('1) P  (people)     - по номеру документа возвращает владельца')
    print('2) L  (list)       - выводит список всех документов')
    print('3) S  (shelf)      - по номеру документа возвращает номер полки')
    print('4) A  (add)        - добавляет новый документ в каталог')
    print('5) D  (delete)     - удаляет документ из каталога')
    print('6) M  (move)       - перемещает документ с одной полки на другую')
    print('7) AS (add shelf)  - добавляет новую полку')
    print('8) H  (help)       - выводит список команд, поддерживаемых программой ')
    print('9) Q  (quit)       - прекращает работу')
    print('----И наш новый функционал!!!----')
    print('10) SA  (Show All) - выводит имена всех владельцев документов')


def show_all_owners():
    print('Список всех владельцев:')
    for doc in documents:
        try:
            print(doc['name'])
        except KeyError:
            print(f'У документа {doc["number"]} нет владельца')


def main():
    show_help()

    while True:
        user_input = input('\nВведите команду: ').lower()

        if user_input == 'p' or user_input == '1':
            doc_num = input('Введите номер документа: ')
            print(get_owner(doc_num))

        elif user_input == 'l' or user_input == '2':
            show_documents()

        elif user_input == 's' or user_input == '3':
            doc_num = input('Введите номер документа: ')
            print(get_shell(doc_num))

        elif user_input == 'a' or user_input == '4':
            doc_num = input('Введите номер документа: ')
            doc_type = input('Введите тип документа: ')
            doc_owner = input('Введите имя владельца документа: ')
            doc_shell = input('Введите номер полки, на кототрой будет храниться документ: ')
            add_document(doc_num, doc_type, doc_owner, doc_shell)

        elif user_input == 'd' or user_input == '5':
            doc_num = input('Введите номер документа: ')
            delete_document(doc_num)

        elif user_input == 'm' or user_input == '6':
            doc_num = input('Введите номер документа: ')
            new_shell = input('Введите номер полки, на которую нужно переместить документ: ')
            move_document(doc_num, new_shell)

        elif user_input == 'as' or user_input == '7':
            new_shell = input('Введите номер новой полки: ')
            add_shell(new_shell)

        elif user_input == 'h' or user_input == '8':
            show_help()

        elif user_input == 'q' or user_input == '9':
            print('Пока!')
            break

        elif user_input == 'sa' or user_input == '10':
            show_all_owners()


main()
