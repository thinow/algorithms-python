from sort.core import swap


def selection(array):
    for index in range(0, len(array)):

        index_min = index
        for index_potential_min in range(index + 1, len(array)):
            if array[index_potential_min] < array[index_min]:
                index_min = index_potential_min

        swap(array, index, index_min)


def bubble(array):
    # range = from [length -1] to [1]
    for limit in range(len(array) - 1, 1, -1):
        for index in range(0, limit):
            if array[index] > array[index + 1]:
                swap(array, index, index + 1)


def insertion_using_gap(array, start, gap):
    for index in range(start + gap, len(array), gap):
        position = index

        while position > 0 and array[position - gap] > array[position]:
            swap(array, position - gap, position)
            position -= gap


def shell(array):
    for gap in [6, 4, 3, 2, 1]:
        for start in range(0, gap):
            insertion_using_gap(array, start, gap)
