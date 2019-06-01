def compress(string):
    compressed = []
    count = 0

    for i in range(len(string)):
        count += 1
        if i + 1 == len(string) or string[i] != string[i + 1]:
            compressed.append(string[i])
            compressed.append(str(count))
            count = 0
    return ''.join(compressed) if len(compressed) < len(string) else string


if __name__ == '__main__':
    print(compress('aabcccccaaa'))
    print(compress('abcde'))
