def is_unique(string):
    checker = 0
    for c in string:
        diff = ord(c) - ord('a')
        mask = 1 << diff
        if checker & mask > 0:
            return False
        checker |= mask
    return True


if __name__ == '__main__':
    print(is_unique('bishop'))
