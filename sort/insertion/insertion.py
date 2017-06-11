from sort.core import swap


def insertion(array):
    for index in range(1, len(array)):
        position = index

        while position > 0 and array[position - 1] > array[position]:
            swap(array, position - 1, position)
            position -= 1
