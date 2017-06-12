def merge(left, right):
    merged = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged.append(left[0])
            del left[0]
        else:
            merged.append(right[0])
            del right[0]

    merged.extend(left)
    merged.extend(right)

    return merged


def sort_merge(array):
    if len(array) == 1:
        return array

    middle = int(len(array) / 2)
    left = array[:middle]
    right = array[middle:]

    return merge(sort_merge(left), sort_merge(right))
