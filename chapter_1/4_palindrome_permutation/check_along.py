from collections import defaultdict


def is_palindrome_permutation(string):
    odd_count = 0
    counts = defaultdict(int)

    for c in string:
        if c.isalnum():
            counts[c.lower()] += 1
            if counts[c.lower()] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
    return odd_count <= 1


if __name__ == '__main__':
    print(is_palindrome_permutation('Tact Coa'))
