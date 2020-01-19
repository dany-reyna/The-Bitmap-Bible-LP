from lib.list import Node, create_list


def add_lists(n1, n2, carry):
    if n1 is None and n2 is None and carry == 0:
        return None

    result = Node()
    value = carry
    if n1 is not None:
        value += n1.data
    if n2 is not None:
        value += n2.data
    result.data = value % 10

    if n1 is not None or n2 is not None:
        extra = add_lists(None if n1 is None else n1.next,
                          None if n2 is None else n2.next,
                          1 if value >= 10 else 0)
        result.next = extra

    return result


if __name__ == '__main__':
    n1 = create_list(3)
    n2 = create_list(4)
    print(f'List 1: {n1}')
    print(f'List 2: {n2}')
    print(add_lists(n1, n2, 0))
