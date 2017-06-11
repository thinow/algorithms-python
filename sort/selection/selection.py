from sort.core import swap


def sort_selection(array):
    for index in range(0, len(array)):

        index_min = index
        for index_potential_min in range(index + 1, len(array)):
            if array[index_potential_min] < array[index_min]:
                index_min = index_potential_min

        swap(array, index, index_min)
