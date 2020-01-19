from lib.list import Node, create_palindrome_list


class Result:
    def __init__(self, is_pal, node):
        self.is_pal = is_pal
        self.node = node


def is_palindrome(head, length):
    if head is None or length == 0:
        return Result(True, head)
    elif length == 1:
        return Result(True, head.next)
    result = is_palindrome(head.next, length - 2)

    if not result.is_pal:
        return result

    result.is_pal = head.data == result.node.data
    result.node = result.node.next

    return result


if __name__ == '__main__':
    head = create_palindrome_list(8)
    print(f'Palindrome: {head}')
    print(is_palindrome(head, len(head)).is_pal)
