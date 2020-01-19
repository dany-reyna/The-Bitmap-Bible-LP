from lib.list import Node, create_list


class ExtraWrapper:
    def __init__(self):
        self.sum = None
        self.carry = 0


def pad_list(node, padding):
    head = node
    for _ in range(padding):
        head = append_to_head(head, 0)
    return head


def append_to_head(node, d):
    start = Node(d)
    if node is not None:
        start.next = node
    return start


def sum_helper(n1, n2):
    if n1 is None and n2 is None:
        return ExtraWrapper()

    extra = sum_helper(n1.next, n2.next)

    value = extra.carry + n1.data + n2.data
    result = append_to_head(extra.sum, value % 10)

    extra.sum = result
    extra.carry = int(value / 10)

    return extra


def add_lists(n1, n2):
    if len(n1) < len(n2):
        n1 = pad_list(n1, len(n2) - len(n1))
    else:
        n2 = pad_list(n2, len(n1) - len(n2))

    extra = sum_helper(n1, n2)

    if extra.carry > 0:
        return append_to_head(extra.sum, extra.carry)
    return extra.sum


if __name__ == '__main__':
    n1 = create_list(5)
    n2 = create_list(3)
    print(f'List 1: {n1}')
    print(f'List 2: {n2}')
    print(add_lists(n1, n2))
