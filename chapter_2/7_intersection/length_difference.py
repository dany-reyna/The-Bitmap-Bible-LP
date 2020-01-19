from lib.list import create_list, get_n


class Wrapper:
    def __init__(self, tail, length):
        self.tail = tail
        self.length = length


def get_tail_and_length(head):
    if head is None:
        return None

    length = 0
    curr = head
    while curr.next is not None:
        length += 1
        curr = curr.next

    return Wrapper(curr, length)


def find_intersection(n1, n2):
    if n1 is None or n2 is None:
        return None

    w1 = get_tail_and_length(n1)
    w2 = get_tail_and_length(n2)
    if w1.tail != w2.tail:
        return None

    shorter = n1 if w1.length < w2.length else n2
    longer = n2 if w1.length < w2.length else n1
    longer = get_n(longer, abs(w1.length - w2.length))

    while shorter != longer:
        shorter = shorter.next
        longer = longer.next
    return shorter


if __name__ == '__main__':
    list = create_list(4)
    a = create_list(6)
    b = create_list(3)
    a.append_node_to_tail(list)
    b.append_node_to_tail(list)
    print(f'List a: {a}')
    print(f'List b: {b}')

    intersection = find_intersection(a, b)
    print(f'Intersection: {intersection}')
