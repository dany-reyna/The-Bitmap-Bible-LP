def sort_string(string):
    return ''.join(sorted(string))


def permutation(s, t):
    if len(s) != len(t):
        return False
    return sort_string(s) == sort_string(t)


if __name__ == '__main__':
    print(permutation('doaG', 'Goda'))
