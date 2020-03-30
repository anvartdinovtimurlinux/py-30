from time import time, localtime
from random import randint


class ExecutionTime:
    def __init__(self, function):
        self.function = function

    def __enter__(self):
        self.start_time = time()
        print(f'Время начала работы функции - {self.get_time_to_print(self.start_time)}')
        return self.function

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish_time = time()
        print(f'Время окончания работы функции - {self.get_time_to_print(self.finish_time)}')
        print(f'Время работы функции {self.function.__name__} - {(self.finish_time - self.start_time):.8f}c')

    def get_time_to_print(self, time):
        return ':'.join(map(str, list(localtime(time))[3:6]))


def get_random_number_list(list_length: int) -> list:
    return [randint(0, 999) for _ in range(list_length)]


def bubble_sort(unsorted_list: list) -> list:
    sorted_list = list.copy(unsorted_list)

    i = 0
    list_length = len(sorted_list)
    while i < list_length - 1:
        j = 0
        while j < list_length - 1 - i:
            if sorted_list[j + 1] < sorted_list[j]:
                sorted_list[j + 1], sorted_list[j] = sorted_list[j], sorted_list[j + 1]
            j += 1
        i += 1

    return sorted_list


def selection_sort(unsorted_list: list) -> list:
    sorted_list = list.copy(unsorted_list)

    list_length = len(sorted_list)
    for i in range(list_length):
        min_index = i
        for j in range(i + 1, list_length):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j
        if min_index != i:
            value = sorted_list[min_index]
            for k in range(min_index, i - 1, -1):
                sorted_list[k] = sorted_list[k - 1]
            sorted_list[i] = value

    return sorted_list


if __name__ == '__main__':
    random_list_10 = get_random_number_list(10)
    random_list_1000 = get_random_number_list(1000)
    random_list_5000 = get_random_number_list(5000)

    print('Пример корректной работы функций сортировки')
    print(f'Оригинальный список:\n\t{random_list_10}')
    print(f'Отсортированный с помощью функции bubble_sort\n\t{bubble_sort(random_list_10)}')
    print(f'Отсортированный с помощью функции selection_sort\n\t{selection_sort(random_list_10)}')
    print('<------------------------------>\n')

    print('Сравнение времени сортировки на списке из 1000 элементов')
    with ExecutionTime(bubble_sort) as func:
        func(random_list_1000)
    print()
    with ExecutionTime(selection_sort) as func:
        func(random_list_1000)
    print('<------------------------------>\n')

    print('Сравнение времени сортировки на списке из 5000 элементов')
    with ExecutionTime(bubble_sort) as func:
        func(random_list_5000)
    print()
    with ExecutionTime(selection_sort) as func:
        func(random_list_5000)
    print('<------------------------------>')
