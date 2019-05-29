def replaceSpaces(string):
    stripped = string.strip()
    return '%20'.join(stripped.split())


if __name__ == '__main__':
    print(replaceSpaces('Mr John Smith    '))
