def insertion(array):
    for index in range(1, len(array)):

        value = array[index]
        position = index

        while position > 0 and array[position - 1] > value:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = value
