def insertion(array):
    for index in range(1, len(array)):

        value = array[index]
        position = index

        while position > 0 and array[position - 1] > value:
            array[position] = array[position - 1]
            position -= 1

        array[position] = value


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def selection(array):
    for index in range(0, len(array)):

        index_min = index
        for index_potential_min in range(index + 1, len(array)):
            if array[index_potential_min] < array[index_min]:
                index_min = index_potential_min

        swap(array, index, index_min)