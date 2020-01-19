from lib.list import create_list


def partition(node, x):
    head = node
    tail = node

    while node is not None:
        next = node.next
        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next

    tail.next = None
    return head


if __name__ == '__main__':
    head = create_list(7)
    print(head)
    print('---')
    print(partition(head, 4))
