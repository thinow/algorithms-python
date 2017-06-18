def count_on_the_fly(array):
    count = {}

    for letter in array:
        amount = count[letter] if letter in count else 0
        count[letter] = amount + 1

    return count


def count_in_array(letter, array):
    count = 0
    for actual in array:
        if letter == actual:
            count += 1
    return count


def count_with_all_letters(array):
    count = {}

    for code in range(ord('A'), ord('Z') + 1):
        letter = chr(code)
        letter_count = count_in_array(letter, array)

        if letter_count != 0:
            count[letter] = letter_count

    return count
