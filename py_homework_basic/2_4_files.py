import sys
from pprint import pprint


def create_cook_book(path_to_file: str) -> dict:
    """
    Функция читает файл с рецептами и возвращает
    словарь с рецептами
    :param str path_to_file: путь к файлу
    :return dict cook_book: словарь с рецептами
    """
    cook_book = {}

    with open(path_to_file, encoding='utf8') as f:
        while True:
            dish = f.readline().strip()
            if not dish:
                break
            cook_book[dish] = []

            ingredients_amount = int(f.readline().strip())
            for _ in range(ingredients_amount):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                cook_book[dish].append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure,
                })

            f.readline()  # Пустая строка отделяет в файле одно блюдо от другого

    return cook_book


def get_shop_list_by_dishes(dishes_list: list, persons_amount: int) -> dict:
    """
    Функция принимает список блюд из cook_book и количество персон
    И возвращает словарь с названием ингредиентов и их количество для закупки
    :param list dishes_list: список блюд
    :param int persons_amount: количество персон
    :return dict shop_list_by_dishes: словарь с ингридеантами и количеством
    """
    shop_list_by_dishes = {}

    for dish in dishes_list:
        ingredients = new_cook_book[dish]

        for ingredient in ingredients:
            ingredient_name = ingredient['ingredient_name']
            shop_list_by_dishes[ingredient_name] = shop_list_by_dishes.get(ingredient_name, {
                'measure': ingredient['measure'],
                'quantity': 0,
            })
            shop_list_by_dishes[ingredient_name]['quantity'] += ingredient['quantity'] * persons_amount

    return shop_list_by_dishes


if __name__ == '__main__':
    try:
        new_cook_book = create_cook_book('2_5_context/recipes.txt')
    except FileNotFoundError:
        print('Неправильный путь к файлу')
        sys.exit()

    new_shop_list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    pprint(new_shop_list_by_dishes)
