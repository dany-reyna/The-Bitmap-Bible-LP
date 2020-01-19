from lib.list import create_list, Node


def partition(node, x):
    start_before = None
    end_before = None
    start_after = None
    end_after = None

    while node is not None:
        next = node.next
        node.next = None

        if node.data < x:
            if start_before is None:
                start_before = node
                end_before = start_before
            else:
                end_before.next = node
                end_before = node
        else:
            if start_after is None:
                start_after = node
                end_after = start_after
            else:
                end_after.next = node
                end_after = node
        node = next

    if start_before is None:
        return start_after
    end_before.next = start_after

    return start_before


if __name__ == '__main__':
    head = create_list(7)
    print(head)
    print('---')
    print(partition(head, 4))
