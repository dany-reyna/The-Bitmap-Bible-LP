def is_substring(s1, s2):
    return s2 in s1


def is_rotation(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    return is_substring(f'{s1}{s1}', s2)


if __name__ == '__main__':
    print(is_rotation('sourcecode', 'codesource'))
