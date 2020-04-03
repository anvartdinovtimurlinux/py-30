import sys
from pprint import pprint


class CookBook:
    def __init__(self, path_to_file):
        try:
            self.cook_book = self.create_cookbook_from_file(path_to_file)
        except FileNotFoundError:
            print('Неправильный путь к файлу')
            sys.exit()

    def create_cookbook_from_file(self, path_to_file):
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

    def get_shop_list_by_dishes(self, dishes_list, persons_amount):
        shop_list_by_dishes = {}
        for dish in dishes_list:
            ingredients = self.cook_book[dish]

            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                shop_list_by_dishes[ingredient_name] = shop_list_by_dishes.get(ingredient_name, {
                    'measure': ingredient['measure'],
                    'quantity': 0,
                })
                shop_list_by_dishes[ingredient_name]['quantity'] += ingredient['quantity'] * persons_amount
        return shop_list_by_dishes

    def __repr__(self):
        result = []
        for dish, ingredients in self.cook_book.items():
            result.append(f'{dish}:')
            for ingredient in ingredients:
                result.append(f'\t{ingredient["ingredient_name"]} - {ingredient["quantity"]} {ingredient["measure"]}')
        return '\n'.join(result)


my_recipes_book = CookBook('2_5_context/recipes.txt')
print(my_recipes_book)
pprint(my_recipes_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
