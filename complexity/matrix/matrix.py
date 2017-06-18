def sum_two_dimension(matrix):
    sum = 0

    for line in matrix:
        for cell in line:
            if cell:
                sum += cell

    return sum


def sum_one_dimension(matrix):
    sum = 0

    for (row, column, value) in matrix:
        sum += value

    return sum
