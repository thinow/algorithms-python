from sort.core import swap


def sort_insertion_using_gap(array, start, gap):
    for index in range(start + gap, len(array), gap):
        position = index

        while position > 0 and array[position - gap] > array[position]:
            swap(array, position - gap, position)
            position -= gap


def sort_shell(array):
    for gap in [6, 4, 3, 2, 1]:
        for start in range(0, gap):
            sort_insertion_using_gap(array, start, gap)
