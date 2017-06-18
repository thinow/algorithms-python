from sort.core import swap


def recursive_sort(array, start, end):
    if end - start <= 1:
        return

    pivot = start

    for evaluated in range(start + 1, end):
        if array[pivot] > array[evaluated]:
            swap(array, pivot + 1, evaluated)
            swap(array, pivot + 1, pivot)
            pivot += 1

    recursive_sort(array, start, pivot)
    recursive_sort(array, pivot + 1, end)


def sort_quick(array):
    recursive_sort(array, 0, len(array))
