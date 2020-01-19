from lib.list import create_list


def delete_node(node):
    if None in (node, node.next):
        return
    node.data = node.next.data
    node.next = node.next.next


if __name__ == '__main__':
    head = create_list(5)
    node = head
    move_n = 2

    for _ in range(move_n):
        node = node.next

    print(head)
    print('---')
    delete_node(node)
    print(head)
