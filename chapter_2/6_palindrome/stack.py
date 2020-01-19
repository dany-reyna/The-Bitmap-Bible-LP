from lib.list import Node, create_palindrome_list


def is_palindrome(head):
    base = head
    runner = head
    stack = []

    while runner is not None and runner.next is not None:
        stack.append(base.data)
        base = base.next
        runner = runner.next.next

    if runner is not None:
        base = base.next

    while base is not None:
        if stack.pop() != base.data:
            return False
        base = base.next

    return True


if __name__ == '__main__':
    head = create_palindrome_list(7)
    print(f'Palindrome: {head}')
    print(is_palindrome(head))
