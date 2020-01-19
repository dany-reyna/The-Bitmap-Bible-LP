from lib.list import Node, create_palindrome_list


def reverse(node):
    head = None
    while node is not None:
        n = Node(node.data)
        n.next = head
        head = n
        node = node.next
    return head


def is_equal(n1, n2):
    while n1 is not None and n2 is not None:
        if n1.data != n2.data:
            return False
        n1 = n1.next
        n2 = n2.next
    return n1 is None and n2 is None


if __name__ == '__main__':
    head = create_palindrome_list(9)
    print(f'Palindrome: {head}')
    backwards = reverse(head)
    print(is_equal(head, backwards))
