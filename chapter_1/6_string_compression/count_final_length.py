def count_compression(string):
    length = 0
    count = 0

    for i in range(len(string)):
        count += 1
        if i + 1 == len(string) or string[i] != string[i + 1]:
            length += 1 + len(str(count))
            count = 0
    return length


def compress(string):
    final_length = count_compression(string)
    if final_length >= len(string):
        return string

    compressed = [''] * final_length
    count = 0
    insertion_index = 0
    for i in range(len(string)):
        count += 1
        if i + 1 == len(string) or string[i] != string[i + 1]:
            compressed[insertion_index] = string[i]
            compressed[insertion_index + 1] = str(count)
            insertion_index += 2
            count = 0
    return ''.join(compressed)


if __name__ == '__main__':
    print(compress('aabcccccaaa'))
    print(compress('abcde'))
