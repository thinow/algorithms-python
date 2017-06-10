def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def insertion(array):
    for index in range(1, len(array)):
        position = index

        while position > 0 and array[position - 1] > array[position]:
            swap(array, position - 1, position)
            position -= 1


def selection(array):
    for index in range(0, len(array)):

        index_min = index
        for index_potential_min in range(index + 1, len(array)):
            if array[index_potential_min] < array[index_min]:
                index_min = index_potential_min

        swap(array, index, index_min)
