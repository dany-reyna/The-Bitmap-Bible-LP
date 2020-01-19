from lib.list import create_list


def delete_duplicates(node):
    current = node
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


if __name__ == '__main__':
    head = create_list(6)
    print(head)
    print('---')
    delete_duplicates(head)
    print(head)
