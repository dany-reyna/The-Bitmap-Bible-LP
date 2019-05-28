def is_unique(string):
    if len(string) > 128:
        return False

    chars = []
    for c in string:
        if c in chars:
            return False
        chars.append(c)
    return True


if __name__ == '__main__':
    print(is_unique('asda'))
