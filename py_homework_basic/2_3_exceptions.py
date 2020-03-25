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

while True:
    print('\nПрограмма реализует польскую нотацию для целых положительных чисел')
    print('В данный момент доступны сложение (+), вычитание (-), '
          'умножение (*) и деление (/)')
    print('Введите ваш пример, например "* 2 5"')

    try:
        operator, x, y = input().strip().split()
        assert operator in operations
        x, y = map(int, (x, y))
        assert x > 0 and y > 0 and x == round(x) and y == round(y)

        result = operations[operator](x, y)
    except (ValueError, AssertionError):
        print('Вы ввели некорректный пример')
    except ZeroDivisionError:
        print('На ноль делить нельзя! Это ж не джаваскрипт какой-нибудь')
    else:
        result = result if (round(result) == result) else f'{result:.2f}'
        print(f'Результатом {x} {operator} {y} будет {result}')
        break
