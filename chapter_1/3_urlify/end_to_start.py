def replaceSpaces(string, true_length):
    arr = list(string)

    # first scan
    space_count = 0
    for i in range(true_length):
        if arr[i] == ' ':
            space_count += 1

    index = true_length + space_count * 2

    # second scan
    for i in range(true_length - 1, 0, -1):
        if arr[i] == ' ':
            arr[index - 1] = '0'
            arr[index - 2] = '2'
            arr[index - 3] = '%'
            index -= 3
        else:
            arr[index - 1] = arr[i]
            index -= 1

    return ''.join(arr)


if __name__ == '__main__':
    print(replaceSpaces('Mr John Smith    ', 13))
