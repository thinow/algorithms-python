from sort.core import swap


def bubble(array):
    # range = from [length -1] to [1]
    for limit in range(len(array) - 1, 1, -1):
        for index in range(0, limit):
            if array[index] > array[index + 1]:
                swap(array, index, index + 1)
