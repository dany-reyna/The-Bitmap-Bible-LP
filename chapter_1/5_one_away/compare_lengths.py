def one_edit_replace(s1, s2):
    found_diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_diff:
                return False
            found_diff = True
    return True


def one_edit_insert(s1, s2):
    idx1 = 0
    idx2 = 0
    while idx1 < len(s1) and idx2 < len(s2):
        if s1[idx1] != s2[idx2]:
            if idx1 != idx2:
                return False
            idx2 += 1
        else:
            idx1 += 1
            idx2 += 1
    return True


def one_edit_away(s1, s2):
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) == len(s2) + 1:
        return one_edit_insert(s2, s1)
    return False


if __name__ == '__main__':
    print(one_edit_away('pale', 'ple'))
    print(one_edit_away('pales', 'pale'))
    print(one_edit_away('pale', 'bale'))
    print(one_edit_away('pale', 'bake'))
    print(one_edit_away('pale', 'bae'))
