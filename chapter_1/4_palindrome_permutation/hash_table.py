from collections import defaultdict


def get_frequency_dict(string):
    counts = defaultdict(int)
    for c in string:
        if c.isalnum():
            counts[c.lower()] += 1
    return counts


def check_max_one_odd(counts):
    found_odd = False
    for count in counts.values():
        if count % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


def is_palindrome_permutation(string):
    counts = get_frequency_dict(string)
    return check_max_one_odd(counts)


if __name__ == '__main__':
    print(is_palindrome_permutation('Tact Coa'))
