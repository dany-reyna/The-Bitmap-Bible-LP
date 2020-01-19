from lib.list import create_list


def delete_duplicates(node):
    values = set()
    last_unique = None

    while node is not None:
        if node.data in values:
            last_unique.next = node.next
        else:
            values.add(node.data)
            last_unique = node
        node = node.next


if __name__ == '__main__':
    head = create_list(6)
    print(head)
    print('---')
    delete_duplicates(head)
    print(head)
