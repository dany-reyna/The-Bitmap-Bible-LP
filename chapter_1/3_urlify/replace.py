def replaceSpaces(string):
    stripped = string.strip()
    return stripped.replace(' ', '%20')


if __name__ == '__main__':
    print(replaceSpaces('Mr John Smith    '))
