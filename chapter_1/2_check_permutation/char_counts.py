from collections import defaultdict


def permutation(s, t):
    if len(s) != len(t):
        return False
    char_counts = defaultdict(int)
    for c in s:
        char_counts[c] = 1
    for c in t:
        char_counts[c] += 1
        if char_counts[c] > 2:
            return False
    return all(count == 2 for count in char_counts.values())


if __name__ == '__main__':
    print(permutation('dog', 'log'))
