# Нужно реализовать Польскую нотацию для двух положительных чисел.
# Реализовать нужно будет следующие операции:
# 1) Сложение
# 2) Вычитание
# 3) Умножение
# 4) Деление
# Например, пользователь вводит: + 2 2 Ответ должен быть: 4


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


class NotPositiveIntegerError(Exception):
    pass


while True:
    print('\nПрограмма реализует польскую нотацию для целых положительных чисел')
    print('В данный момент доступны сложение (+), вычитание (-), '
          'умножение (*) и деление (/)')
    print('Введите ваш пример, например "* 2 5"')

    try:
        operator, x, y = input().strip().split()
    except ValueError:
        print('Вы ввели некорректный пример')
        continue

    assert operator in operations, 'Используйте следующие операторы: + - * /'

    try:
        x, y = map(int, (x, y))
        if x < 0 or y < 0 or x != round(x) or y != round(y):
            raise NotPositiveIntegerError('Вы должны вводить положительные целые числа')
        result = operations[operator](x, y)
    except NotPositiveIntegerError as e:
        print(e)
    except ValueError:
        print('Вторым и третьим аргументом должны быть целые положительные числа')
    except ZeroDivisionError:
        print('На ноль делить нельзя! Это ж не джаваскрипт какой-нибудь')
    else:
        result = result if (round(result) == result) else f'{result:.2f}'
        print(f'Результатом {x} {operator} {y} будет {result}')
        break
