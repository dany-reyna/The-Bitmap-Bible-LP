def create_bit_vector(string):
    bit_vector = 0
    for c in string:
        if c.isalnum():
            diff = ord(c.lower()) - ord('a')
            mask = 1 << diff

            if bit_vector & mask == 0:
                bit_vector |= mask
            else:
                bit_vector &= ~mask
    return bit_vector


def check_one_bit_set(bit_vector):
    return (bit_vector & (bit_vector - 1)) == 0


def is_palindrome_permutation(string):
    bit_vector = create_bit_vector(string)
    return bit_vector == 0 or check_one_bit_set(bit_vector)


if __name__ == '__main__':
    print(is_palindrome_permutation('Tact Coa'))
