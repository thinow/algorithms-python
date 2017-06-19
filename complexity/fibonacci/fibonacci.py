def get(index):
    if index <= 1:
        return index
    else:
        return get(index - 2) + get(index - 1)
