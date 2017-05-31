def insertion(input):
    output = []
    for item in input:
        for index in range(0, len(output)):
            if item < output[index]:
                output.insert(index, item)
                break
        else:
            output.append(item)
    return output
