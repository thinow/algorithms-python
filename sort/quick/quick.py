from sort.core import swap


def partition(array, start, end):
    pivot = start

    for evaluated in range(start + 1, end):
        if array[pivot] > array[evaluated]:
            swap(array, pivot + 1, evaluated)
            swap(array, pivot + 1, pivot)
            pivot += 1

    return pivot


def recursive_sort(array, start, end):
    # length of the sub-array
    if end - start <= 1:
        return

    pivot = partition(array, start, end)

    recursive_sort(array, start, pivot)
    recursive_sort(array, pivot + 1, end)


def sort_quick(array):
    recursive_sort(array, 0, len(array))
