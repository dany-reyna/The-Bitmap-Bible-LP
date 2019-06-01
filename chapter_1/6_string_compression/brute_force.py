def compress(string):
    compressed = ""
    count = 0

    for i in range(len(string)):
        count += 1
        if i + 1 == len(string) or string[i] != string[i + 1]:
            compressed = f'{compressed}{string[i]}{count}'
            count = 0
    return compressed if len(compressed) < len(string) else string


if __name__ == '__main__':
    print(compress('aabcccccaaa'))
    print(compress('abcde'))
