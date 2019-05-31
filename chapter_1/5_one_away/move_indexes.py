def one_edit_away(first, second):
    if abs(len(first) - len(second)) > 1:
        return False

    s1 = first if len(first) < len(second) else second
    s2 = second if len(first) < len(second) else first

    found_diff = False
    idx1 = 0
    idx2 = 0

    while idx1 < len(s1) and idx2 < len(s2):
        if s1[idx1] != s2[idx2]:
            if found_diff:
                return False
            found_diff = True

            if len(s1) == len(s2):
                idx1 += 1
        else:
            idx1 += 1
        idx2 += 1
    return True


if __name__ == '__main__':
    print(one_edit_away('pale', 'ple'))
    print(one_edit_away('pales', 'pale'))
    print(one_edit_away('pale', 'bale'))
    print(one_edit_away('pale', 'bake'))
    print(one_edit_away('pale', 'bae'))
